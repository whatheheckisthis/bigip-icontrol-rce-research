# Repository : bigip-icontrol-rce-research
# Path       : Makefile
# Purpose    : Orchestrates proto generation, service lifecycle, tests, and release gates.
# Layer      : config
# SDLC Phase : release
# ASVS Ref   : N/A
# OWASP Ref  : N/A
# Modified   : 2026-04-11
PYTHON    := python3.12
PROTO_DIR := proto
GEN_DIR   := generated
COMPOSE   := docker compose

.PHONY: proto services services-detach services-down test test-coverage         asvs audit lint evidence-export release clean verify-tools help

proto:
	@mkdir -p $(GEN_DIR)
	$(PYTHON) -m grpc_tools.protoc 		--proto_path=$(PROTO_DIR) 		--python_out=$(GEN_DIR) 		--grpc_python_out=$(GEN_DIR) 		$(PROTO_DIR)/*.proto
	@touch $(GEN_DIR)/__init__.py

verify-tools:
	@bash scripts/verify_tools.sh

services: proto
	$(COMPOSE) up --build

services-detach: proto
	$(COMPOSE) up --build -d

services-down:
	$(COMPOSE) down

test:
	$(PYTHON) -m pytest tests/unit tests/integration 		--cov=services --cov-report=term-missing -v

test-coverage:
	$(PYTHON) -m pytest tests/ --cov=services --cov-report=html -v

asvs:
	$(PYTHON) -m pytest -m asvs -v --tb=short 		--json-report --json-report-file=/tmp/asvs_results.json
	$(PYTHON) scripts/export_asvs_matrix.py 		--input /tmp/asvs_results.json 		--output sdlc/verification/asvs_test_matrix.csv

audit:
	pip-audit -r requirements.txt --fail-on-severity high

lint:
	ruff check services/ tests/ scripts/
	mypy services/

evidence-export:
	$(PYTHON) scripts/export_evidence.py 		--output sdlc/verification/evidence_ledger_export.json

release: lint audit asvs
	$(PYTHON) scripts/release_gate.py 		--gap-register evidence_gap_register.csv 		--asvs-matrix sdlc/verification/asvs_test_matrix.csv

clean:
	$(COMPOSE) down --volumes --remove-orphans
	rm -rf $(GEN_DIR) htmlcov/ .coverage .pytest_cache
	find . -name "*.pyc" -delete

help:
	@grep -E '^[a-zA-Z_-]+:' Makefile | 		awk -F: '{print $$1}' | sort
