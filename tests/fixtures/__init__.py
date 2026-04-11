import json
from pathlib import Path

def load_vectors() -> dict:
    data = json.loads(Path(__file__).with_name("exploit_trace_vectors.json").read_text())
    return {item["trace_id"]: item for item in data["vectors"]}
