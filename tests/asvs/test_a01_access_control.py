import pytest
from tests.fixtures import load_vectors

@pytest.mark.asvs("V4.1.1")
def test_interceptor_layer_decision(trace_client):
    vectors = load_vectors()
    for vid in ["vector-001-token-extraction", "vector-002-basic-bypass", "vector-003-id-recon"]:
        assert trace_client.CaptureTrace(vectors[vid]).trace_id
    with pytest.raises(trace_client.InvalidArgumentError):
        trace_client.CaptureTrace(vectors["vector-004-ssrf-rejection"])
    assert trace_client.interceptor_invoked is True
