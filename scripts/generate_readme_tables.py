from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OWASP_CSV = ROOT / "owasp_control_matrix.csv"
SDLC_CSV = ROOT / "sdlc_artifact_map.csv"


def table_from_csv(path: Path, headers: list[str], key_map: dict[str, str]) -> str:
    rows = list(csv.DictReader(path.read_text(encoding="utf-8").splitlines()))
    lines = [
        "| " + " | ".join(headers) + " |",
        "|" + "|".join(["---"] * len(headers)) + "|",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row[key_map[h]] for h in headers) + " |")
    return "\n".join(lines)


def replace_block(content: str, start: str, end: str, body: str) -> str:
    before, remainder = content.split(start, 1)
    _, after = remainder.split(end, 1)
    return f"{before}{start}\n{body}\n{end}{after}"


def asvs_pass_rate() -> str:
    matrix = ROOT / "sdlc/verification/asvs_test_matrix.csv"
    if not matrix.exists():
        return "n/a"
    rows = list(csv.DictReader(matrix.read_text(encoding="utf-8").splitlines()))
    if not rows:
        return "0%"
    passed = sum(1 for r in rows if r.get("status", "").strip().lower() == "pass")
    return f"{round((passed / len(rows)) * 100)}%"


def main() -> None:
    content = README.read_text(encoding="utf-8")

    owasp_rows = list(csv.DictReader(OWASP_CSV.read_text(encoding="utf-8").splitlines()))
    owasp_count = len(owasp_rows)
    pass_rate = asvs_pass_rate()

    owasp_table = table_from_csv(
        OWASP_CSV,
        ["OWASP Category", "ASVS Control ID", "Implementation", "Test Coverage", "Status"],
        {
            "OWASP Category": "owasp_title",
            "ASVS Control ID": "asvs_control",
            "Implementation": "service_owner",
            "Test Coverage": "asvs_control",
            "Status": "implementation_status",
        },
    )

    sdlc_table = table_from_csv(
        SDLC_CSV,
        ["Phase", "Artefact", "Path", "Status"],
        {"Phase": "phase", "Artefact": "artefact", "Path": "path", "Status": "status"},
    )

    content = replace_block(content, "<!-- OWASP_TABLE_START -->", "<!-- OWASP_TABLE_END -->", owasp_table)
    content = replace_block(content, "<!-- SDLC_TABLE_START -->", "<!-- SDLC_TABLE_END -->", sdlc_table)

    content = re.sub(
        r"!\[ASVS controls .*?\]\(https://img\.shields\.io/badge/ASVS%20controls-.*?-6f42c1\)",
        f"![ASVS controls {owasp_count}](https://img.shields.io/badge/ASVS%20controls-{owasp_count}-6f42c1)",
        content,
    )
    content = re.sub(
        r"!\[ASVS pass rate .*?\]\(https://img\.shields\.io/badge/test%20pass-.*?-brightgreen\)",
        f"![ASVS pass rate {pass_rate}](https://img.shields.io/badge/test%20pass-{pass_rate}-brightgreen)",
        content,
    )

    README.write_text(content, encoding="utf-8")
    print("README tables regenerated")


if __name__ == "__main__":
    main()
