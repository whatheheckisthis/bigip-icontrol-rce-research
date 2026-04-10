# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/ingestion/dedup.py
# Purpose    : Provides deterministic fingerprinting and duplicate checks for CVE records
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V14.2.1
# OWASP Ref  : A06
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
import hashlib
from typing import Iterable

def fingerprint(cve_id: str, cvss_vector: str, affected_versions: Iterable[str]) -> str:
    material = "|".join([cve_id, cvss_vector, *sorted(affected_versions)])
    return hashlib.sha256(material.encode("utf-8")).hexdigest()
