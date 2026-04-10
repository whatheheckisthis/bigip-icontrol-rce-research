from __future__ import annotations

from services.evidence.ledger import EvidenceLedger


class EvidenceService:
    def __init__(self) -> None:
        self.ledger = EvidenceLedger()

    def record(self, evidence: dict) -> str:
        evidence_id = evidence["evidence_id"]
        self.ledger.append(evidence_id, str(evidence))
        return evidence_id
