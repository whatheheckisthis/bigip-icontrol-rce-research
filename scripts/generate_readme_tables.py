# ============================================================
# Repository : bigip-icontrol-rce-research
# Path       : scripts/generate_readme_tables.py
# Purpose    : Regenerates README OWASP and SDLC table sections from CSV source files
# Layer      : sdlc
# SDLC Phase : implementation
# ASVS Ref   : V15.1
# OWASP Ref  : A04
# Modified   : 2026-04-10
# ============================================================
from __future__ import annotations

import argparse
import csv
from pathlib import Path


def _load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8") as handle:
        lines = [line for line in handle if not line.startswith("#") and line.strip()]
    return list(csv.DictReader(lines))


def _markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    head = "| " + " | ".join(headers) + " |"
    sep = "|" + "|".join(["---"] * len(headers)) + "|"
    body = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([head, sep, *body])


def _replace_section(text: str, start: str, end: str, replacement: str) -> str:
    start_idx = text.index(start) + len(start)
    end_idx = text.index(end)
    return text[:start_idx] + "\n\n" + replacement + "\n\n" + text[end_idx:]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate README tables from CSV sources")
    parser.add_argument("--control-matrix", required=True, help="Input OWASP control matrix CSV")
    parser.add_argument("--gap-register", required=True, help="Input evidence gap register CSV")
    parser.add_argument("--output", required=True, help="README path to write")
    parser.add_argument(
        "--artifact-map",
        default="sdlc_artifact_map.csv",
        help="Input SDLC artefact map CSV (defaults to sdlc_artifact_map.csv)",
    )
    args = parser.parse_args()

    readme_path = Path(args.output)
    readme_text = readme_path.read_text(encoding="utf-8")

    control_rows = _load_csv(Path(args.control_matrix))
    owasp_md = _markdown_table(
        ["OWASP Category", "ASVS Control ID", "Implementation", "Test Coverage", "Status"],
        [
            [
                row["owasp_category"],
                row["asvs_control_id"],
                row["implementation_location"],
                row["test_coverage"],
                row["implementation_status"],
            ]
            for row in control_rows
        ],
    )

    artifact_rows = _load_csv(Path(args.artifact_map))
    sdlc_md = _markdown_table(
        ["Phase", "Artefact", "Path", "Status"],
        [
            [
                row["phase"].title(),
                row["artifact_path"].split("/")[-1],
                row["artifact_path"],
                "Generated" if row["maintenance_mode"] == "generated" else "Maintained",
            ]
            for row in artifact_rows
        ],
    )

    updated = _replace_section(readme_text, "<!-- BEGIN:OWASP_TABLE -->", "<!-- END:OWASP_TABLE -->", owasp_md)
    updated = _replace_section(updated, "<!-- BEGIN:SDLC_TABLE -->", "<!-- END:SDLC_TABLE -->", sdlc_md)
    readme_path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
