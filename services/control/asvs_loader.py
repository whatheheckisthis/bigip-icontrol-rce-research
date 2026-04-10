from __future__ import annotations

import csv
from pathlib import Path


def load_asvs_manifest(path: str) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))
