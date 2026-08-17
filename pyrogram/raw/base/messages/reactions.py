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
    Reactions = Any
else:
    Reactions = Union[raw.types.messages.Reactions, raw.types.messages.ReactionsNotModified]

_doc = """A set of message reactions

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            messages.Reactions
            messages.ReactionsNotModified

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetTopReactions
            messages.GetRecentReactions
            messages.GetDefaultTagReactions"""
try:
    _t = type(Reactions)
    _module = getattr(_t, "__module__", "")
    _name = getattr(_t, "__name__", "")
    # typing.Union (and UnionType) can have a read-only __doc__ on newer Python versions
    if _module != "typing" and not (_module == "types" and _name == "UnionType"):
        Reactions.__doc__ = _doc
except (AttributeError, TypeError):
    pass
