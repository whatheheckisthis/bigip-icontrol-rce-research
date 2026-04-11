# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a08_integrity.py
# Purpose    : Verifies evidence hashing and content integrity operations.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V10.2.1
# OWASP Ref  : A08
# Modified   : 2026-04-11

import pytest
from services.evidence import hasher

@pytest.mark.asvs("V10.2.1")
def test_v10_2_1_evidence_record_has_content_hash():
    """Asserts generated hash has expected SHA-256 hex length."""
    h=hasher.hash_content(b"abc")
    assert len(h)==64

@pytest.mark.asvs("V10.2.1")
def test_v10_2_1_hash_verify_roundtrip():
    """Asserts hash verification succeeds for matching content and digest."""
    h=hasher.hash_content(b"test")
    assert hasher.hash_content(b"test")==h and hasher.verify(b"test",h) is True
