import json
import re
import time
import uuid
from dataclasses import dataclass, field


@dataclass
class ExploitTrace:
    trace_id: str
    target_fixture_url: str
    request_method: str
    request_headers: dict[str, str] = field(default_factory=dict)
    request_body_raw: str = ""
    response_status: int = 0
    response_body_raw: str = ""
    command_injected: str = ""
    command_result: str = ""
    token_extracted: bool = False
    timestamp: int = 0
    operator_id: str = ""


def serialise(method, url, headers, body, response_status, response_body):
    payload = json.loads(body or "{}") if isinstance(body, str) else (body or {})
    util = payload.get("utilCmdArgs", "")
    command = util[3:] if isinstance(util, str) and util.startswith("-c ") else util
    token = bool(re.search(r'"selfLink":"https://localhost/mgmt/shared/authz/tokens/', response_body or ""))
    return ExploitTrace(
        trace_id=uuid.uuid4().hex,
        target_fixture_url=url,
        request_method=method,
        request_headers=headers or {},
        request_body_raw=body or "",
        response_status=response_status,
        response_body_raw=response_body or "",
        command_injected=command,
        command_result="synthetic-output" if command else "",
        token_extracted=token,
        timestamp=int(time.time()),
    )
