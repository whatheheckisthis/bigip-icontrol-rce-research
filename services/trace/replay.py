import re

import httpx

from services.trace.capture import ExploitTrace


ALLOWLIST = re.compile(r"^https?://(127\.|localhost)")


def replay(trace: ExploitTrace):
    assert ALLOWLIST.match(trace.target_fixture_url), "target_fixture_url must resolve to localhost or 127.0.0.0/8"
    with httpx.Client() as client:
        response = client.request(
            method=trace.request_method,
            url=trace.target_fixture_url,
            headers=trace.request_headers,
            content=trace.request_body_raw,
            timeout=5.0,
        )
    return {"trace": trace, "response_status": response.status_code, "response_body": response.text}
