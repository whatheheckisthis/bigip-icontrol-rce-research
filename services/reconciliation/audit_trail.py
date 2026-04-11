import sqlite3


class AuditTrail:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_trail (
              record_id TEXT,
              before_json TEXT,
              after_json TEXT,
              strategy TEXT,
              operator_id TEXT,
              mutation_time INTEGER DEFAULT (strftime('%s','now'))
            )
            """
        )
        self.conn.commit()

    def record_mutation(self, record_id, before: dict, after: dict, strategy: str, operator_id: str) -> None:
        self.conn.execute(
            "INSERT INTO audit_trail (record_id,before_json,after_json,strategy,operator_id) VALUES (?,?,?,?,?)",
            (record_id, str(before), str(after), strategy, operator_id),
        )
        self.conn.commit()

    def get_trail(self, record_id: str) -> list[dict]:
        rows = self.conn.execute("SELECT record_id,before_json,after_json,strategy,operator_id,mutation_time FROM audit_trail WHERE record_id=? ORDER BY mutation_time ASC", (record_id,)).fetchall()
        return [{"record_id": r[0], "before_json": r[1], "after_json": r[2], "strategy": r[3], "operator_id": r[4], "mutation_time": r[5]} for r in rows]
