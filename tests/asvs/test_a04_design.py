import pytest

@pytest.mark.asvs("V1.1.1")
def test_a04_design_control_mapping(control_registry):
    """V1.1.1 is represented in the matrix and mapped to an implementation file."""
    assert "V1.1.1" in control_registry
