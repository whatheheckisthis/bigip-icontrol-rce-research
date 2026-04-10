# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/reconciliation/server.py
# Purpose    : Service helper that combines resolver and audit trail operations
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V1.1.2
# OWASP Ref  : A04
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
from services.reconciliation.audit_trail import record
from services.reconciliation.resolver import resolve


def reconcile(current_value: str, incoming_value: str, strategy: str) -> str:
    result = resolve(current_value, incoming_value, strategy)
    record(f"{strategy}:{current_value}->{result}")
    return result
