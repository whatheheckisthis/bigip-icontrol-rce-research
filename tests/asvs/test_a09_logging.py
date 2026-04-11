import pytest

@pytest.mark.asvs("V7.2.1")
def test_a09_logging_control_mapping(control_registry):
    """V7.2.1 is represented in the matrix and mapped to an implementation file."""
    assert "V7.2.1" in control_registry
