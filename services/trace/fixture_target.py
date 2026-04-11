# Repository : bigip-icontrol-rce-research
# Path       : services/trace/fixture_target.py
# Purpose    : Local synthetic target that logs patterns without command execution.
# Layer      : service
# SDLC Phase : verification
# ASVS Ref   : V4.1.1,V5.2.3
# OWASP Ref  : A01,A03
# Modified   : 2026-04-11
from fastapi import FastAPI, Request
import logging
import os
import re

app = FastAPI()
logger = logging.getLogger("fixture_target")

FIXTURE_MODE = os.environ.get("FIXTURE_MODE") == "true"
assert FIXTURE_MODE, "fixture_target must only run with FIXTURE_MODE=true"


@app.post("/mgmt/shared/authn/login")
async def authn_login(request: Request):
    body = await request.json()
    logger.info("authn_login request received", extra={"body": body})
    return {"selfLink": "https://localhost/mgmt/shared/authz/tokens/SYNTHETIC-TOKEN-001"}


@app.post("/mgmt/tm/util/bash")
async def util_bash(request: Request):
    body = await request.json()
    cmd = body.get("utilCmdArgs", "")
    logger.info("util_bash request received", extra={"utilCmdArgs": cmd, "executed": False})
    return {"commandResult": "synthetic-output
"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
