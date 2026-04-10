from __future__ import annotations


class AuditTrail:
    def __init__(self) -> None:
        self.events: dict[str, list[str]] = {}

    def append(self, record_id: str, event: str) -> None:
        self.events.setdefault(record_id, []).append(event)
