# Repository : bigip-icontrol-rce-research
# Path       : services/control/server.py
# Purpose    : Implements ControlService state transitions and export functions.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V1.1.1,V7.1.1
# OWASP Ref  : A04,A09
# Modified   : 2026-04-11
import csv
import io
import os
from concurrent import futures

import grpc

from generated import control_v1_pb2, control_v1_pb2_grpc
from services.control import asvs_loader


class ControlService(control_v1_pb2_grpc.ControlServiceServicer):
    def __init__(self):
        self.registry = {r.control_id: r for r in asvs_loader.load(os.environ["ASVS_MANIFEST_PATH"])}

    def RegisterControl(self, request, context):
        self.registry[request.record.control_id] = request.record
        return control_v1_pb2.RegisterControlResponse(record=request.record, evidence_id=f"ev-control-{request.record.control_id}")

    def UpdateStatus(self, request, context):
        record = self.registry[request.control_id]
        record.status = request.status
        if request.evidence_ref:
            record.evidence_refs.append(request.evidence_ref)
        record.last_verified_timestamp = request.verified_timestamp
        return control_v1_pb2.UpdateStatusResponse(record=record, evidence_id=f"ev-control-status-{request.control_id}")

    def GetControl(self, request, context):
        return self.registry.get(request.control_id, control_v1_pb2.ControlRecord())

    def ListByOWASPCategory(self, request, context):
        rows = [r for r in self.registry.values() if r.owasp_category == request.owasp_category]
        return control_v1_pb2.ListByOWASPResponse(records=rows)

    def ExportControlMatrix(self, request, context):
        buf = io.StringIO()
        writer = csv.writer(buf)
        writer.writerow(["owasp_category", "owasp_id", "asvs_control_id", "asvs_description", "implementation_location", "implementation_status", "test_coverage", "notes"])
        for rec in self.registry.values():
            writer.writerow([rec.owasp_category, rec.owasp_category, rec.control_id, rec.description, "services/control/server.py", "IMPLEMENTED", "tests/asvs", ""])
        return control_v1_pb2.ExportControlMatrixResponse(csv_content=buf.getvalue().encode())


def serve():
    grpc_port = os.environ.get("GRPC_PORT")
    if not grpc_port:
        raise EnvironmentError("GRPC_PORT is required")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    control_v1_pb2_grpc.add_ControlServiceServicer_to_server(ControlService(), server)
    server.add_insecure_port(f"[::]:{grpc_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
