# Repository : bigip-icontrol-rce-research
# Path       : scripts/release_gate.py
# Purpose    : Validates release gate conditions from gap and ASVS matrix artifacts.
# Layer      : scripts
# SDLC Phase : release
# ASVS Ref   : N/A
# OWASP Ref  : N/A
# Modified   : 2026-04-11
import argparse
import csv
import pathlib
import sys
import time


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--gap-register", required=True)
    p.add_argument("--asvs-matrix", required=True)
    args = p.parse_args()
    failed = False

    with open(args.gap_register, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(line for line in f if not line.startswith("#"))]
    critical = [r for r in rows if r["severity"] == "CRITICAL" and r["status"] == "OPEN"]
    if critical:
        print(f"[FAIL] {len(critical)} CRITICAL gap(s) open")
        failed = True
    else:
        print("[OK]   no CRITICAL gaps")

    with open(args.asvs_matrix, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(line for line in f if not line.startswith("#"))]
    not_passed = [r for r in rows if r.get("status") != "passed"]
    if not_passed:
        print(f"[FAIL] {len(not_passed)} ASVS test(s) not passing")
        failed = True
    else:
        print("[OK]   all ASVS tests passing")

    mtime_age = time.time() - pathlib.Path(args.asvs_matrix).stat().st_mtime
    if mtime_age > 86400:
        print("[FAIL] asvs matrix older than 24h")
        failed = True
    else:
        print("[OK]   asvs matrix updated within last 24h")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
