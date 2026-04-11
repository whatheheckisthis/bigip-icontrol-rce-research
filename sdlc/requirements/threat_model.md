# STRIDE Threat Model — CVE-2021-22986 Research Harness

## Spoofing
- **Threat description:** unauthenticated token extraction via `/mgmt/shared/authn/login` allows attacker session spoofing.
- **Affected component:** `services/trace/fixture_target.py` login endpoint.
- **Likelihood:** High.
- **Impact:** High.
- **Mitigation:** `V2.1.1` and `V4.1.1` controls with pre-processing guardrails.

## Tampering
- **Threat description:** `utilCmdArgs` injection attempts to alter system behavior via `/mgmt/tm/util/bash`.
- **Affected component:** trace capture and fixture bash endpoint.
- **Likelihood:** High.
- **Impact:** High.
- **Mitigation:** `V5.2.3` input handling; fixture returns synthetic output only.

## Repudiation
- **Threat description:** management plane events can be denied without immutable audit.
- **Affected component:** evidence and reconciliation mutation history.
- **Likelihood:** Medium.
- **Impact:** High.
- **Mitigation:** append-only ledger and audit trail (`V7.1.1`, `V7.2.1`).

## Information Disclosure
- **Threat description:** token selfLink in response body discloses authentication token path.
- **Affected component:** fixture response and trace persistence.
- **Likelihood:** Medium.
- **Impact:** Medium.
- **Mitigation:** localhost fixture boundary and synthetic token artefacts (`V6.2.1`).

## Elevation of Privilege
- **Threat description:** Basic auth bypass pattern (empty `X-F5-Auth-Token` plus Basic header) implies root-level endpoint access in vulnerable products.
- **Affected component:** auth-path classification in trace service.
- **Likelihood:** High.
- **Impact:** High.
- **Mitigation:** ASVS authentication and SSRF restrictions (`V2.1.1`, `V10.3.2`).
