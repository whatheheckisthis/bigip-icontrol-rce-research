<!--
Repository : bigip-icontrol-rce-research
Path       : sdlc/release/release_checklist.md
Purpose    : Defines release quality gates validated by release_gate.py.
Layer      : sdlc
SDLC Phase : release
ASVS Ref   : N/A
OWASP Ref  : N/A
Modified   : 2026-04-11
-->
- [ ] make lint exits 0
- [ ] make audit exits 0
- [ ] npm run audit:deps exits 0
- [ ] npm run audit:licenses exits 0
- [ ] make asvs exits 0
- [ ] asvs_test_matrix.csv updated within last 24h
- [ ] evidence_gap_register.csv has zero CRITICAL+OPEN rows
- [ ] generated/ stubs consistent with proto/ (proto:check passes)
- [ ] No hardcoded credentials in tree
- [ ] fixture_target.py host == "127.0.0.1"
- [ ] docker-compose.yml fixture port binding contains "127.0.0.1:8080"
