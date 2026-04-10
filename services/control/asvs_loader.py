# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/control/asvs_loader.py
# Purpose    : Loads ASVS control IDs and statuses from CSV-derived records
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V1.1.1
# OWASP Ref  : A04
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations

def normalize_control_id(control_id: str) -> str:
    return control_id.strip().upper()
