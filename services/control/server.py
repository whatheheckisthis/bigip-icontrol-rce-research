# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/control/server.py
# Purpose    : Control service aggregation helpers for control records
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V1.1.2
# OWASP Ref  : A04
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
from services.control.owasp_crosswalk import map_asvs_to_owasp

def control_record(asvs_id: str, description: str) -> dict[str, str]:
    return {"asvs_id": asvs_id, "owasp_id": map_asvs_to_owasp(asvs_id), "description": description}
