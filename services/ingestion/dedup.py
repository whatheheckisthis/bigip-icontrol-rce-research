import hashlib


def generate_fingerprint(record: dict) -> str:
    payload = record["cve_id"] + "|" + record["cvss_vector"] + "|" + "|".join(sorted(record.get("affected_versions", [])))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def check_duplicate(fingerprint: str, store: dict) -> bool:
    return fingerprint in store


def detect_conflict(existing: dict, incoming: dict) -> dict[str, dict]:
    conflicts = {}
    for field in ["cvss_score", "cvss_vector", "attack_vector", "privileges_required", "affected_versions", "patched_versions"]:
        if existing.get(field) != incoming.get(field):
            conflicts[field] = {
                "field_name": field,
                "value_a": str(existing.get(field)),
                "value_b": str(incoming.get(field)),
                "source_a": existing.get("source_uri", "nvd"),
                "source_b": incoming.get("source_uri", "nvd"),
            }
    return conflicts
