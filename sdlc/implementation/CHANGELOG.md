# Changelog

All notable changes to this project are documented in this file.

## [0.1.0] — 2026-04-11

### Added
- proto/ — five protobuf contract definitions (vulnerability, exploit_trace, control, evidence, reconciliation)
- services/ — five gRPC service implementations
- services/trace/fixture_target.py — localhost-bound FastAPI fixture simulating iControl REST surface
- tests/fixtures/exploit_trace_vectors.json — four serialised ExploitTrace test vectors (three positive, one negative SSRF rejection)
- tests/asvs/ — ten ASVS control verification test modules
- sdlc/ — STRIDE threat model, ASVS requirements CSV, architecture doc, control design doc, test plan, release checklist
- owasp_control_matrix.csv — all ten OWASP Top 10 controls mapped
- evidence_gap_register.csv — three open items (GAP-001 HIGH, GAP-002 MEDIUM, GAP-003 LOW)
- Makefile, docker-compose.yml, pyproject.toml, package.json, CI workflow
