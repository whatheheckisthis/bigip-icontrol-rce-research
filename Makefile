# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : Makefile
# Purpose    : Build, test, compose, and release automation entry points
# Layer      : config
# SDLC Phase : implementation
# ASVS Ref   : V14.2, V14.3
# OWASP Ref  : A06, A08
# Modified   : 2026-04-10
# ============================================================

PYTHON      := python3.12
VENV        := .venv
PROTO_DIR   := proto
GEN_DIR     := generated
COMPOSE     := docker compose

.PHONY: all proto proto-js services services-detach services-down \
        test test-coverage asvs audit lint evidence-export readme \
        verify-tools repo-map release clean help

## help: Print this target list
help:
	@grep -E '^## ' Makefile | sed 's/## //'

## verify-tools: Check all prerequisites, exit non-zero if missing
verify-tools:
	@scripts/verify_tools.sh

## proto: Compile all .proto definitions to Python gRPC stubs
proto: verify-tools
	@mkdir -p $(GEN_DIR)
	$(PYTHON) -m grpc_tools.protoc \
		--proto_path=$(PROTO_DIR) \
		--python_out=$(GEN_DIR) \
		--grpc_python_out=$(GEN_DIR) \
		$(PROTO_DIR)/*.proto
	@touch $(GEN_DIR)/__init__.py
	@echo "[proto] Stubs written to $(GEN_DIR)/"

## proto-js: Compile .proto to TypeScript stubs (optional, requires Node)
proto-js:
	@scripts/proto_js.sh

## services: Start all gRPC services via docker-compose
services: proto
	$(COMPOSE) up --build

## services-detach: Start all services detached
services-detach: proto
	$(COMPOSE) up --build -d

## services-down: Stop and remove all service containers
services-down:
	$(COMPOSE) down

## test: Run unit and integration tests with coverage
test:
	$(PYTHON) -m pytest tests/unit tests/integration \
		--cov=services --cov-report=term-missing \
		-v

## test-coverage: Run tests and write htmlcov/
test-coverage:
	$(PYTHON) -m pytest tests/ \
		--cov=services --cov-report=html \
		-v

## asvs: Run ASVS-tagged control verification tests, export matrix CSV
asvs:
	$(PYTHON) -m pytest -m asvs \
		--cov=services \
		-v \
		--tb=short
	$(PYTHON) scripts/export_asvs_matrix.py \
		--output sdlc/verification/asvs_test_matrix.csv

## audit: Run pip-audit, fail on any finding CVSS >= 7.0
audit:
	pip-audit -r requirements.txt \
		--vulnerability-service osv \
		--fail-on-severity high

## lint: Run ruff and mypy across all service modules
lint:
	ruff check services/ tests/ scripts/
	mypy services/ --ignore-missing-imports

## evidence-export: Export full evidence ledger from EvidenceService
evidence-export:
	$(PYTHON) scripts/export_evidence.py \
		--output sdlc/verification/evidence_ledger_export.json

## readme: Regenerate dynamic README sections from CSV sources
readme:
	$(PYTHON) scripts/generate_readme_tables.py \
		--control-matrix owasp_control_matrix.csv \
		--gap-register evidence_gap_register.csv \
		--output README.md

## repo-map: Regenerate annotated directory tree in README
repo-map:
	$(PYTHON) scripts/generate_repo_map.py --output README.md

## release: Full release gate — asvs + audit + gap register + clean tree
release: lint audit asvs
	$(PYTHON) scripts/release_gate.py \
		--gap-register evidence_gap_register.csv \
		--asvs-matrix sdlc/verification/asvs_test_matrix.csv
	@echo "[release] All gates passed."

## clean: Remove containers, generated stubs, coverage artefacts
clean:
	$(COMPOSE) down --volumes --remove-orphans
	rm -rf $(GEN_DIR) htmlcov/ .coverage .pytest_cache __pycache__
	find . -name "*.pyc" -delete
