# Repository : bigip-icontrol-rce-research
# Path       : services/trace/server.py
# Purpose    : Implements ExploitTraceService with SSRF guardrail and evidence hook.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V4.1.1,V10.3.2
# OWASP Ref  : A01,A10
# Modified   : 2026-04-11
import hashlib
import json
import os
import re
from concurrent import futures

import grpc
import httpx

from generated import evidence_v1_pb2, exploit_trace_v1_pb2, exploit_trace_v1_pb2_grpc
from services.trace import capture

URL_ALLOWLIST_RE = re.compile(r"^https?://(127\.|localhost)")


class ExploitTraceService(exploit_trace_v1_pb2_grpc.ExploitTraceServiceServicer):
    def __init__(self):
        self.store = {}
        self.evidence = {}

    def CaptureTrace(self, request, context):
        url = request.trace.target_fixture_url
        if not URL_ALLOWLIST_RE.match(url):
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "target_fixture_url must resolve to localhost or 127.0.0.0/8")
        trace = capture.serialise(
            request.trace.request_method,
            url,
            dict(request.trace.request_headers),
            request.trace.request_body_raw,
            request.trace.response_status,
            request.trace.response_body_raw,
        )
        self.store[trace.trace_id] = trace
        evidence_id = f"ev-trace-{trace.trace_id}"
        self.evidence[evidence_id] = evidence_v1_pb2.EvidenceRecord(
            evidence_id=evidence_id,
            artefact_type=evidence_v1_pb2.TRACE,
            source_service="trace",
            content_hash=hashlib.sha256(json.dumps({"trace_id": trace.trace_id}, sort_keys=True).encode()).hexdigest(),
            content_uri=f"memory://trace/{trace.trace_id}",
            created_at=trace.timestamp,
            operator_id=trace.operator_id,
        )
        return exploit_trace_v1_pb2.CaptureTraceResponse(trace=trace, evidence_id=evidence_id)

    def ReplayTrace(self, request, context):
        trace = self.store[request.trace_id]
        if not URL_ALLOWLIST_RE.match(trace.target_fixture_url):
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "target_fixture_url must resolve to localhost or 127.0.0.0/8")
        r = httpx.post(trace.target_fixture_url, headers=dict(trace.request_headers), content=trace.request_body_raw, timeout=10)
        return exploit_trace_v1_pb2.ReplayTraceResponse(trace=trace, response_status=r.status_code, response_body=r.text)

    def ListTraces(self, request, context):
        traces = list(self.store.values())[request.offset : request.offset + request.limit]
        return exploit_trace_v1_pb2.ListTracesResponse(traces=traces)

    def ExportTraceBundle(self, request, context):
        chosen = [self.store[i] for i in request.trace_ids if i in self.store]
        data = json.dumps([{"trace_id": t.trace_id, "command_injected": t.command_injected} for t in chosen], sort_keys=True).encode()
        return exploit_trace_v1_pb2.ExportTraceBundleResponse(bundle=data, checksum_sha256=hashlib.sha256(data).hexdigest())


def serve():
    grpc_port = os.environ.get("GRPC_PORT")
    if not grpc_port:
        raise EnvironmentError("GRPC_PORT is required")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    exploit_trace_v1_pb2_grpc.add_ExploitTraceServiceServicer_to_server(ExploitTraceService(), server)
    server.add_insecure_port(f"[::]:{grpc_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
