import csv
from pathlib import Path


def load(path: str) -> list[dict]:
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"ASVS manifest not found: {path}")
    controls = []
    for row in csv.DictReader(csv_path.read_text().splitlines()):
        controls.append({
            "control_id": row["asvs_id"],
            "owasp_category": row["category"],
            "description": row["requirement_text"],
            "status": "NOT_STARTED",
            "evidence_refs": [],
            "last_verified_timestamp": 0,
        })
    return controls
