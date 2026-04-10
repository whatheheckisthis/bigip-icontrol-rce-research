# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : tests/integration/test_pipeline.py
# Purpose    : Integration sanity test for core helper workflow
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V1.1.2
# OWASP Ref  : A04
# Modified   : 2026-04-10
# ============================================================
from services.ingestion.server import ingest_record

def test_pipeline_ingest_returns_hash() -> None:
    assert len(ingest_record("CVE-2021-22986", "AV:N", ["16.0"])) == 64
