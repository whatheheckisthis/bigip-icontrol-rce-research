# Architecture

```mermaid
flowchart LR
  Ingestion --> Reconciliation
  Trace --> Evidence
  Control --> Evidence
  Reconciliation --> Evidence
```

Threat model outputs from `sdlc/requirements/threat_model.md` are explicit design inputs.
