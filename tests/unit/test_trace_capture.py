# Repository : bigip-icontrol-rce-research
# Path       : tests/unit/test_trace_capture.py
# Purpose    : Unit-tests capture serialisation extraction logic.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V2.1.1,V5.2.3
# OWASP Ref  : A07,A03
# Modified   : 2026-04-11
from services.trace.capture import serialise

def test_serialise_extracts_command_and_token():
    t=serialise("POST","http://127.0.0.1:8080",{},'{"utilCmdArgs":"-c whoami"}',200,'{"selfLink":"https://localhost/mgmt/shared/authz/tokens/a"}')
    assert t.command_injected=="whoami" and t.token_extracted is True
