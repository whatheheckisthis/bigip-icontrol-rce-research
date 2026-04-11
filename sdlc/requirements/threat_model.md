<!--
Repository : bigip-icontrol-rce-research
Path       : sdlc/requirements/threat_model.md
Purpose    : Captures STRIDE threats and mapped mitigations for the research harness.
Layer      : sdlc
SDLC Phase : requirements
ASVS Ref   : V1.1.1,V2.1.1,V5.2.3,V7.1.1,V9.2.1
OWASP Ref  : A02,A03,A04,A07,A09
Modified   : 2026-04-11
-->
# Spoofing
Threat: Unauthenticated token extraction on `/mgmt/shared/authn/login`.
Affected component: `services/trace/fixture_target.py`.
Likelihood: H.
Impact: H.
Mitigation: V2.1.1 (A07).

# Tampering
Threat: `utilCmdArgs` injection patterns on `/mgmt/tm/util/bash`.
Affected component: `services/trace/capture.py`.
Likelihood: H.
Impact: H.
Mitigation: V5.2.3 (A03).

# Repudiation
Threat: Missing audit trail on management port 5001 actions.
Affected component: `services/evidence/ledger.py`.
Likelihood: M.
Impact: H.
Mitigation: V7.1.1 (A09) — append-only ledger.

# Information Disclosure
Threat: Token `selfLink` appears in plaintext response body.
Affected component: `services/trace/fixture_target.py`.
Likelihood: M.
Impact: M.
Mitigation: V9.2.1 (A02).

# Elevation
Threat: Basic auth bypass with empty `X-F5-Auth-Token` header.
Affected component: `services/trace/capture.py` and `services/trace/server.py`.
Likelihood: H.
Impact: H.
Mitigation: V2.1.1 (A07), V4.1.1 (A01).
