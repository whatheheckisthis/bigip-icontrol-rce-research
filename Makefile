.PHONY: proto proto-js services services-detach services-down test test-coverage asvs audit lint evidence-export readme verify-tools release clean

PYTHON ?= python
PROTO_DIR := proto
GENERATED_DIR := generated

proto:
	mkdir -p $(GENERATED_DIR)
	$(PYTHON) -m grpc_tools.protoc -I $(PROTO_DIR) --python_out=$(GENERATED_DIR) --grpc_python_out=$(GENERATED_DIR) $(PROTO_DIR)/*.proto

proto-js:
	@echo "Optional JS/TS proto generation entrypoint; install npm devDependencies then run npm run proto:gen"

services:
	docker-compose up

services-detach:
	docker-compose up -d

services-down:
	docker-compose down

test:
	pytest tests/unit tests/integration --cov=services --cov-report=term

test-coverage:
	pytest tests/unit tests/integration tests/asvs --cov=services --cov-report=term --cov-report=html

asvs:
	pytest -m asvs tests/asvs --junitxml=sdlc/verification/asvs-results.xml

audit:
	pip-audit -r requirements.txt

lint:
	ruff check services tests scripts && mypy services scripts

evidence-export:
	$(PYTHON) scripts/export_evidence.py

readme:
	$(PYTHON) scripts/generate_readme_tables.py

verify-tools:
	@python3 -c "import sys; assert sys.version_info >= (3, 12), 'Python >= 3.12 required'"
	@docker --version >/dev/null || (echo "Docker is required" && exit 1)
	@docker-compose version >/dev/null || (echo "docker-compose v2+ is required" && exit 1)
	@protoc --version >/dev/null || (echo "protoc is required" && exit 1)

release: asvs audit
	@test -z "$$(git status --porcelain)" || (echo "working tree must be clean for release" && exit 1)
	@! rg -n '^CRITICAL,' evidence_gap_register.csv >/dev/null || (echo "critical evidence gaps block release" && exit 1)

clean:
	docker-compose down -v || true
	rm -rf $(GENERATED_DIR) htmlcov .pytest_cache
	find . -name "*_pb2.py" -delete
	find . -name "*_pb2_grpc.py" -delete
