# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/evidence/hasher.py
# Purpose    : Computes SHA-256 hashes for serialized evidence payloads
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V10.2.1
# OWASP Ref  : A08
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
import hashlib

def sha256_text(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
