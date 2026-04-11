# Repository : bigip-icontrol-rce-research
# Path       : services/reconciliation/audit_trail.py
# Purpose    : Persists immutable mutation records for conflict resolution actions.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V7.1.1
# OWASP Ref  : A09
# Modified   : 2026-04-11
import json
import os

from sqlalchemy import create_engine, text

LEDGER_PATH = os.environ.get("LEDGER_PATH", "/tmp/reconciliation-ledger.db")


class AuditTrail:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{LEDGER_PATH}")
        with self.engine.begin() as conn:
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

    def record_mutation(self, record_id, before, after, strategy, operator_id):
        with self.engine.begin() as conn:
            conn.execute(text("INSERT INTO audit_trail (record_id, before_json, after_json, strategy, operator_id) VALUES (:r,:b,:a,:s,:o)"), {"r": record_id, "b": json.dumps(before, sort_keys=True), "a": json.dumps(after, sort_keys=True), "s": strategy, "o": operator_id})

    def get_trail(self, record_id: str) -> list[dict]:
        with self.engine.begin() as conn:
            rows = conn.execute(text("SELECT * FROM audit_trail WHERE record_id = :r ORDER BY mutation_time ASC"), {"r": record_id}).mappings().all()
        return [dict(r) for r in rows]

    def update(self, *_args, **_kwargs):
        raise NotImplementedError("evidence ledger is append-only")

    def delete(self, *_args, **_kwargs):
        raise NotImplementedError("evidence ledger is append-only")
