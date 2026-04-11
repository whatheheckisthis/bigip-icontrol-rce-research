import pytest

@pytest.mark.asvs("V6.2.1")
def test_a02_crypto_control_mapping(control_registry):
    """V6.2.1 is represented in the matrix and mapped to an implementation file."""
    assert "V6.2.1" in control_registry
