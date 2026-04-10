from __future__ import annotations


def choose_source_priority(sources: dict[str, dict]) -> dict:
    order = ["nvd", "vendor advisory", "third-party"]
    for src in order:
        if src in sources:
            return sources[src]
    return next(iter(sources.values()))
