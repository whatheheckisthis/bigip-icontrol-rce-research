# Repository : bigip-icontrol-rce-research
# Path       : services/evidence/ledger.py
# Purpose    : Provides append-only SQLite persistence for evidence and audit trail rows.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V7.1.1,V10.2.1
# OWASP Ref  : A09,A08
# Modified   : 2026-04-11
import json
import os

from sqlalchemy import create_engine, text

from generated import evidence_v1_pb2

LEDGER_PATH = os.environ.get("LEDGER_PATH")
if not LEDGER_PATH:
    raise EnvironmentError("LEDGER_PATH is required")


class Ledger:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{LEDGER_PATH}")
        with self.engine.begin() as conn:
            conn.execute(text("""
            CREATE TABLE IF NOT EXISTS evidence_records (
                evidence_id      TEXT PRIMARY KEY,
                artefact_type    INTEGER NOT NULL,
                source_service   TEXT NOT NULL,
                content_hash     TEXT NOT NULL,
                content_uri      TEXT,
                lineage          TEXT,
                created_at       INTEGER NOT NULL,
                operator_id      TEXT,
                insert_time      INTEGER NOT NULL DEFAULT (strftime('%s','now'))
            )
            """))
            conn.execute(text("""
            CREATE TABLE IF NOT EXISTS audit_trail (
                record_id        TEXT NOT NULL,
                before_json      TEXT NOT NULL,
                after_json       TEXT NOT NULL,
                strategy         INTEGER NOT NULL,
                operator_id      TEXT,
                mutation_time    INTEGER NOT NULL DEFAULT (strftime('%s','now'))
            )
            """))

    def insert(self, record: evidence_v1_pb2.EvidenceRecord) -> None:
        with self.engine.begin() as conn:
            conn.execute(text("INSERT INTO evidence_records (evidence_id, artefact_type, source_service, content_hash, content_uri, lineage, created_at, operator_id) VALUES (:e,:a,:s,:h,:u,:l,:c,:o)"), {
                "e": record.evidence_id,
                "a": int(record.artefact_type),
                "s": record.source_service,
                "h": record.content_hash,
                "u": record.content_uri,
                "l": json.dumps(list(record.lineage)),
                "c": int(record.created_at),
                "o": record.operator_id,
            })

    def get(self, evidence_id: str) -> evidence_v1_pb2.EvidenceRecord:
        with self.engine.begin() as conn:
            row = conn.execute(text("SELECT evidence_id, artefact_type, source_service, content_hash, content_uri, lineage, created_at, operator_id FROM evidence_records WHERE evidence_id=:e"), {"e": evidence_id}).mappings().first()
        if not row:
            return evidence_v1_pb2.EvidenceRecord()
        return evidence_v1_pb2.EvidenceRecord(
            evidence_id=row["evidence_id"], artefact_type=row["artefact_type"], source_service=row["source_service"], content_hash=row["content_hash"], content_uri=row["content_uri"] or "", lineage=json.loads(row["lineage"] or "[]"), created_at=row["created_at"], operator_id=row["operator_id"] or ""
        )

    def export_all(self) -> list[dict]:
        with self.engine.begin() as conn:
            rows = conn.execute(text("SELECT * FROM evidence_records ORDER BY insert_time ASC")).mappings().all()
        return [dict(r) for r in rows]

    def update(self, *_args, **_kwargs):
        raise NotImplementedError("evidence ledger is append-only")

    def delete(self, *_args, **_kwargs):
        raise NotImplementedError("evidence ledger is append-only")
