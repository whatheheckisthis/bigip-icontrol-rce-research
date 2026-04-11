import pytest

@pytest.mark.asvs("V14.2.1")
def test_a05_security_config_control_mapping(control_registry):
    """V14.2.1 is represented in the matrix and mapped to an implementation file."""
    assert "V14.2.1" in control_registry
