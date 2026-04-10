# OWASP Top 10 Control Design

- A01 Broken Access Control: enforce fixture-only URL constraint in trace service.
- A02 Cryptographic Failures: TLS required for gRPC channels in deployment profile.
- A03 Injection: utilCmdArgs payload validation + detection in trace capture.
- A04 Insecure Design: STRIDE integrated into architecture artefacts.
- A05 Security Misconfiguration: docker-compose binds fixture port to localhost.
- A06 Vulnerable Components: pinned dependencies and `make audit`.
- A07 Auth Failures: model token extraction and Basic bypass trace paths.
- A08 Software Integrity Failures: SHA-256 hashing in EvidenceService.
- A09 Logging Failures: structured logs + append-only evidence ledger.
- A10 SSRF: reject non-localhost/non-127 target fixture URLs.
