# Verification Test Plan

## Scope
Testing uses only `tests/fixtures/exploit_trace_vectors.json` fixtures and synthetic services; no live F5 device interaction.

## Entry Criteria
- `make proto` exits 0.
- `npm run build` exits 0.
- `docker compose` stack reports healthy services.

## Exit Criteria
- All unit tests pass.
- All ASVS tests pass.
- `make audit` exits 0.
- `sdlc/verification/asvs_test_matrix.csv` updated with latest results.

## Test Categories
**Unit:** validates parser, deduplication, hashing, and serialisation logic with deterministic fixtures.

**Integration:** validates cross-service flows from ingestion through reconciliation and evidence registration.

**ASVS:** validates control behavior with explicit `@pytest.mark.asvs` mappings and fixture vectors.

## Out of Scope
- Live exploitation of production F5 devices.
- SIEM integration.
- Alert triage workflows.
