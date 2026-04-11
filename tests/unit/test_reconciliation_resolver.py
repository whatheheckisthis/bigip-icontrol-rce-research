# Repository : bigip-icontrol-rce-research
# Path       : tests/unit/test_reconciliation_resolver.py
# Purpose    : Unit-tests all reconciliation strategies.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V7.1.1
# OWASP Ref  : A09
# Modified   : 2026-04-11
import pytest
from generated import vulnerability_v1_pb2
from services.reconciliation import resolver

def test_resolvers():
    a=vulnerability_v1_pb2.VulnerabilityRecord(source_uri="nvd",ingestion_timestamp=1,cvss_vector="A")
    b=vulnerability_v1_pb2.VulnerabilityRecord(source_uri="vendor",ingestion_timestamp=2,cvss_vector="B")
    assert resolver.resolve_latest_wins(a,b,{"cvss_vector":None}).cvss_vector=="B"
    a2=vulnerability_v1_pb2.VulnerabilityRecord(source_uri="nvd",ingestion_timestamp=1,cvss_vector="A")
    b2=vulnerability_v1_pb2.VulnerabilityRecord(source_uri="vendor",ingestion_timestamp=2,cvss_vector="B")
    assert resolver.resolve_source_priority(a2,b2,{"cvss_vector":None}).cvss_vector=="A"
    with pytest.raises(resolver.ManualResolutionRequired):
        resolver.resolve_manual("x")
