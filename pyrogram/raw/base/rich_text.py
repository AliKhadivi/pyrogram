#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import TYPE_CHECKING, Any, Union
from pyrogram import raw

# Runtime keeps the exact constructor union for compatibility and docs.
# Static analysis treats raw base aliases as dynamic because legacy Pyrogram
# parsers intentionally duck-type constructor-specific fields after runtime
# checks that Pyright cannot reliably infer across generated TL unions.
if TYPE_CHECKING:
    RichText = Any
else:
    RichText = Union[raw.types.TextAnchor, raw.types.TextAutoEmail, raw.types.TextAutoPhone, raw.types.TextAutoUrl, raw.types.TextBankCard, raw.types.TextBold, raw.types.TextBotCommand, raw.types.TextCashtag, raw.types.TextConcat, raw.types.TextCustomEmoji, raw.types.TextDate, raw.types.TextDiff, raw.types.TextEmail, raw.types.TextEmpty, raw.types.TextFixed, raw.types.TextHashtag, raw.types.TextImage, raw.types.TextItalic, raw.types.TextMarked, raw.types.TextMath, raw.types.TextMention, raw.types.TextMentionName, raw.types.TextPhone, raw.types.TextPlain, raw.types.TextSpoiler, raw.types.TextStrike, raw.types.TextSubscript, raw.types.TextSuperscript, raw.types.TextUnderline, raw.types.TextUrl]

_doc = """Rich text

    Constructors:
        This base type has 30 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            TextAnchor
            TextAutoEmail
            TextAutoPhone
            TextAutoUrl
            TextBankCard
            TextBold
            TextBotCommand
            TextCashtag
            TextConcat
            TextCustomEmoji
            TextDate
            TextDiff
            TextEmail
            TextEmpty
            TextFixed
            TextHashtag
            TextImage
            TextItalic
            TextMarked
            TextMath
            TextMention
            TextMentionName
            TextPhone
            TextPlain
            TextSpoiler
            TextStrike
            TextSubscript
            TextSuperscript
            TextUnderline
            TextUrl"""
try:
    _t = type(RichText)
    _module = getattr(_t, "__module__", "")
    _name = getattr(_t, "__name__", "")
    # typing.Union (and UnionType) can have a read-only __doc__ on newer Python versions
    if _module != "typing" and not (_module == "types" and _name == "UnionType"):
        RichText.__doc__ = _doc
except (AttributeError, TypeError):
    pass
