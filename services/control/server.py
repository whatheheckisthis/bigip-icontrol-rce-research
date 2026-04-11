import csv
import io
import time

from services.control import asvs_loader


class ControlServiceServicer:
    def __init__(self, manifest_path: str):
        self.registry = {c["control_id"]: c for c in asvs_loader.load(manifest_path)}

    def RegisterControl(self, request, context):
        self.registry[request["control_id"]] = request
        return {"control_id": request["control_id"]}

    def UpdateStatus(self, request, context):
        rec = self.registry[request["control_id"]]
        rec["status"] = request["status"]
        if request.get("evidence_ref"):
            rec.setdefault("evidence_refs", []).append(request["evidence_ref"])
        rec["last_verified_timestamp"] = int(time.time())
        return {"updated": rec}

    def ExportControlMatrix(self, request, context):
        out = io.StringIO()
        writer = csv.DictWriter(out, fieldnames=["control_id", "owasp_category", "description", "status", "evidence_refs", "last_verified_timestamp"])
        writer.writeheader()
        for row in self.registry.values():
            writer.writerow(row)
        return {"csv_content": out.getvalue().encode("utf-8")}
