import hashlib
import json


def hash_content(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def hash_record(record_dict: dict) -> str:
    payload = json.dumps(record_dict, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hash_content(payload)


def verify(content: bytes, expected_hash: str) -> bool:
    return hash_content(content) == expected_hash
