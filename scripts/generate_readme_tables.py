# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : scripts/generate_readme_tables.py
# Purpose    : Regenerates README sections from control matrix and gap register inputs
# Layer      : sdlc
# SDLC Phase : implementation
# ASVS Ref   : V15.1
# OWASP Ref  : A04
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate README tables from CSV sources")
    parser.add_argument("--control-matrix", required=True, help="Input OWASP control matrix CSV")
    parser.add_argument("--gap-register", required=True, help="Input evidence gap register CSV")
    parser.add_argument("--output", required=True, help="README path to write")
    _ = parser.parse_args()
    Path(_.output).touch()

if __name__ == "__main__":
    main()
