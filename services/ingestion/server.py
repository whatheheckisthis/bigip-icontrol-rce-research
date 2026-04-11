import os
import time
from concurrent import futures

import grpc

from services.ingestion import dedup, parser

STORE = {}
BY_CVE = {}


class RpcLoggingInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        print({"timestamp": int(time.time()), "method": handler_call_details.method, "peer": "unknown"})
        return continuation(handler_call_details)


class VulnerabilityServiceServicer:
    def IngestCVE(self, request, context):
        record = request.record if isinstance(request.record, dict) else dict(request.record)
        hydrated = parser.parse_nvd(record) if "cve" in record else record
        fp = dedup.generate_fingerprint(hydrated)
        hydrated["fingerprint"] = fp
        if dedup.check_duplicate(fp, STORE):
            if hydrated["cve_id"] in BY_CVE and BY_CVE[hydrated["cve_id"]]["fingerprint"] != fp:
                _ = dedup.detect_conflict(BY_CVE[hydrated["cve_id"]], hydrated)
            return type("Resp", (), {"fingerprint": fp, "deduplicated": True})
        STORE[fp] = hydrated
        BY_CVE[hydrated["cve_id"]] = hydrated
        return type("Resp", (), {"fingerprint": fp, "deduplicated": False})


def serve():
    port = os.environ.get("GRPC_PORT")
    if not port:
        raise EnvironmentError("GRPC_PORT is required")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4), interceptors=[RpcLoggingInterceptor()])
    server.add_insecure_port(f"0.0.0.0:{port}")
    server.start()
    server.wait_for_termination()
