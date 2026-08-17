#!/usr/bin/env python3
"""Validate statically referenced pyrogram.raw symbols against generated Layer API.

Run after generating the raw API. This intentionally checks structural API drift
(e.g. raw.types.SomeRemovedConstructor) without trying to type-check all of
Pyrogram's legacy dynamic/mixin patterns.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path
from typing import Iterable

from pyrogram import raw

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "pyrogram"
EXCLUDED_PARTS = {"raw", "__pycache__"}
RAW_ROOTS = {"types", "functions", "base"}


def iter_python_files() -> Iterable[Path]:
    for path in PACKAGE.rglob("*.py"):
        relative = path.relative_to(PACKAGE)
        if relative.parts and relative.parts[0] in EXCLUDED_PARTS:
            continue
        yield path


def raw_chain(node: ast.AST) -> list[str] | None:
    parts: list[str] = []
    current = node

    while isinstance(current, ast.Attribute):
        parts.append(current.attr)
        current = current.value

    if not isinstance(current, ast.Name) or current.id != "raw":
        return None

    parts.reverse()
    if not parts or parts[0] not in RAW_ROOTS:
        return None

    return parts


def resolve(parts: list[str]) -> tuple[bool, str]:
    current = raw
    resolved = ["raw"]

    for part in parts:
        if not hasattr(current, part):
            return False, ".".join(resolved + [part])
        current = getattr(current, part)
        resolved.append(part)

    return True, ".".join(resolved)


def main() -> int:
    failures: set[tuple[str, int, str]] = set()

    for path in iter_python_files():
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            failures.add((str(path.relative_to(ROOT)), exc.lineno or 0, f"syntax error: {exc.msg}"))
            continue

        for node in ast.walk(tree):
            chain = raw_chain(node)
            if chain is None:
                continue

            ok, name = resolve(chain)
            if not ok:
                failures.add((str(path.relative_to(ROOT)), getattr(node, "lineno", 0), name))

    if failures:
        print("Invalid raw API references:")
        for filename, line, name in sorted(failures):
            print(f"  {filename}:{line}: {name}")
        print(f"\n{len(failures)} invalid raw API reference(s).")
        return 1

    print("All statically referenced raw API symbols exist in the generated layer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
