#!/usr/bin/env python3
"""Normalize generated Raw API typing without changing wire behavior."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "pyrogram" / "raw"
OPTIONAL_RAW = re.compile(r'(?P<type>"raw\.base\.[A-Za-z0-9_.]+") = None')


def normalize(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    updated = OPTIONAL_RAW.sub(r'Optional[\g<type>] = None', source)
    updated = updated.replace('TLObject["raw.base.Bool"]', 'TLObject[bool]')
    updated = updated.replace('"List[raw.base.Bool]"', '"List[bool]"')

    if "bytes: bytes" in updated:
        updated = updated.replace("bytes: bytes", "bytes: builtins.bytes")
        if "import builtins\n" not in updated:
            marker = "from io import BytesIO\n"
            updated = updated.replace(marker, marker + "import builtins\n", 1)

    if updated != source:
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = sum(normalize(path) for path in RAW.rglob("*.py"))
    print(f"Normalized generated typing in {changed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
