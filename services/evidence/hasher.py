# Repository : bigip-icontrol-rce-research
# Path       : services/evidence/hasher.py
# Purpose    : Computes and verifies SHA-256 hashes for evidence payloads.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V10.2.1
# OWASP Ref  : A08
# Modified   : 2026-04-11
import hashlib
import json


def hash_content(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def hash_record(record_dict: dict) -> str:
    serialised = json.dumps(record_dict, sort_keys=True).encode("utf-8")
    return hash_content(serialised)


def verify(content: bytes, expected_hash: str) -> bool:
    return hash_content(content) == expected_hash
