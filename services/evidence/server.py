# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/evidence/server.py
# Purpose    : Service-level helper to append entries with computed hash metadata
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V10.2.1
# OWASP Ref  : A08
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
from services.evidence.hasher import sha256_text


def build_evidence_record(evidence_id: str, payload: str) -> dict[str, str]:
    return {"evidence_id": evidence_id, "payload": payload, "sha256": sha256_text(payload)}
