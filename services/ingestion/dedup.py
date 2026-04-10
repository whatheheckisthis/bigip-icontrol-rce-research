from __future__ import annotations

import hashlib
from dataclasses import dataclass


@dataclass(slots=True)
class CanonicalVulnerability:
    cve_id: str
    cvss_vector: str
    affected_versions: list[str]


def build_fingerprint(record: CanonicalVulnerability) -> str:
    canonical = f"{record.cve_id}|{record.cvss_vector}|{','.join(sorted(record.affected_versions))}"
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
