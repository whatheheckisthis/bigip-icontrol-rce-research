import os
import sqlite3


class EvidenceLedger:
    def __init__(self):
        path = os.environ.get("LEDGER_PATH")
        if not path:
            raise EnvironmentError("LEDGER_PATH is required")
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS evidence_records (
              evidence_id TEXT PRIMARY KEY,
              artefact_type INTEGER,
              source_service TEXT,
              content_hash TEXT,
              content_uri TEXT,
              lineage TEXT,
              created_at INTEGER,
              operator_id TEXT,
              insert_time INTEGER NOT NULL DEFAULT (strftime('%s','now'))
            )
            """
        )
        self.conn.commit()

    def insert(self, record: dict) -> None:
        self.conn.execute(
            "INSERT INTO evidence_records (evidence_id,artefact_type,source_service,content_hash,content_uri,lineage,created_at,operator_id) VALUES (?,?,?,?,?,?,?,?)",
            (
                record["evidence_id"],
                record["artefact_type"],
                record["source_service"],
                record["content_hash"],
                record["content_uri"],
                ",".join(record.get("lineage", [])),
                record["created_at"],
                record.get("operator_id", ""),
            ),
        )
        self.conn.commit()

    def get(self, evidence_id: str) -> dict:
        row = self.conn.execute("SELECT evidence_id,artefact_type,source_service,content_hash,content_uri,lineage,created_at,operator_id FROM evidence_records WHERE evidence_id=?", (evidence_id,)).fetchone()
        if not row:
            raise KeyError(evidence_id)
        return {
            "evidence_id": row[0], "artefact_type": row[1], "source_service": row[2], "content_hash": row[3],
            "content_uri": row[4], "lineage": row[5].split(",") if row[5] else [], "created_at": row[6], "operator_id": row[7]
        }

    def export_all(self) -> list[dict]:
        rows = self.conn.execute("SELECT evidence_id,artefact_type,source_service,content_hash,content_uri,lineage,created_at,operator_id,insert_time FROM evidence_records ORDER BY insert_time ASC").fetchall()
        return [{"evidence_id": r[0], "artefact_type": r[1], "source_service": r[2], "content_hash": r[3], "content_uri": r[4], "lineage": r[5], "created_at": r[6], "operator_id": r[7], "insert_time": r[8]} for r in rows]

    def update(self, *args, **kwargs):
        raise NotImplementedError("evidence ledger is append-only")

    def delete(self, *args, **kwargs):
        raise NotImplementedError("evidence ledger is append-only")
