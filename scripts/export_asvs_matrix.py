#!/usr/bin/env python3
import csv
import datetime as dt
import json
from pathlib import Path


def export(json_report: str, output_csv: str):
    report = json.loads(Path(json_report).read_text())
    rows = []
    for test in report.get("tests", []):
        keywords = test.get("keywords", [])
        asvs = [k.split("(")[1].rstrip(")") for k in keywords if k.startswith("asvs(")]
        for asvs_id in asvs:
            rows.append({
                "asvs_id": asvs_id,
                "test_file": test.get("nodeid", "").split("::")[0],
                "test_name": test.get("nodeid", "").split("::")[-1],
                "status": test.get("outcome", "error"),
                "run_at": dt.datetime.utcnow().isoformat(),
            })
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["asvs_id", "test_file", "test_name", "status", "run_at"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    export(".pytest_cache/v/cache/lastfailed", "sdlc/verification/asvs_test_matrix.csv")
