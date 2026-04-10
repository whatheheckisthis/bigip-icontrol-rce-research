# proto/

<!--
Repository : bigip-icontrol-rce-research
Path       : proto/README.md
Purpose    : Documents protobuf contract files and dependency structure
Layer      : docs
SDLC Phase : design
ASVS Ref   : V1.1.2
OWASP Ref  : A04
Modified   : 2026-04-10
-->

Canonical Protocol Buffer contracts for all service APIs.

## Files
- `vulnerability.proto`: CVE ingestion and dedup payloads.
- `exploit_trace.proto`: Trace capture and replay payloads.
- `control.proto`: ASVS/OWASP control registry and status updates.
- `evidence.proto`: Ledger record definitions and export APIs.
- `reconciliation.proto`: Conflict detection and resolution workflows.
