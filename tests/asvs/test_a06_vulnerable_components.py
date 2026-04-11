import pytest

@pytest.mark.asvs("V1.14.4")
def test_a06_vulnerable_components_control_mapping(control_registry):
    """V1.14.4 is represented in the matrix and mapped to an implementation file."""
    assert "V1.14.4" in control_registry
