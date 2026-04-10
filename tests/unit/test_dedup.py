# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : tests/unit/test_dedup.py
# Purpose    : Unit tests for ingestion fingerprint determinism
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V14.2.1
# OWASP Ref  : A06
# Modified   : 2026-04-10
# ============================================================
from services.ingestion.dedup import fingerprint

def test_fingerprint_deterministic() -> None:
    assert fingerprint("CVE-1", "AV:N", ["1.0", "2.0"]) == fingerprint("CVE-1", "AV:N", ["2.0", "1.0"])
