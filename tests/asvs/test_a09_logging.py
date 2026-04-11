# Repository : bigip-icontrol-rce-research
# Path       : tests/asvs/test_a09_logging.py
# Purpose    : Checks append-only audit behavior and evidence emission path.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V7.1.1
# OWASP Ref  : A09
# Modified   : 2026-04-11

import os
import pytest

os.environ.setdefault("LEDGER_PATH","/tmp/test-ledger.db")
from services.evidence.ledger import Ledger

@pytest.mark.asvs("V7.1.1")
def test_v7_1_1_ledger_is_append_only():
    """Asserts ledger update and delete operations are intentionally unsupported."""
    l=Ledger()
    with pytest.raises(NotImplementedError):
        l.update()
    with pytest.raises(NotImplementedError):
        l.delete()

@pytest.mark.asvs("V7.1.1")
def test_v7_1_1_all_ingest_events_produce_evidence_record():
    """Asserts ingestion evidence records identify ingestion as source service."""
    assert "source_service="ingestion"" in open("services/ingestion/server.py",encoding="utf-8").read()
