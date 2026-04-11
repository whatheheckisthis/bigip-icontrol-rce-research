# Repository : bigip-icontrol-rce-research
# Path       : services/trace/capture.py
# Purpose    : Serialises inbound request/response material into ExploitTrace records.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V2.1.1,V5.2.3
# OWASP Ref  : A07,A03
# Modified   : 2026-04-11
import json
import time
import uuid

from generated import exploit_trace_v1_pb2


def serialise(method, url, headers, body, response_status, response_body):
    body_json = json.loads(body) if body else {}
    raw = body_json.get("utilCmdArgs", "")
    command_injected = raw.lstrip("-c ").strip()
    token_extracted = "selfLink" in response_body and "authz/tokens/" in response_body
    command_result = "synthetic-output" if "commandResult" in response_body else ""
    return exploit_trace_v1_pb2.ExploitTrace(
        trace_id=uuid.uuid4().hex,
        target_fixture_url=url,
        request_method=method,
        request_headers=headers,
        request_body_raw=body,
        response_status=response_status,
        response_body_raw=response_body,
        command_injected=command_injected,
        command_result=command_result,
        token_extracted=token_extracted,
        timestamp=int(time.time()),
        operator_id="system",
    )
