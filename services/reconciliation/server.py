# Repository : bigip-icontrol-rce-research
# Path       : services/reconciliation/server.py
# Purpose    : Implements conflict intake, resolution, and unresolved listing.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V7.1.1
# OWASP Ref  : A09
# Modified   : 2026-04-11
import csv
import os
import time
from concurrent import futures

import grpc

from generated import reconciliation_v1_pb2, reconciliation_v1_pb2_grpc
from services.reconciliation.audit_trail import AuditTrail


class ReconciliationService(reconciliation_v1_pb2_grpc.ReconciliationServiceServicer):
    def __init__(self):
        self.records = {}
        self.audit = AuditTrail()

    def SubmitConflict(self, request, context):
        conflict = request.conflict
        self.records[conflict.record_id] = conflict
        if conflict.strategy == reconciliation_v1_pb2.MANUAL:
            gap_path = "evidence_gap_register.csv"
            with open(gap_path, "a", encoding="utf-8", newline="") as handle:
                csv.writer(handle).writerow(["GAP-MANUAL", "HIGH", "Manual resolution pending", conflict.record_id, "unassigned", "2026-12-31", "OPEN", "V7.1.1", "A09", f"conflict:{conflict.record_id}"])
        return reconciliation_v1_pb2.SubmitConflictResponse(conflict_id=conflict.record_id)

    def ResolveConflict(self, request, context):
        conflict = self.records[request.conflict_id]
        before = {"resolved_at": conflict.resolved_at, "resolved_by": conflict.resolved_by}
        conflict.resolved_at = int(time.time())
        conflict.resolved_by = request.operator_id
        self.audit.record_mutation(conflict.record_id, before, {"resolved_at": conflict.resolved_at, "resolved_by": conflict.resolved_by}, request.strategy, request.operator_id)
        return reconciliation_v1_pb2.ResolveConflictResponse(conflict=conflict)

    def GetAuditTrail(self, request, context):
        trail = self.audit.get_trail(request.record_id)
        return reconciliation_v1_pb2.GetAuditTrailResponse(trail_rows=[str(r) for r in trail])

    def ListUnresolved(self, request, context):
        rows = [r for r in self.records.values() if r.resolved_at == 0]
        return reconciliation_v1_pb2.ListUnresolvedResponse(conflicts=rows)


def serve():
    grpc_port = os.environ.get("GRPC_PORT")
    if not grpc_port:
        raise EnvironmentError("GRPC_PORT is required")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    reconciliation_v1_pb2_grpc.add_ReconciliationServiceServicer_to_server(ReconciliationService(), server)
    server.add_insecure_port(f"[::]:{grpc_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
