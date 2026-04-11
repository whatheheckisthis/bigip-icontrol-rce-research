<!--
Repository : bigip-icontrol-rce-research
Path       : sdlc/implementation/CHANGELOG.md
Purpose    : Records created project artifacts for the initial release baseline.
Layer      : sdlc
SDLC Phase : implementation
ASVS Ref   : N/A
OWASP Ref  : N/A
Modified   : 2026-04-11
-->
# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
- Trunk-based development workflow — branch naming convention, branch
  protection rules, Conventional Commits enforcement
- `.github/workflows/ci.yml` — branch-lint and commit-lint jobs added;
  npm-audit split from audit job; job dependency chain established
- `.github/CODEOWNERS` — proto/, tests/asvs/, sdlc/, owasp_control_matrix.csv,
  evidence_gap_register.csv, scripts/release_gate.py designated
- `.github/commitlint.config.js` — type and scope enums enforced

## [0.1.0] - 2026-04-11
### Added
- proto contracts in `proto/`.
- generated stubs in `generated/`.
- service implementations in `services/`.
- verification suites in `tests/`.
- SDLC artifacts in `sdlc/`.
- helper automation in `scripts/`.
- root configs (`Makefile`, `pyproject.toml`, dependency manifests).
- CI workflow in `.github/workflows/ci.yml`.
