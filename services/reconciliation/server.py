from __future__ import annotations

from datetime import UTC, datetime

from services.reconciliation.audit_trail import AuditTrail


class ReconciliationService:
    def __init__(self) -> None:
        self.audit = AuditTrail()

    def resolve(self, record_id: str, strategy: str, actor: str) -> None:
        stamp = datetime.now(UTC).isoformat()
        self.audit.append(record_id, f"resolved strategy={strategy} actor={actor} at={stamp}")
