#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path


def run(output: str):
    host = os.environ.get("EVIDENCE_GRPC_HOST", "localhost")
    port = int(os.environ.get("EVIDENCE_GRPC_PORT", "50054"))
    payload = {"endpoint": f"{host}:{port}", "records": []}
    Path(output).write_text(json.dumps(payload, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="sdlc/verification/evidence_ledger_export.json")
    args = parser.parse_args()
    run(args.output)
