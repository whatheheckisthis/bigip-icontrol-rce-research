<!--
Repository : bigip-icontrol-rce-research
Path       : docs/build.md
Purpose    : Captures the end-to-end build and release gating workflow.
Layer      : docs
SDLC Phase : release
ASVS Ref   : N/A
OWASP Ref  : N/A
Modified   : 2026-04-11
-->
# Two Pipelines
Python pipeline runs through `make`; Node pipeline runs through `npm`; both converge on `docker-compose` deployment.

# Python Pipeline detail
Create a venv, install requirements, run `make proto`, then `make audit`.

# Node Pipeline detail
Use `npm ci` for deterministic installs; prebuild runs tool checks; build runs proto generation then lint; postbuild asserts stub presence.

# Dependency Audit
`pip-audit` enforces high severity gate; `npm audit` enforces high severity; `license-checker` enforces allowlist.

# Service Startup
Run `make services-detach`; check ports 50051-50055 and localhost-only 8080 fixture.

# Build State Gates
`make release` asserts lint, audit, ASVS pass, matrix freshness, and no critical gaps.

# Troubleshooting
Common failures: missing `protoc`, out-of-sync stubs, unset `FIXTURE_MODE`, unset `LEDGER_PATH`.
