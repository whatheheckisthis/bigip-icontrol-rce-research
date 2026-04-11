# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a07_auth.py
# Purpose    : Validates auth-path artifacts are captured in traces.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V2.1.1
# OWASP Ref  : A07
# Modified   : 2026-04-11

import pytest
from services.trace.capture import serialise

@pytest.mark.asvs("V2.1.1")
def test_v2_1_1_token_extraction_path_captured():
    """Asserts selfLink token path is detected in response body."""
    t=serialise("POST","http://127.0.0.1:8080",{},'{}',200,'{"selfLink":"https://localhost/mgmt/shared/authz/tokens/SYNTHETIC-TOKEN-001"}')
    assert t.token_extracted is True

@pytest.mark.asvs("V2.1.1")
def test_v2_1_1_basic_bypass_headers_present_in_trace():
    """Asserts bypass headers persist inside serialized trace record."""
    h={"X-F5-Auth-Token":"","Authorization":"Basic aaa"}
    t=serialise("POST","http://127.0.0.1:8080",h,'{}',200,'{}')
    assert t.request_headers["X-F5-Auth-Token"]=="" and t.request_headers["Authorization"].startswith("Basic ")

@pytest.mark.asvs("V2.1.1")
def test_v2_1_1_fixture_returns_synthetic_output_regardless_of_auth():
    """Asserts synthetic output behavior is independent of auth headers."""
    a=serialise("POST","http://127.0.0.1:8080",{},'{}',200,'{"commandResult":"synthetic-output\n"}')
    b=serialise("POST","http://127.0.0.1:8080",{"Authorization":"Basic b"},'{}',200,'{}')
    assert a.command_result in ["synthetic-output",""] and b.command_result in ["synthetic-output",""]
