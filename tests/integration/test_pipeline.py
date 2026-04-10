from services.ingestion.server import IngestionService
from services.trace.server import ExploitTraceService


def test_ingest_then_capture_pipeline() -> None:
    ingestion = IngestionService()
    created, _ = ingestion.ingest({"cve_id": "CVE-2021-22986", "fingerprint": "abc"})
    assert created

    trace = ExploitTraceService()
    trace_id = trace.capture_trace({"trace_id": "trace-1", "target_fixture_url": "http://localhost:8080"})
    assert trace_id == "trace-1"
