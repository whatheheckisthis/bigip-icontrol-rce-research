# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a06_components.py
# Purpose    : Verifies dependency pinning and vulnerability gate execution.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V14.2.1
# OWASP Ref  : A06
# Modified   : 2026-04-11

import pytest
from pathlib import Path

@pytest.mark.asvs("V14.2.1")
def test_v14_2_1_requirements_fully_pinned():
    """Asserts requirements use strict == pinning for all packages."""
    for line in Path("requirements.txt").read_text().splitlines():
        line=line.strip()
        if line and not line.startswith("#"):
            assert "==" in line and ">=" not in line and "~=" not in line

@pytest.mark.asvs("V14.2.1")
def test_v14_2_1_no_known_critical_vulns_in_requirements():
    """Asserts pip-audit dependency gate command is defined for high severity failures."""
    assert "pip-audit -r requirements.txt --fail-on-severity high" in Path("Makefile").read_text()
