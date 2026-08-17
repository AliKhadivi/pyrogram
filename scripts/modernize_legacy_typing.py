#!/usr/bin/env python3
"""Mechanical typing cleanup for legacy Pyrogram annotations.

This only changes annotations; runtime control flow and MTProto behavior are untouched.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "pyrogram"

# Matches common legacy signatures such as `foo: str = None`.
# Horizontal whitespace is intentional: never allow a match to cross lines.
NONE_DEFAULT = re.compile(
    r'(?P<name>\b[A-Za-z_]\w*)[ \t]*:[ \t]*(?P<type>(?!typing\.Optional\[|Optional\[)[^,\n=]+?)[ \t]*=[ \t]*None(?P<tail>[ \t]*[,\)])'
)


def add_typing_import(source: str) -> str:
    if "import typing\n" in source:
        return source

    lines = source.splitlines(keepends=True)
    insert_at = 0

    # Keep license/comments and module docstring area intact; insert before
    # the first normal import/from statement.
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("import ") or stripped.startswith("from "):
            insert_at = i
            break
    else:
        return "import typing\n" + source

    lines.insert(insert_at, "import typing\n")
    return "".join(lines)


def normalize(path: Path) -> bool:
    source = path.read_text(encoding="utf-8")
    updated = source

    def repl(match: re.Match[str]) -> str:
        annotation = match.group("type").strip()
        if annotation in {"Any", "typing.Any"}:
            return match.group(0)
        return f'{match.group("name")}: typing.Optional[{annotation}] = None{match.group("tail")}'

    updated = NONE_DEFAULT.sub(repl, updated)

    # Pyrogram method mixins deliberately annotate self as Client even though
    # the containing class is a mixin. Modern Pyright treats that as an
    # invalid self type. Removing only this annotation preserves behavior.
    if "pyrogram/methods/" in path.as_posix():
        updated = updated.replace('self: "pyrogram.Client"', 'self')
        updated = updated.replace("self: 'pyrogram.Client'", 'self')

    if updated != source:
        if "typing.Optional[" in updated:
            updated = add_typing_import(updated)
        path.write_text(updated, encoding="utf-8")
        return True
    return False


def main() -> int:
    changed = 0
    for path in PKG.rglob("*.py"):
        if "raw" in path.relative_to(PKG).parts:
            continue
        if normalize(path):
            changed += 1
    print(f"Modernized legacy typing in {changed} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
