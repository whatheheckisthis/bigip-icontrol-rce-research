# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a05_misconfig.py
# Purpose    : Verifies local-only fixture binding and internal networking.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V14.4.1
# OWASP Ref  : A05
# Modified   : 2026-04-11

import pytest,yaml
from pathlib import Path

@pytest.mark.asvs("V14.4.1")
def test_v14_4_1_fixture_port_bound_localhost():
    """Asserts fixture docker port binding is localhost-scoped."""
    d=yaml.safe_load(Path("docker-compose.yml").read_text())
    assert "127.0.0.1:8080:8080" in d["services"]["fixture_target"]["ports"]

@pytest.mark.asvs("V14.4.1")
def test_v14_4_1_internal_network_flag_set():
    """Asserts research_internal network is marked internal."""
    d=yaml.safe_load(Path("docker-compose.yml").read_text())
    assert d["networks"]["research_internal"]["internal"] is True
