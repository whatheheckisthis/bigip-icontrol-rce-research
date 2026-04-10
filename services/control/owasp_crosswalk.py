# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/control/owasp_crosswalk.py
# Purpose    : Provides simple ASVS to OWASP category mapping helpers
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V1.1.1
# OWASP Ref  : A04
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations

DEFAULT_MAP: dict[str, str] = {"V5.2.3": "A03", "V10.3.2": "A10"}

def map_asvs_to_owasp(asvs_id: str) -> str:
    return DEFAULT_MAP.get(asvs_id, "UNMAPPED")
