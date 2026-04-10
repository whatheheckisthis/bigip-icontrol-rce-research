# services/

<!--
Repository : bigip-icontrol-rce-research
Path       : services/README.md
Purpose    : Index of all gRPC service implementations and boundaries
Layer      : docs
SDLC Phase : implementation
ASVS Ref   : V1.1.2
OWASP Ref  : A04
Modified   : 2026-04-10
-->

Contains five service implementations: ingestion, trace, control, evidence, and reconciliation.
Each module reads only protobuf contracts from `generated/` and exposes a single service boundary.
