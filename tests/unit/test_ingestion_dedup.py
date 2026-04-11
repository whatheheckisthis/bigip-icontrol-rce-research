# Repository : bigip-icontrol-rce-research
# Path       : tests/unit/test_ingestion_dedup.py
# Purpose    : Unit-tests dedup fingerprint and conflict detection functions.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V10.2.1
# OWASP Ref  : A08
# Modified   : 2026-04-11
from generated import vulnerability_v1_pb2
from services.ingestion import dedup

def test_fingerprint_and_duplicate():
    r=vulnerability_v1_pb2.VulnerabilityRecord(cve_id="CVE-X",cvss_vector="AV:N",affected_versions=["a","b"])
    fp=dedup.generate_fingerprint(r)
    assert dedup.check_duplicate(fp,{fp:r}) is True
