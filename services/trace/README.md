# services/trace/

<!--
Repository : bigip-icontrol-rce-research
Path       : services/trace/README.md
Purpose    : Service-level documentation for the trace service implementation
Layer      : docs
SDLC Phase : implementation
ASVS Ref   : V1.1.2
OWASP Ref  : A04
Modified   : 2026-04-10
-->

Implements the Trace service contract and contains server entrypoint, domain logic, and container definition.

## Fixture Target
`fixture_target.py` is a FastAPI simulation of selected BIG-IP iControl endpoints and binds to localhost-only.
