# Repository : bigip-icontrol-rce-research
# Path       : services/trace/replay.py
# Purpose    : Replays stored traces against localhost fixture endpoints only.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V4.1.1,V10.3.2
# OWASP Ref  : A01,A10
# Modified   : 2026-04-11
import httpx

from generated import exploit_trace_v1_pb2
from services.trace.server import URL_ALLOWLIST_RE


def replay(trace_id: str, store: dict) -> exploit_trace_v1_pb2.ReplayTraceResponse:
    trace = store[trace_id]
    assert URL_ALLOWLIST_RE.match(trace.target_fixture_url)
    r = httpx.post(
        trace.target_fixture_url,
        headers=dict(trace.request_headers),
        content=trace.request_body_raw,
        timeout=10,
    )
    return exploit_trace_v1_pb2.ReplayTraceResponse(trace=trace, response_status=r.status_code, response_body=r.text)
