# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/ingestion/server.py
# Purpose    : Ingestion service entrypoint and in-memory workflow orchestration
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V1.1.2
# OWASP Ref  : A04
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
from services.ingestion.dedup import fingerprint

def ingest_record(cve_id: str, cvss_vector: str, versions: list[str]) -> str:
    return fingerprint(cve_id=cve_id, cvss_vector=cvss_vector, affected_versions=versions)
