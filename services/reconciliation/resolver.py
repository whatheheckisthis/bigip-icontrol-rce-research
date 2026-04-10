# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/reconciliation/resolver.py
# Purpose    : Conflict resolution strategy helpers for latest-wins and manual modes
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V7.1.1
# OWASP Ref  : A09
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations

def resolve(current_value: str, incoming_value: str, strategy: str) -> str:
    if strategy == "LATEST_WINS":
        return incoming_value
    return current_value
