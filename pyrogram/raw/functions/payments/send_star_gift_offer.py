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


class SendStarGiftOffer(TLObject["raw.base.Updates"]):
    """Send an offer to purchase a collectible gift », see here » for the full flow.


    Details:
        - Layer: ``228``
        - ID: ``8FB86B41``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            Owner of the collectible gift: equal to starGiftUnique.owner_id.

        slug (``str``):
            Identifier of the collectible gift: equal to starGiftUnique.slug.

        price (:obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`):
            Offer price, in stars or TON.

        duration (``int`` ``32-bit``):
            Duration of the offer, in seconds: must be one of 21600, 43200, 86400, 129600, 172800, or 259200; can also be 120 in test mode.

        random_id (``int`` ``64-bit``):
            Random 64-bit identifier used to avoid sending the same offer twice in case of network issues.

        allow_paid_stars (``int`` ``64-bit``, *optional*):
            If the destination peer has paid messages » enabled, specifies the amount of Telegram Stars the sending user has agreed to pay in order to send the offer (in addition to the amount for the offer itself, contained in price).

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "slug", "price", "duration", "random_id", "allow_paid_stars"]

    ID = 0x8fb86b41
    QUALNAME = "functions.payments.SendStarGiftOffer"

    def __init__(self, *, peer: "raw.base.InputPeer", slug: str, price: "raw.base.StarsAmount", duration: int, random_id: int, allow_paid_stars: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.slug = slug  # string
        self.price = price  # StarsAmount
        self.duration = duration  # int
        self.random_id = random_id  # long
        self.allow_paid_stars = allow_paid_stars  # flags.0?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendStarGiftOffer":
        
        flags = Int.read(b)
        
        peer = TLObject.read(b)
        
        slug = String.read(b)
        
        price = TLObject.read(b)
        
        duration = Int.read(b)
        
        random_id = Long.read(b)
        
        allow_paid_stars = Long.read(b) if flags & (1 << 0) else None
        return SendStarGiftOffer(peer=peer, slug=slug, price=price, duration=duration, random_id=random_id, allow_paid_stars=allow_paid_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_paid_stars is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.slug))
        
        b.write(self.price.write())
        
        b.write(Int(self.duration))
        
        b.write(Long(self.random_id))
        
        if self.allow_paid_stars is not None:
            b.write(Long(self.allow_paid_stars))
        
        return b.getvalue()
