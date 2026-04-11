# Repository : bigip-icontrol-rce-research
# Path       : scripts/export_evidence.py
# Purpose    : Exports evidence ledger rows into verification artifacts.
# Layer      : scripts
# SDLC Phase : verification
# ASVS Ref   : V10.2.1
# OWASP Ref  : A08
# Modified   : 2026-04-11
import argparse, json, os
os.environ.setdefault("LEDGER_PATH","/tmp/release-ledger.db")
from services.evidence.ledger import Ledger

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); args=ap.parse_args()
    with open(args.output,"w",encoding="utf-8") as f:
        json.dump(Ledger().export_all(),f,indent=2)

if __name__=="__main__":
    main()
