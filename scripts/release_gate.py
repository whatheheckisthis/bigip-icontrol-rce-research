#!/usr/bin/env python3
import csv
from pathlib import Path


def assert_no_critical_gaps(path: Path) -> bool:
    rows = list(csv.DictReader(path.read_text().splitlines()))
    return not any(r.get("severity") == "CRITICAL" and r.get("status") == "OPEN" for r in rows)


def assert_all_asvs_passed(path: Path) -> bool:
    rows = list(csv.DictReader(path.read_text().splitlines()))
    return not any(r.get("status") != "passed" for r in rows)


if __name__ == "__main__":
    checks = {
        "critical_gap_check": assert_no_critical_gaps(Path("evidence_gap_register.csv")),
        "asvs_status_check": assert_all_asvs_passed(Path("sdlc/verification/asvs_test_matrix.csv")),
    }
    failed = False
    for name, status in checks.items():
        print(f"{'PASS' if status else 'FAIL'} {name}")
        failed = failed or (not status)
    raise SystemExit(1 if failed else 0)
