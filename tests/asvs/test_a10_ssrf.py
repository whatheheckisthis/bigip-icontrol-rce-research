# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a10_ssrf.py
# Purpose    : Validates SSRF rejection and localhost acceptance behavior.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V10.3.2
# OWASP Ref  : A10
# Modified   : 2026-04-11

import pytest
from services.trace.server import URL_ALLOWLIST_RE

@pytest.mark.asvs("V10.3.2")
def test_v10_3_2_non_localhost_url_rejected():
    """Asserts non-localhost URLs fail the allowlist regex check."""
    assert not URL_ALLOWLIST_RE.match("http://192.168.1.1:8080")

@pytest.mark.asvs("V10.3.2")
def test_v10_3_2_localhost_variants_accepted():
    """Asserts localhost and loopback URLs pass the allowlist regex check."""
    assert URL_ALLOWLIST_RE.match("http://127.0.0.1:8080") and URL_ALLOWLIST_RE.match("http://localhost:8080")

@pytest.mark.asvs("V10.3.2")
def test_v10_3_2_external_ip_rejected():
    """Asserts RFC1918 URLs are rejected by allowlist regex check."""
    assert not URL_ALLOWLIST_RE.match("http://10.0.0.1:8080") and not URL_ALLOWLIST_RE.match("http://192.168.1.1:8080")
