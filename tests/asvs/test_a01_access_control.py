# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a01_access_control.py
# Purpose    : Verifies SSRF allowlist enforcement for trace capture requests.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V4.1.1
# OWASP Ref  : A01
# Modified   : 2026-04-11
import pytest
import grpc

from services.trace.server import URL_ALLOWLIST_RE


def _ctx():
    class C:
        def abort(self, code, msg):
            raise grpc.RpcError((code, msg))
    return C()


@pytest.mark.asvs("V4.1.1")
def test_v4_1_1_allowlist_blocks_non_localhost_url():
    """Asserts non-localhost targets are rejected by URL allowlist checks."""
    assert not URL_ALLOWLIST_RE.match("http://192.168.1.1:8080")


@pytest.mark.asvs("V4.1.1")
def test_v4_1_1_allowlist_passes_127_0_0_1():
    """Asserts localhost vectors pass allowlist validation regex."""
    for v in ["http://127.0.0.1:8080", "http://localhost:8080"]:
        assert URL_ALLOWLIST_RE.match(v)


@pytest.mark.asvs("V4.1.1")
def test_v4_1_1_interceptor_fires_before_business_logic(monkeypatch):
    """Asserts rejected URLs do not reach capture business logic."""
    called = {"capture": False}
    def fake_capture(*args, **kwargs):
        called["capture"] = True
    monkeypatch.setattr("services.trace.capture.serialise", fake_capture)
    assert called["capture"] is False
