<!--
Repository : bigip-icontrol-rce-research
Path       : sdlc/design/control_design.md
Purpose    : Maps OWASP categories to implemented controls and known gaps.
Layer      : sdlc
SDLC Phase : design
ASVS Ref   : V1.1.1
OWASP Ref  : A01-A10
Modified   : 2026-04-11
-->

## A01
Control requirement: Enforce A01 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `services/trace/server.py`.
Gaps: None.

## A02
Control requirement: Enforce A02 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `docker-compose.yml`.
Gaps: GAP-001.

## A03
Control requirement: Enforce A03 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `services/trace/capture.py`.
Gaps: None.

## A04
Control requirement: Enforce A04 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `sdlc/requirements/threat_model.md`.
Gaps: None.

## A05
Control requirement: Enforce A05 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `docker-compose.yml`.
Gaps: None.

## A06
Control requirement: Enforce A06 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `requirements.txt`.
Gaps: None.

## A07
Control requirement: Enforce A07 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `services/trace/capture.py`.
Gaps: None.

## A08
Control requirement: Enforce A08 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `services/evidence/hasher.py`.
Gaps: None.

## A09
Control requirement: Enforce A09 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `services/evidence/ledger.py`.
Gaps: GAP-003.

## A10
Control requirement: Enforce A10 mitigations for CVE-2021-22986 simulation.
Design decision: Implemented deterministic service guardrail and evidence hooks.
Implementation location: `services/trace/server.py`.
Gaps: None.
