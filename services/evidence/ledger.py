from __future__ import annotations

import sqlite3
from pathlib import Path


class EvidenceLedger:
    def __init__(self, db_path: str = "evidence.db") -> None:
        self.db_path = db_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS evidence_ledger (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    evidence_id TEXT NOT NULL,
                    payload TEXT NOT NULL
                )
                """
            )

    def append(self, evidence_id: str, payload: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO evidence_ledger(evidence_id, payload) VALUES (?, ?)",
                (evidence_id, payload),
            )
