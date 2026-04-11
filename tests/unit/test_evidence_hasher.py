# Repository : bigip-icontrol-rce-research
# Path       : tests/unit/test_evidence_hasher.py
# Purpose    : Unit-tests evidence hashing and verification helper routines.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V10.2.1
# OWASP Ref  : A08
# Modified   : 2026-04-11
from services.evidence.hasher import hash_content, hash_record, verify

def test_hash_verify():
    h=hash_content(b"test")
    assert len(h)==64 and verify(b"test",h)
    assert hash_record({"a":1})==hash_record({"a":1})
