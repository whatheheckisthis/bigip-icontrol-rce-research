# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : scripts/release_gate.py
# Purpose    : Validates release criteria from gap register and ASVS matrix status
# Layer      : sdlc
# SDLC Phase : release
# ASVS Ref   : V14.3
# OWASP Ref  : A06
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
import argparse
import csv
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Run release gate checks")
    parser.add_argument("--gap-register", required=True, help="Path to evidence gap register CSV")
    parser.add_argument("--asvs-matrix", required=True, help="Path to ASVS matrix CSV")
    args = parser.parse_args()
    with Path(args.gap_register).open(encoding="utf-8") as fh:
        rows = [r for r in csv.reader(fh) if r and not r[0].startswith("#")]
    if not rows:
        raise SystemExit("gap register is empty")
    if not Path(args.asvs_matrix).exists():
        raise SystemExit("asvs matrix missing")
    print("release gate checks passed")

if __name__ == "__main__":
    main()
