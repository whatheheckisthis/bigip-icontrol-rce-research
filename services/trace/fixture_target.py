# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : services/trace/fixture_target.py
# Purpose    : FastAPI fixture endpoints that model iControl request/response behavior safely
# Layer      : service
# SDLC Phase : implementation
# ASVS Ref   : V10.3.2
# OWASP Ref  : A10
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations
from fastapi import FastAPI

app = FastAPI(title="fixture-target")

@app.post("/mgmt/shared/authn/login")
def login() -> dict[str, str]:
    return {"token": "synthetic-token"}

@app.post("/mgmt/tm/util/bash")
def util_bash(payload: dict[str, str]) -> dict[str, str]:
    cmd = payload.get("utilCmdArgs", "")
    return {"commandResult": f"synthetic output for {cmd}"}
