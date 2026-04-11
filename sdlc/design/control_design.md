# Control Design

## A01 — Broken Access Control
- **Control requirement:** enforce access control before business logic.
- **Design decision:** apply URL allowlist as a gRPC interceptor in trace service.
- **Implementation location:** `services/trace/server.py`
- **Trade-offs/gaps:** strict localhost policy limits remote replay scenarios.

## A02 — Cryptographic Failures
- **Control requirement:** protect confidentiality and integrity in transit.
- **Design decision:** replay client only permits localhost fixture and expects HTTP loopback use.
- **Implementation location:** `services/trace/replay.py`
- **Trade-offs/gaps:** fixture mode uses synthetic data, not real cert rotation.

## A03 — Injection
- **Control requirement:** treat utilCmdArgs as data, never executable input.
- **Design decision:** capture extracts command_injected as pattern only.
- **Implementation location:** `services/trace/capture.py`
- **Trade-offs/gaps:** command taxonomy is intentionally narrow to known vectors.

## A04 — Insecure Design
- **Control requirement:** maintain explicit security architecture and boundaries.
- **Design decision:** protobuf-first decomposition with evidence and reconciliation paths.
- **Implementation location:** `sdlc/design/architecture.md`
- **Trade-offs/gaps:** no multi-tenant policy engine in v0.1.0.

## A05 — Security Misconfiguration
- **Control requirement:** secure defaults and explicit fixture constraints.
- **Design decision:** fixture asserts `FIXTURE_MODE=true` and binds to 127.0.0.1.
- **Implementation location:** `services/trace/fixture_target.py`
- **Trade-offs/gaps:** environment-dependent startup assertion can block local misconfigured runs.

## A06 — Vulnerable and Outdated Components
- **Control requirement:** verify baseline toolchain and dependency hygiene.
- **Design decision:** version gates in shell verification script.
- **Implementation location:** `scripts/verify_tools.sh`
- **Trade-offs/gaps:** language package CVEs are checked separately by audit tasks.

## A07 — Identification and Authentication Failures
- **Control requirement:** represent auth paths and detect bypass patterns.
- **Design decision:** trace capture records headers and token extraction state.
- **Implementation location:** `services/trace/server.py`
- **Trade-offs/gaps:** fixture is synthetic and does not model real auth backend.

## A08 — Software and Data Integrity Failures
- **Control requirement:** store immutable evidence entries with hashes.
- **Design decision:** append-only ledger module disallows update/delete APIs.
- **Implementation location:** `services/evidence/ledger.py`
- **Trade-offs/gaps:** pruning and archival policy is tracked in `evidence_gap_register.csv`.

## A09 — Security Logging and Monitoring Failures
- **Control requirement:** persist audit history for conflict resolution mutations.
- **Design decision:** append-only audit trail table in shared SQLite DB.
- **Implementation location:** `services/reconciliation/audit_trail.py`
- **Trade-offs/gaps:** SIEM forwarding remains future work.

## A10 — Server-Side Request Forgery
- **Control requirement:** block non-localhost target_fixture_url values.
- **Design decision:** interceptor rejects anything not matching localhost/127 prefix.
- **Implementation location:** `services/trace/server.py`
- **Trade-offs/gaps:** static allowlist does not yet support named local aliases.
