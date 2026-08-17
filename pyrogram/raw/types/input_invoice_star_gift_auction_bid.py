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


class InputInvoiceStarGiftAuctionBid(TLObject):
    """Used to place a bid in a collectible gift auction ».

    Constructor of :obj:`~pyrogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``228``
        - ID: ``1ECAFA10``

    Parameters:
        gift_id (``int`` ``64-bit``):
            Identifier of the gift, from starGift.id

        bid_amount (``int`` ``64-bit``):
            Total amount of the bid in Telegram Stars.

        hide_name (``bool``, *optional*):
            If set, your name will be hidden if the destination peer decides to display the gift on their profile (they will still see that you sent the gift).    Must not be set when updating an existing bid, as the value cannot be changed for existing bids.

        update_bid (``bool``, *optional*):
            Must be set when increasing an already existing bid.

        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Identifier of the user or channel (only if channelFull.stargifts_available is set) that will receive the gift.

        message (:obj:`TextWithEntities <pyrogram.raw.base.TextWithEntities>`, *optional*):
            Optional message that will be attached with the gift if we end up winning this round: the maximum length for this field is specified in the stargifts_message_length_max client configuration value ».    Must not be set when updating an existing bid, as the value cannot be changed for existing bids.

    """

    __slots__: List[str] = ["gift_id", "bid_amount", "hide_name", "update_bid", "peer", "message"]

    ID = 0x1ecafa10
    QUALNAME = "types.InputInvoiceStarGiftAuctionBid"

    def __init__(self, *, gift_id: int, bid_amount: int, hide_name: Optional[bool] = None, update_bid: Optional[bool] = None, peer: "raw.base.InputPeer" = None, message: "raw.base.TextWithEntities" = None) -> None:
        self.gift_id = gift_id  # long
        self.bid_amount = bid_amount  # long
        self.hide_name = hide_name  # flags.0?true
        self.update_bid = update_bid  # flags.2?true
        self.peer = peer  # flags.3?InputPeer
        self.message = message  # flags.1?TextWithEntities

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoiceStarGiftAuctionBid":
        
        flags = Int.read(b)
        
        hide_name = True if flags & (1 << 0) else False
        update_bid = True if flags & (1 << 2) else False
        peer = TLObject.read(b) if flags & (1 << 3) else None
        
        gift_id = Long.read(b)
        
        bid_amount = Long.read(b)
        
        message = TLObject.read(b) if flags & (1 << 1) else None
        
        return InputInvoiceStarGiftAuctionBid(gift_id=gift_id, bid_amount=bid_amount, hide_name=hide_name, update_bid=update_bid, peer=peer, message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.hide_name else 0
        flags |= (1 << 2) if self.update_bid else 0
        flags |= (1 << 3) if self.peer is not None else 0
        flags |= (1 << 1) if self.message is not None else 0
        b.write(Int(flags))
        
        if self.peer is not None:
            b.write(self.peer.write())
        
        b.write(Long(self.gift_id))
        
        b.write(Long(self.bid_amount))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
