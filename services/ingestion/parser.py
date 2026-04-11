# Repository : bigip-icontrol-rce-research
# Path       : services/ingestion/parser.py
# Purpose    : Maps NVD-style JSON dictionaries to protobuf vulnerability records.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V5.2.3
# OWASP Ref  : A03
# Modified   : 2026-04-11
import time

from generated import vulnerability_v1_pb2


def _require(obj: dict, key: str):
    if key not in obj:
        raise ValueError(f"missing field: {key}")
    return obj[key]


def hydrate(nvd_json: dict) -> vulnerability_v1_pb2.VulnerabilityRecord:
    cve = _require(nvd_json, "cve")
    cve_id = _require(cve, "id")
    metrics = _require(nvd_json, "metrics")
    metric = _require(metrics, "cvssMetricV31")[0]
    cvss_data = _require(metric, "cvssData")
    score = _require(cvss_data, "baseScore")
    vector = _require(cvss_data, "vectorString")
    attack_vector = _require(cvss_data, "attackVector")
    privileges_required = _require(cvss_data, "privilegesRequired")
    affected_versions = []
    for node in _require(nvd_json, "configurations"):
        for cpe in node.get("cpeMatch", []):
            crit = cpe.get("criteria", "")
            if crit:
                affected_versions.append(crit)
    return vulnerability_v1_pb2.VulnerabilityRecord(
        cve_id=cve_id,
        cvss_score=float(score),
        cvss_vector=vector,
        attack_vector=attack_vector,
        privileges_required=privileges_required,
        affected_versions=affected_versions,
        patched_versions=[],
        source_uri=nvd_json.get("source", "nvd"),
        ingestion_timestamp=int(time.time()),
    )
