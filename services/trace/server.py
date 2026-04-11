import re
from concurrent import futures

import grpc

from services.trace import capture, replay

TRACE_STORE = {}
ALLOWLIST = re.compile(r"^https?://(127\.|localhost)")


class UrlAllowlistInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        return continuation(handler_call_details)


def validate_url(url: str):
    if not ALLOWLIST.match(url):
        raise ValueError("target_fixture_url must resolve to localhost or 127.0.0.0/8")


class ExploitTraceServiceServicer:
    def CaptureTrace(self, request, context):
        validate_url(request["target_fixture_url"])
        trace = capture.serialise(
            request["request_method"],
            request["target_fixture_url"],
            request.get("request_headers", {}),
            request.get("request_body_raw", ""),
            request.get("response_status", 0),
            request.get("response_body_raw", ""),
        )
        TRACE_STORE[trace.trace_id] = trace
        return type("Resp", (), {"trace_id": trace.trace_id})

    def ReplayTrace(self, request, context):
        trace = TRACE_STORE[request["trace_id"]]
        return replay.replay(trace)


def serve(port: int = 50052):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4), interceptors=[UrlAllowlistInterceptor()])
    server.add_insecure_port(f"0.0.0.0:{port}")
    server.start()
    return server
