# Repository : bigip-icontrol-rce-research
# Path       : services/ingestion/server.py
# Purpose    : Implements VulnerabilityService with in-memory deduplication and evidence hooks.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V7.1.1,V10.2.1
# OWASP Ref  : A08,A09
# Modified   : 2026-04-11
import logging
import os
import time
from concurrent import futures

import grpc

from generated import evidence_v1_pb2, reconciliation_v1_pb2, vulnerability_v1_pb2, vulnerability_v1_pb2_grpc
from services.ingestion import dedup, parser


class LoggingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        logging.info("rpc", extra={"ts": int(time.time()), "method": handler_call_details.method, "peer": "unknown"})
        return continuation(handler_call_details)


class VulnerabilityService(vulnerability_v1_pb2_grpc.VulnerabilityServiceServicer):
    def __init__(self):
        self.by_cve = {}
        self.by_fingerprint = {}
        self.evidence = {}

    def IngestCVE(self, request, context):
        record = request.record if request.record.cve_id else parser.hydrate({
            "cve": {"id": ""}, "metrics": {"cvssMetricV31": [{"cvssData": {"baseScore": 0, "vectorString": "", "attackVector": "", "privilegesRequired": ""}}]}, "configurations": []
        })
        fp = dedup.generate_fingerprint(record)
        record.fingerprint = fp
        if dedup.check_duplicate(fp, self.by_fingerprint):
            existing = self.by_fingerprint[fp]
            conflicts = dedup.detect_conflict(existing, record)
            if conflicts:
                _ = reconciliation_v1_pb2.SubmitConflictRequest(
                    conflict=reconciliation_v1_pb2.ConflictRecord(
                        record_id=record.cve_id, record_type="VulnerabilityRecord", conflicts=conflicts
                    )
                )
                return vulnerability_v1_pb2.IngestCVEResponse(accepted=False, duplicate=True, fingerprint=fp)
            return vulnerability_v1_pb2.IngestCVEResponse(accepted=False, duplicate=True, fingerprint=fp)
        evidence_id = f"ev-ingestion-{record.cve_id}"
        self.evidence[evidence_id] = evidence_v1_pb2.EvidenceRecord(
            evidence_id=evidence_id,
            artefact_type=evidence_v1_pb2.LOG,
            source_service="ingestion",
            content_hash=fp,
            content_uri=f"memory://ingestion/{record.cve_id}",
            created_at=int(time.time()),
        )
        self.by_cve[record.cve_id] = record
        self.by_fingerprint[fp] = record
        return vulnerability_v1_pb2.IngestCVEResponse(accepted=True, fingerprint=fp, evidence_id=evidence_id)

    def GetCVE(self, request, context):
        return self.by_cve.get(request.cve_id, vulnerability_v1_pb2.VulnerabilityRecord())

    def ListAffectedVersions(self, request, context):
        rec = self.by_cve.get(request.cve_id)
        return vulnerability_v1_pb2.ListAffectedVersionsResponse(versions=list(rec.affected_versions) if rec else [])

    def DeduplicateFeed(self, request, context):
        ingested = skipped = conflicts = 0
        for rec in request.records:
            response = self.IngestCVE(vulnerability_v1_pb2.IngestCVERequest(record=rec), context)
            if response.accepted:
                ingested += 1
            elif response.duplicate:
                skipped += 1
        return vulnerability_v1_pb2.DeduplicateFeedResponse(ingested=ingested, skipped=skipped, conflicts=conflicts)


def serve():
    grpc_port = os.environ.get("GRPC_PORT")
    if not grpc_port:
        raise EnvironmentError("GRPC_PORT is required")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4), interceptors=[LoggingInterceptor()])
    vulnerability_v1_pb2_grpc.add_VulnerabilityServiceServicer_to_server(VulnerabilityService(), server)
    server.add_insecure_port(f"[::]:{grpc_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
