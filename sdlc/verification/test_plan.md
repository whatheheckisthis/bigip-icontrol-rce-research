<!--
Repository : bigip-icontrol-rce-research
Path       : sdlc/verification/test_plan.md
Purpose    : Defines verification strategy and boundaries for the research harness.
Layer      : sdlc
SDLC Phase : verification
ASVS Ref   : N/A
OWASP Ref  : N/A
Modified   : 2026-04-11
-->
# Scope
Validate proto contracts, service logic, and OWASP/ASVS control assertions.

# Entry Criteria
Generated stubs are current, dependencies installed, and services build cleanly.

# Exit Criteria
Unit, integration, and ASVS suites pass and release gate checks are green.

# Test Categories
- unit
- integration
- asvs

# Out of Scope
live exploitation, SIEM integration, reverse shells, file writes, any payload beyond pattern-extraction test vectors.
