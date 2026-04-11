import logging
import os

from fastapi import FastAPI

assert os.environ.get("FIXTURE_MODE") == "true", "fixture_target must only run with FIXTURE_MODE=true"

app = FastAPI(title="Synthetic iControl Fixture")
logger = logging.getLogger("fixture_target")


@app.post("/mgmt/shared/authn/login")
def login() -> dict:
    return {"selfLink": "https://localhost/mgmt/shared/authz/tokens/SYNTHETIC-TOKEN-001"}


@app.post("/mgmt/tm/util/bash")
def util_bash(payload: dict) -> dict:
    logger.info("exploit_trace", extra={"utilCmdArgs": payload.get("utilCmdArgs", "")})
    return {"commandResult": "synthetic-output\n"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
