import pytest
from tests.fixtures import load_vectors

@pytest.mark.asvs("V5.2.3")
class TestInjectionDetection:
    """Injection patterns are captured and never executed."""

    def test_utilcmdargs_extracted_as_field_not_executed(self, trace_client):
        vector = load_vectors()["vector-002-basic-bypass"]
        response = trace_client.CaptureTrace(vector)
        trace = trace_client.GetTrace(response.trace_id)
        assert trace.command_injected == "whoami"
        assert trace.command_result == "synthetic-output"
        assert trace.command_result != get_real_whoami()

    def test_injection_pattern_negative_vector_id(self, trace_client):
        vector = load_vectors()["vector-003-id-recon"]
        response = trace_client.CaptureTrace(vector)
        trace = trace_client.GetTrace(response.trace_id)
        assert trace.command_injected == "id"
        assert trace.command_result == "synthetic-output"

    def test_empty_utilcmdargs_produces_empty_command_injected(self, trace_client):
        vector = load_vectors()["vector-001-token-extraction"]
        response = trace_client.CaptureTrace(vector)
        trace = trace_client.GetTrace(response.trace_id)
        assert trace.command_injected == ""

def get_real_whoami():
    import getpass
    return getpass.getuser()
