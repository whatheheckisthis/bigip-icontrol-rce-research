import time

from services.reconciliation import audit_trail, resolver


class ReconciliationServiceServicer:
    def __init__(self, db_path: str):
        self.records = {}
        self.audit = audit_trail.AuditTrail(db_path)

    def SubmitConflict(self, request, context):
        conflict = dict(request["conflict"])
        self.records[conflict["record_id"]] = conflict
        if conflict.get("strategy") == "MANUAL":
            with open("evidence_gap_register.csv", "a", encoding="utf-8") as f:
                f.write(f"\n{conflict['record_id']},HIGH,OPEN,manual review required,secops,2026-05-01")
        return {"record_id": conflict["record_id"]}

    def ResolveConflict(self, request, context):
        rec = self.records[request["record_id"]]
        before = dict(rec)
        rec["strategy"] = request["strategy"]
        rec["resolved_by"] = request["resolved_by"]
        rec["resolved_at"] = int(time.time())
        self.audit.record_mutation(rec["record_id"], before, rec, request["strategy"], request["resolved_by"])
        return {"resolved": rec}

    def ListUnresolved(self, request, context):
        unresolved = [r for r in self.records.values() if int(r.get("resolved_at", 0)) == 0]
        return {"conflicts": unresolved[: request.get("limit", len(unresolved))]}
