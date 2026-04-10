from pathlib import Path


def main() -> None:
    out = Path("sdlc/verification/evidence_ledger_export.json")
    out.write_text('{"status":"placeholder-export"}\n', encoding="utf-8")
    print(f"exported {out}")


if __name__ == "__main__":
    main()
