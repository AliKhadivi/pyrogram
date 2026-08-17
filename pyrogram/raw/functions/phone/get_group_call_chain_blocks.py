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


class GetGroupCallChainBlocks(TLObject["raw.base.Updates"]):
    """Fetch blocks from a conference call subchain »; handle the returned updateGroupCallChainBlocks as specified here ».


    Details:
        - Layer: ``228``
        - ID: ``EE9F88A6``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Conference whose subchain blocks should be fetched

        sub_chain_id (``int`` ``32-bit``):
            0 for the main state blockchain, 1 for the call verification subchain

        offset (``int`` ``32-bit``):
            Fetch blocks starting from this height; pass -1 to fetch the latest block

        limit (``int`` ``32-bit``):
            Maximum number of blocks to return in this call, see pagination, max 100.

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "sub_chain_id", "offset", "limit"]

    ID = 0xee9f88a6
    QUALNAME = "functions.phone.GetGroupCallChainBlocks"

    def __init__(self, *, call: "raw.base.InputGroupCall", sub_chain_id: int, offset: int, limit: int) -> None:
        self.call = call  # InputGroupCall
        self.sub_chain_id = sub_chain_id  # int
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetGroupCallChainBlocks":
        # No flags
        
        call = TLObject.read(b)
        
        sub_chain_id = Int.read(b)
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetGroupCallChainBlocks(call=call, sub_chain_id=sub_chain_id, offset=offset, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Int(self.sub_chain_id))
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
