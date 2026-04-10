# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/trace/server.py
# Purpose    : Trace service orchestration helpers for capture and replay paths
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V4.1.1
# OWASP Ref  : A01
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
import re

ALLOWLIST = re.compile(r"^https?://(127\\.|localhost)")

def validate_fixture_url(url: str) -> bool:
    return bool(ALLOWLIST.search(url))
