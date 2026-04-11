from dataclasses import dataclass


@dataclass
class ManualResolutionRequired(Exception):
    conflict_id: str


def resolve_latest_wins(a: dict, b: dict, conflicts: dict) -> dict:
    newer = a if a.get("ingestion_timestamp", 0) >= b.get("ingestion_timestamp", 0) else b
    resolved = dict(a)
    for field in conflicts:
        resolved[field] = newer.get(field)
    return resolved


def resolve_source_priority(a, b, conflicts, priority_order: list[str]):
    rank = {name: idx for idx, name in enumerate(priority_order)}
    source_a = a.get("source_uri", "third-party")
    source_b = b.get("source_uri", "third-party")
    winner = a if rank.get(source_a, 999) <= rank.get(source_b, 999) else b
    resolved = dict(a)
    for field in conflicts:
        resolved[field] = winner.get(field)
    return resolved


def resolve_manual(conflict_id: str) -> None:
    with open("evidence_gap_register.csv", "a", encoding="utf-8") as handle:
        handle.write(f"\n{conflict_id},HIGH,OPEN,manual-resolution-required,reconciliation-team,2026-05-01")
    raise ManualResolutionRequired(conflict_id)
