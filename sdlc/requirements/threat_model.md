# STRIDE Threat Model — CVE-2021-22986 Fixture Scope

## Scope
Fixture target only (`services/trace/fixture_target.py`), no live F5 devices.

## Threats
- **Spoofing**: token extraction + Basic bypass paths modelled in traces.
- **Tampering**: utilCmdArgs command injection payload mutation.
- **Repudiation**: missing event correlation without evidence ledger.
- **Information Disclosure**: unauthenticated token exposure patterns.
- **Denial of Service**: abusive replay against fixture endpoint.
- **Elevation of Privilege**: command execution through simulated bash endpoint.
