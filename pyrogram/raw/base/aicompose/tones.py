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

from typing import Union
from pyrogram import raw

Tones = Union[raw.types.aicompose.Tones, raw.types.aicompose.TonesNotModified]
_doc = """The list of saved AI composer tones » of the current user.

    Constructors:
        This base type has 2 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            aicompose.Tones
            aicompose.TonesNotModified

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            aicompose.GetTone
            aicompose.GetTones"""
try:
    _t = type(Tones)
    _module = getattr(_t, "__module__", "")
    _name = getattr(_t, "__name__", "")
    # typing.Union (and UnionType) can have a read-only __doc__ on newer Python versions
    if _module != "typing" and not (_module == "types" and _name == "UnionType"):
        Tones.__doc__ = _doc
except (AttributeError, TypeError):
    pass
