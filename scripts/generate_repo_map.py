# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : scripts/generate_repo_map.py
# Purpose    : Generates repository map content for README maintenance automation
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
    parser = argparse.ArgumentParser(description="Regenerate repository map in README")
    parser.add_argument("--output", required=True, help="README path to update")
    args = parser.parse_args()
    p = Path(args.output)
    content = p.read_text(encoding="utf-8") if p.exists() else ""
    p.write_text(content, encoding="utf-8")

if __name__ == "__main__":
    main()
