import pytest
from tests.fixtures import load_vectors

@pytest.mark.asvs("V2.1.1")
def test_auth_paths_and_evidence(trace_client, evidence_client):
    vectors = load_vectors()
    v1 = vectors["vector-001-token-extraction"]
    r1 = trace_client.CaptureTrace(v1)
    t1 = trace_client.GetTrace(r1.trace_id)
    assert t1.token_extracted is True
    assert v1["auth_path"] == "A"

    v2 = vectors["vector-002-basic-bypass"]
    assert v2["request_headers"]["X-F5-Auth-Token"] == ""
    assert v2["request_headers"]["Authorization"].startswith("Basic ")
    r2 = trace_client.CaptureTrace(v2)
    assert evidence_client.has_trace(r1.trace_id)
    assert evidence_client.has_trace(r2.trace_id)
