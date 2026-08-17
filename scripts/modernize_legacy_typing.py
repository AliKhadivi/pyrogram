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

# Restrict self annotation to text between a function declaration and its
# closing parameter parenthesis. This avoids touching ordinary calls such as
# Session(self, ...).
MIXIN_SELF = re.compile(
    r'(?P<prefix>\b(?:async[ \t]+)?def[ \t]+\w+[ \t]*\([^)]*?)'
    r'(?<![A-Za-z0-9_])self(?![A-Za-z0-9_]|[ \t]*:)'
)


def add_typing_import(source: str) -> str:
    if "import typing\n" in source:
        return source

    lines = source.splitlines(keepends=True)
    insert_at = 0

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

    posix = path.as_posix()

    # Client methods are composed from many independent mixin classes. Inside
    # those mixins, `self` is the final Client instance at runtime, but static
    # analyzers otherwise see only the narrow mixin class. Model it as dynamic
    # rather than emitting hundreds of false missing-member errors.
    if "/pyrogram/methods/" in posix:
        updated = updated.replace('self: "pyrogram.Client"', 'self: typing.Any')
        updated = updated.replace("self: 'pyrogram.Client'", 'self: typing.Any')
        updated = MIXIN_SELF.sub(r'\g<prefix>self: typing.Any', updated)

    # Pyrogram Object instances may be deserialized before they are rebound to
    # a Client. Bound helper methods intentionally assume a client exists once
    # invoked. Keep that runtime behavior but avoid propagating Optional[Client]
    # through every high-level type.
    if posix.endswith("/pyrogram/types/object.py"):
        updated = updated.replace("self._client = client", "self._client: typing.Any = client")

    if updated != source:
        if "typing." in updated:
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
