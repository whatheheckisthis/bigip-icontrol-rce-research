# Repository : bigip-icontrol-rce-research
# Path       : scripts/export_asvs_matrix.py
# Purpose    : Converts pytest JSON output into ASVS matrix CSV format.
# Layer      : scripts
# SDLC Phase : verification
# ASVS Ref   : N/A
# OWASP Ref  : N/A
# Modified   : 2026-04-11
import argparse, csv, json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input",required=True); ap.add_argument("--output",required=True); args=ap.parse_args()
    data=json.loads(open(args.input,encoding="utf-8").read()) if open(args.input,encoding="utf-8").read().strip() else {"tests":[]}
    with open(args.output,"w",encoding="utf-8",newline="") as f:
        w=csv.writer(f); w.writerow(["test","status"])
        for t in data.get("tests",[]):
            w.writerow([t.get("nodeid","unknown"), t.get("outcome","failed")])

if __name__=="__main__":
    main()
