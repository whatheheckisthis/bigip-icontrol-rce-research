# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/ingestion/parser.py
# Purpose    : Parses NVD-style JSON into typed vulnerability dictionaries
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V5.1.1
# OWASP Ref  : A03
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
from typing import Any

def parse_nvd_entry(entry: dict[str, Any]) -> dict[str, str]:
    return {
        "cve_id": str(entry.get("id", "")),
        "summary": str(entry.get("summary", "")),
        "cvss_vector": str(entry.get("cvss_vector", "")),
    }
