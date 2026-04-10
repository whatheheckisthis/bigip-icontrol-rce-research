"""Ingestion service placeholder implementation for VulnerabilityService."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


class IngestionService:
    def __init__(self) -> None:
        self._records: dict[str, dict] = {}

    def ingest(self, record: dict) -> tuple[bool, str]:
        cve_id = record["cve_id"]
        if cve_id in self._records and self._records[cve_id]["fingerprint"] == record["fingerprint"]:
            logger.info("deduplicated cve_id=%s", cve_id)
            return False, "duplicate fingerprint"
        self._records[cve_id] = record
        return True, "ingested"
