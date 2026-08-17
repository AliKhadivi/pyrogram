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

from io import BytesIO
from typing import TYPE_CHECKING, List, Optional, Any

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject

if TYPE_CHECKING:
    from pyrogram import raw

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageActionNewCreatorPending(TLObject):
    """Service message: emitted to a supergroup when the group/channel creator leaves the group », indicating that ownership transfer is pending. The new_creator_id user will become the new owner after 7 days if the old owner does not rejoin.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``228``
        - ID: ``B07ED085``

    Parameters:
        new_creator_id (``int`` ``64-bit``):
            The ID of the user who will become the new owner of the group/channel after 7 days if the old owner does not rejoin.

    """

    __slots__: List[str] = ["new_creator_id"]

    ID = 0xb07ed085
    QUALNAME = "types.MessageActionNewCreatorPending"

    def __init__(self, *, new_creator_id: int) -> None:
        self.new_creator_id = new_creator_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionNewCreatorPending":
        # No flags
        
        new_creator_id = Long.read(b)
        
        return MessageActionNewCreatorPending(new_creator_id=new_creator_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.new_creator_id))
        
        return b.getvalue()
