# Repository : bigip-icontrol-rce-research
# Path       : tests/unit/test_ingestion_parser.py
# Purpose    : Unit-tests parser.hydrate field mapping and required-field errors.
# Layer      : test
# SDLC Phase : verification
# ASVS Ref   : V5.2.3
# OWASP Ref  : A03
# Modified   : 2026-04-11
import pytest
from services.ingestion.parser import hydrate

def test_hydrate_maps_fields():
    rec=hydrate({"cve":{"id":"CVE-2021-22986"},"metrics":{"cvssMetricV31":[{"cvssData":{"baseScore":9.8,"vectorString":"AV:N","attackVector":"NETWORK","privilegesRequired":"NONE"}}]},"configurations":[{"cpeMatch":[{"criteria":"cpe:/a:f5:big-ip:15.1.0"}]}]})
    assert rec.cve_id=="CVE-2021-22986" and rec.affected_versions[0].startswith("cpe")

def test_hydrate_missing_field():
    with pytest.raises(ValueError):
        hydrate({})
