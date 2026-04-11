# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a03_injection.py
# Purpose    : Validates utilCmdArgs are captured as inert patterns only.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V5.2.3
# OWASP Ref  : A03
# Modified   : 2026-04-11

import pytest
from services.trace.capture import serialise

@pytest.mark.asvs("V5.2.3")
def test_v5_2_3_utilcmdargs_captured_not_executed():
    """Asserts whoami payload is parsed as command_injected and synthetic output only."""
    t=serialise("POST","http://127.0.0.1:8080",{},'{"utilCmdArgs":"-c whoami"}',200,'{"commandResult":"synthetic-output\n"}')
    assert t.command_injected=="whoami" and t.command_result=="synthetic-output"

@pytest.mark.asvs("V5.2.3")
def test_v5_2_3_id_recon_captured_not_executed():
    """Asserts id payload is parsed as command_injected and remains synthetic."""
    t=serialise("POST","http://127.0.0.1:8080",{},'{"utilCmdArgs":"-c id"}',200,'{"commandResult":"synthetic-output\n"}')
    assert t.command_injected=="id"

@pytest.mark.asvs("V5.2.3")
def test_v5_2_3_empty_utilcmdargs_produces_empty_injection_field():
    """Asserts missing utilCmdArgs yields an empty command_injected field."""
    t=serialise("POST","http://127.0.0.1:8080",{},'{}',200,'{}')
    assert t.command_injected==""
