.PHONY: proto services test asvs audit evidence-export lint clean

proto:
	python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. proto/*.proto

services:
	docker-compose up -d

test:
	pytest tests/unit tests/integration

asvs:
	pytest -m asvs tests/asvs --junitxml=sdlc/verification/asvs-results.xml

audit:
	pip-audit

evidence-export:
	python scripts/export_evidence.py

lint:
	ruff check services tests && mypy services

clean:
	docker-compose down -v || true
	find . -name "*_pb2.py" -delete
	find . -name "*_pb2_grpc.py" -delete
