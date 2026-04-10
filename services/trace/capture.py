# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/trace/capture.py
# Purpose    : Classifies trace payloads for injection-like indicators
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V5.2.3
# OWASP Ref  : A03
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations

def classify_payload(body: str) -> str:
    lowered = body.lower()
    if "utilcmdargs" in lowered or "bash -c" in lowered:
        return "suspicious"
    return "benign"
