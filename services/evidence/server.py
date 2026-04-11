# Repository : bigip-icontrol-rce-research
# Path       : services/evidence/server.py
# Purpose    : Implements EvidenceService against the append-only SQLite ledger.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V7.1.1,V10.2.1
# OWASP Ref  : A09,A08
# Modified   : 2026-04-11
import json
import os
import time
from concurrent import futures

import grpc

from generated import evidence_v1_pb2, evidence_v1_pb2_grpc
from services.evidence.ledger import Ledger


class EvidenceService(evidence_v1_pb2_grpc.EvidenceServiceServicer):
    def __init__(self):
        self.ledger = Ledger()

    def RecordEvidence(self, request, context):
        record = request.record
        if not record.created_at:
            record.created_at = int(time.time())
        self.ledger.insert(record)
        return evidence_v1_pb2.RecordEvidenceResponse(evidence_id=record.evidence_id)

    def GetEvidence(self, request, context):
        return self.ledger.get(request.evidence_id)

    def ChainLineage(self, request, context):
        root = self.ledger.get(request.evidence_id)
        lineage = [root]
        for eid in root.lineage:
            lineage.append(self.ledger.get(eid))
        return evidence_v1_pb2.ChainLineageResponse(lineage=lineage)

    def ExportLedger(self, request, context):
        return evidence_v1_pb2.ExportLedgerResponse(ledger_json=json.dumps(self.ledger.export_all(), sort_keys=True).encode())


def serve():
    grpc_port = os.environ.get("GRPC_PORT")
    if not grpc_port:
        raise EnvironmentError("GRPC_PORT is required")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    evidence_v1_pb2_grpc.add_EvidenceServiceServicer_to_server(EvidenceService(), server)
    server.add_insecure_port(f"[::]:{grpc_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
