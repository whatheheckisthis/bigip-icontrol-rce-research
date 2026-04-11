# Release Checklist

- [ ] make lint exits 0
- [ ] make audit exits 0 (no CVSS >= 7.0 findings)
- [ ] npm run audit:deps exits 0
- [ ] npm run audit:licenses exits 0
- [ ] make asvs exits 0 (all ten ASVS modules passing)
- [ ] sdlc/verification/asvs_test_matrix.csv updated within last 24h
- [ ] evidence_gap_register.csv contains zero CRITICAL items
- [ ] generated/ stubs are consistent with proto/ definitions (proto:check passes)
- [ ] No hardcoded credentials anywhere in tree (grep rule)
- [ ] fixture_target.py host parameter == "127.0.0.1" (grep assert)
- [ ] docker-compose.yml fixture_target port binding contains "127.0.0.1"
