# Repository : bigip-icontrol-rce-research
# Path       : services/control/asvs_loader.py
# Purpose    : Loads ASVS manifest CSV rows into ControlRecord objects.
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V1.1.1
# OWASP Ref  : A04
# Modified   : 2026-04-11
import csv
from pathlib import Path

from generated import control_v1_pb2


def load(path: str) -> list[control_v1_pb2.ControlRecord]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"ASVS manifest not found: {path}")
    out = []
    with p.open("r", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            out.append(control_v1_pb2.ControlRecord(control_id=row["asvs_id"], owasp_category=row["owasp_category"], description=row["description"], status=control_v1_pb2.NOT_STARTED))
    return out
