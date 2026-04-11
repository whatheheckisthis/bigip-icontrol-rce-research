import pytest

@pytest.mark.asvs("V7.1.1")
def test_a08_integrity_control_mapping(control_registry):
    """V7.1.1 is represented in the matrix and mapped to an implementation file."""
    assert "V7.1.1" in control_registry
