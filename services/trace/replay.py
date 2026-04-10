from __future__ import annotations


def deterministic_replay(trace: dict) -> dict:
    return {
        "response_status": trace.get("response_status", 200),
        "response_body_raw": trace.get("response_body_raw", "ok"),
    }
