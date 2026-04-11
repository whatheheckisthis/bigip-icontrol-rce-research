import time


REQUIRED = ["cve.id", "metrics.cvssMetricV31.0.cvssData.baseScore", "metrics.cvssMetricV31.0.cvssData.vectorString"]


def _get(data: dict, path: str):
    cur = data
    for token in path.split('.'):
        if token.isdigit():
            cur = cur[int(token)]
        else:
            cur = cur[token]
    return cur


def parse_nvd(raw: dict) -> dict:
    for req in REQUIRED:
        try:
            _get(raw, req)
        except Exception as exc:
            raise ValueError(req) from exc
    return {
        "cve_id": _get(raw, "cve.id"),
        "cvss_score": float(_get(raw, "metrics.cvssMetricV31.0.cvssData.baseScore")),
        "cvss_vector": _get(raw, "metrics.cvssMetricV31.0.cvssData.vectorString"),
        "attack_vector": _get(raw, "metrics.cvssMetricV31.0.cvssData.attackVector"),
        "privileges_required": _get(raw, "metrics.cvssMetricV31.0.cvssData.privilegesRequired"),
        "affected_versions": raw.get("affected_versions", []),
        "patched_versions": raw.get("patched_versions", []),
        "source_uri": raw.get("source_uri", "https://nvd.nist.gov/"),
        "ingestion_timestamp": int(time.time()),
        "fingerprint": "",
    }
