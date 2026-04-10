from __future__ import annotations

from services.ingestion.dedup import CanonicalVulnerability, build_fingerprint


def parse_nvd_item(item: dict) -> dict:
    cve_id = item["cve"]["id"]
    vector = item["metrics"]["cvssMetricV31"][0]["cvssData"]["vectorString"]
    score = item["metrics"]["cvssMetricV31"][0]["cvssData"]["baseScore"]
    versions = item.get("affected_versions", [])
    fingerprint = build_fingerprint(CanonicalVulnerability(cve_id, vector, versions))
    return {
        "cve_id": cve_id,
        "cvss_score": score,
        "cvss_vector": vector,
        "affected_versions": versions,
        "fingerprint": fingerprint,
    }
