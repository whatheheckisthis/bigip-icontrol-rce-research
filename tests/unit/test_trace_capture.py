# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : tests/unit/test_trace_capture.py
# Purpose    : Unit tests for exploit trace body classification
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V5.2.3
# OWASP Ref  : A03
# Modified   : 2026-04-10
# ============================================================
from services.trace.capture import classify_payload

def test_classify_payload_detects_utilcmdargs() -> None:
    assert classify_payload("utilCmdArgs=-c id") == "suspicious"
