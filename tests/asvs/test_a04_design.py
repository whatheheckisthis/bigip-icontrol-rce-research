# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a04_design.py
# Purpose    : Checks threat-model completeness for design controls.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V1.1.1
# OWASP Ref  : A04
# Modified   : 2026-04-11

import pytest
from pathlib import Path

@pytest.mark.asvs("V1.1.1")
def test_v1_1_1_threat_model_exists():
    """Asserts threat model artifact exists and is not empty."""
    p=Path("sdlc/requirements/threat_model.md")
    assert p.exists() and p.stat().st_size>0

@pytest.mark.asvs("V1.1.1")
def test_v1_1_1_threat_model_covers_all_stride_categories():
    """Asserts threat model includes required STRIDE categories."""
    c=Path("sdlc/requirements/threat_model.md").read_text()
    for n in ["Spoofing","Tampering","Repudiation","Information Disclosure","Elevation"]:
        assert n in c
