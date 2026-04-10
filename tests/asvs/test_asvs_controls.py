import pytest

from services.trace.capture import validate_fixture_url


@pytest.mark.asvs("V4.1.2")
def test_fixture_url_restriction() -> None:
    assert validate_fixture_url("http://localhost:8080")
    assert not validate_fixture_url("http://10.0.0.5:8080")


@pytest.mark.asvs("V1.1.1")
def test_architecture_references_stride() -> None:
    content = open("sdlc/design/architecture.md", encoding="utf-8").read()
    assert "threat_model.md" in content
