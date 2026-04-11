# Repository : bigip-icontrol-rce-research
# Path       : services/ingestion/dedup.py
# Purpose    : Provides deterministic fingerprinting and conflict detection for CVE records.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V10.2.1
# OWASP Ref  : A08
# Modified   : 2026-04-11
import hashlib

from generated import reconciliation_v1_pb2


def generate_fingerprint(record) -> str:
    raw = f"{record.cve_id}|{record.cvss_vector}|{'|'.join(sorted(record.affected_versions))}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def check_duplicate(fingerprint: str, store: dict) -> bool:
    return fingerprint in store


def detect_conflict(existing, incoming) -> dict[str, reconciliation_v1_pb2.ConflictDetail]:
    fields = ["cvss_score", "cvss_vector", "attack_vector", "privileges_required", "source_uri"]
    conflicts = {}
    for field in fields:
        left = getattr(existing, field)
        right = getattr(incoming, field)
        if left != right:
            conflicts[field] = reconciliation_v1_pb2.ConflictDetail(
                field_name=field,
                existing_value=str(left),
                incoming_value=str(right),
            )
    return conflicts
