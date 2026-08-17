#!/usr/bin/env python3
"""Mechanical typing cleanup for legacy Pyrogram annotations.

This only changes annotations; runtime control flow and MTProto behavior are untouched.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PKG = ROOT / "pyrogram"
OPTIONAL_PREFIXES = ("typing.Optional[", "Optional[")

# Matches common legacy signatures such as `foo: str = None`.
# Horizontal whitespace is intentional: never allow a match to cross lines.
NONE_DEFAULT = re.compile(
    r'(?P<name>\b[A-Za-z_]\w*)[ \t]*:[ \t]*(?P<type>[^,\n=]+?)[ \t]*=[ \t]*None(?P<tail>[ \t]*[,\)])'
)

# Restrict self annotation to text between a function declaration and its
# closing parameter parenthesis. This avoids touching ordinary calls such as
# Session(self, ...).
MIXIN_SELF = re.compile(
    r'(?P<prefix>\b(?:async[ \t]+)?def[ \t]+\w+[ \t]*\([^)]*?)'
    r'(?<![A-Za-z0-9_])self(?![A-Za-z0-9_]|[ \t]*:)'
)


def matching_bracket(text: str, open_index: int) -> int | None:
    """Return the closing bracket matching ``text[open_index] == '['``."""
    depth = 0
    quote: str | None = None
    escaped = False

    for index in range(open_index, len(text)):
        char = text[index]

        if quote is not None:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            continue

        if char in {"'", '"'}:
            quote = char
        elif char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
            if depth == 0:
                return index

    return None


def optional_at(text: str, start: int) -> tuple[int, int] | None:
    """Return ``(open_bracket, end)`` when an Optional wrapper starts here."""
    for prefix in OPTIONAL_PREFIXES:
        if text.startswith(prefix, start):
            open_index = start + len(prefix) - 1
            close_index = matching_bracket(text, open_index)
            if close_index is not None:
                return open_index, close_index
    return None


def unwrap_full_optional(expression: str) -> str | None:
    """Return the inner expression when the whole expression is Optional[T]."""
    stripped = expression.strip()
    match = optional_at(stripped, 0)
    if match is None:
        return None

    open_index, close_index = match
    if close_index != len(stripped) - 1:
        return None
    return stripped[open_index + 1:close_index].strip()


def collapse_nested_optionals(text: str) -> str:
    """Canonicalize Optional wrappers and collapse Optional[Optional[T]].

    Both the imported spelling ``Optional[T]`` and ``typing.Optional[T]`` are
    accepted as input. Output uses ``typing.Optional[T]`` so repeated runs are
    deterministic and idempotent.
    """
    pieces: list[str] = []
    cursor = 0

    while cursor < len(text):
        starts = [
            position
            for prefix in OPTIONAL_PREFIXES
            if (position := text.find(prefix, cursor)) >= 0
        ]
        if not starts:
            pieces.append(text[cursor:])
            break

        start = min(starts)
        pieces.append(text[cursor:start])
        match = optional_at(text, start)
        if match is None:
            pieces.append(text[start:])
            break

        open_index, close_index = match
        inner = collapse_nested_optionals(text[open_index + 1:close_index].strip())

        # Collapse only when the complete inner expression is another Optional.
        # Nested optionals inside containers remain semantically distinct, e.g.
        # Optional[List[Optional[int]]].
        while True:
            unwrapped = unwrap_full_optional(inner)
            if unwrapped is None:
                break
            inner = collapse_nested_optionals(unwrapped)

        pieces.append(f"typing.Optional[{inner}]")
        cursor = close_index + 1

    return "".join(pieces)


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
    updated = collapse_nested_optionals(source)

    def repl(match: re.Match[str]) -> str:
        annotation = collapse_nested_optionals(match.group("type").strip())
        if annotation in {"Any", "typing.Any"} or unwrap_full_optional(annotation) is not None:
            return f'{match.group("name")}: {annotation} = None{match.group("tail")}'
        return f'{match.group("name")}: typing.Optional[{annotation}] = None{match.group("tail")}'

    updated = NONE_DEFAULT.sub(repl, updated)
    updated = collapse_nested_optionals(updated)

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
