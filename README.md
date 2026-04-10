# bigip-icontrol-rce-research

<!--
Repository : bigip-icontrol-rce-research
Path       : README.md
Purpose    : Root documentation for architecture, workflows, and security governance of the research platform
Layer      : docs
SDLC Phase : design
ASVS Ref   : V1.1.1, V15.1
OWASP Ref  : A04
Modified   : 2026-04-10
-->

SecDevOps research platform for analyzing CVE-2021-22986 with reproducible protobuf-first services, ASVS control mapping, and evidence-ledger governance.

## Architecture

```text
┌───────────────┐      ┌──────────────┐      ┌─────────────┐
│ IngestionSvc  │─────▶│ EvidenceSvc  │◀─────│ ControlSvc  │
└──────┬────────┘      └──────┬───────┘      └──────┬──────┘
       │                      │                     │
       │                      ▼                     │
       │               ┌─────────────┐              │
       └──────────────▶│ ReconcileSvc│◀─────────────┘
                       └──────┬──────┘
                              │
                              ▼
                        ┌───────────┐
                        │ TraceSvc  │
                        └─────┬─────┘
                              ▼
                       fixture_target
```

## Repository Map

```text
bigip-icontrol-rce-research/
├── proto/               # Protobuf contract definitions — source of truth for all service APIs
├── generated/           # Auto-generated gRPC stubs — do not edit, committed for reproducibility
├── services/            # gRPC service implementations
│   ├── ingestion/       # CVE data ingest, deduplication, fingerprinting
│   ├── trace/           # Exploit trace capture, fixture target, replay
│   ├── control/         # ASVS control registry, OWASP crosswalk
│   ├── evidence/        # Evidence generation, SHA-256 ledger, lineage
│   └── reconciliation/  # Cross-service conflict detection and resolution
├── sdlc/                # SDLC phase artefacts — requirements through release
│   ├── requirements/    # Threat model, ASVS requirements mapping
│   ├── design/          # Architecture, control design decisions
│   ├── implementation/  # Changelog, implementation notes
│   ├── verification/    # Test plan, ASVS test matrix CSV
│   └── release/         # Release gate checklist
├── tests/               # All test code — unit, integration, ASVS-tagged
│   ├── unit/            # Per-module unit tests, no network
│   ├── integration/     # Full pipeline integration harness
│   ├── fixtures/        # Serialised protobuf test vectors
│   └── asvs/            # ASVS control verification tests, tagged by ID
├── scripts/             # Operational scripts — not part of service layer
├── docs/                # Extended documentation not in README
├── .github/             # CI workflow definitions
├── evidence_gap_register.csv
├── owasp_control_matrix.csv
├── docker-compose.yml
├── Makefile
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── package.json
```

## Common Workflows

- `make verify-tools`: verify prerequisite toolchain.
- `make proto`: compile protobuf contracts to Python stubs.
- `make services-detach`: start full gRPC stack.
- `make asvs`: run ASVS tests and export the matrix.
- `make release`: enforce release gate criteria.

## Extended Docs

- [Technical CVE analysis](docs/cve_technical_analysis.md)
- [gRPC contracts](docs/grpc_service_contracts.md)
- [ASVS rationale](docs/asvs_rationale.md)
- [Dedup/reconciliation design](docs/dedup_reconciliation_design.md)
- [Fixture design](docs/fixture_design.md)
