# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a02_crypto.py
# Purpose    : Validates transport crypto configuration declarations.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V9.2.1
# OWASP Ref  : A02
# Modified   : 2026-04-11

import pytest, yaml
from pathlib import Path

@pytest.mark.asvs("V9.2.1")
def test_v9_2_1_grpc_channel_tls_configured():
    """Asserts docker compose environment includes tls credentials keys for gRPC services."""
    data=yaml.safe_load(Path("docker-compose.yml").read_text())
    for s in ["ingestion","trace","control","evidence","reconciliation"]:
        assert "TLS_CREDENTIALS" in data["services"][s]["environment"]

@pytest.mark.asvs("V9.2.1")
@pytest.mark.xfail(reason="GAP-001 — full chain validation pending")
def test_v9_2_1_fixture_http_localhost_only():
    """Asserts fixture target runs on localhost HTTP without TLS termination."""
    content=Path("services/trace/fixture_target.py").read_text()
    assert 'host="127.0.0.1"' in content and "ssl" not in content
