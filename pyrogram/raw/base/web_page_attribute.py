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

WebPageAttribute = Union[raw.types.WebPageAttributeAiComposeTone, raw.types.WebPageAttributeStarGiftAuction, raw.types.WebPageAttributeStarGiftCollection, raw.types.WebPageAttributeStickerSet, raw.types.WebPageAttributeStory, raw.types.WebPageAttributeTheme, raw.types.WebPageAttributeUniqueStarGift]
_doc = """Webpage attributes

    Constructors:
        This base type has 7 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            WebPageAttributeAiComposeTone
            WebPageAttributeStarGiftAuction
            WebPageAttributeStarGiftCollection
            WebPageAttributeStickerSet
            WebPageAttributeStory
            WebPageAttributeTheme
            WebPageAttributeUniqueStarGift"""
try:
    _t = type(WebPageAttribute)
    # typing.Union (and UnionType) can have a read-only __doc__ on newer Python versions
    if _t.__module__ != "typing" and not (_t.__module__ == "types" and _t.__name__ == "UnionType"):
        WebPageAttribute.__doc__ = _doc
except (AttributeError, TypeError):
    pass
