# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/evidence/ledger.py
# Purpose    : Defines append-only in-memory evidence ledger behavior
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V7.1.1
# OWASP Ref  : A09
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class LedgerEntry:
    evidence_id: str
    payload: str

LEDGER: list[LedgerEntry] = []

def append_entry(entry: LedgerEntry) -> None:
    LEDGER.append(entry)
