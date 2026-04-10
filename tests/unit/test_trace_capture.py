import pytest

from services.trace.capture import validate_fixture_url
from services.trace.server import ExploitTraceService


def test_validate_fixture_url_localhost() -> None:
    assert validate_fixture_url("http://localhost:8080")
    assert validate_fixture_url("https://127.0.0.1:8443")


@pytest.mark.asvs("V5.3.2")
def test_capture_rejects_external_fixture() -> None:
    svc = ExploitTraceService()
    with pytest.raises(ValueError):
        svc.capture_trace({"trace_id": "t1", "target_fixture_url": "http://example.com"})
