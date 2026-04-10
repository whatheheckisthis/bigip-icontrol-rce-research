# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_asvs_controls.py
# Purpose    : ASVS-tagged tests aligned to OWASP control matrix entries
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V4.1.1, V5.2.3, V10.3.2
# OWASP Ref  : A01, A03, A10
# Modified   : 2026-04-10
# ============================================================
import pytest
from services.trace.capture import classify_payload
from services.trace.server import validate_fixture_url

@pytest.mark.asvs
def test_v5_2_3_input_validation() -> None:
    assert classify_payload("utilCmdArgs=-c id") == "suspicious"

@pytest.mark.asvs
def test_v10_3_2_allowlist() -> None:
    assert validate_fixture_url("http://localhost:8080")
