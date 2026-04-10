from __future__ import annotations

from services.trace.capture import validate_fixture_url


class ExploitTraceService:
    def __init__(self) -> None:
        self._traces: dict[str, dict] = {}

    def capture_trace(self, trace: dict) -> str:
        target = trace["target_fixture_url"]
        if not validate_fixture_url(target):
            raise ValueError("target_fixture_url must resolve to localhost or 127.0.0.0/8")
        trace_id = trace["trace_id"]
        self._traces[trace_id] = trace
        return trace_id
