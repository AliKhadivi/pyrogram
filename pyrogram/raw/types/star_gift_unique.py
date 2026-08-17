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


class StarGiftUnique(TLObject):
    """Represents a collectible star gift, see here » for more info.

    Constructor of :obj:`~pyrogram.raw.base.StarGift`.

    Details:
        - Layer: ``228``
        - ID: ``85F0A9CD``

    Parameters:
        id (``int`` ``64-bit``):
            Unique identifier of this collectible gift.

        gift_id (``int`` ``64-bit``):
            ID of the regular gift from which this gift was upgraded (all collectible gifts upgraded from the same gift will have the same gift_id, with different attributes).

        title (``str``):
            Collectible title.

        slug (``str``):
            Slug that can be used to create a collectible gift deep link », or elsewhere in the API where a collectible slug is accepted.

        num (``int`` ``32-bit``):
            Unique identifier of this collectible gift among all (already upgraded) collectible gifts of the same type.

        attributes (List of :obj:`StarGiftAttribute <pyrogram.raw.base.StarGiftAttribute>`):
            Collectible attributes

        availability_issued (``int`` ``32-bit``):
            Total number of gifts of the same type that were upgraded to a collectible gift.

        availability_total (``int`` ``32-bit``):
            Total number of gifts of the same type that can be upgraded or were already upgraded to a collectible gift.

        require_premium (``bool``, *optional*):
            This gift can only be bought by users with a Premium subscription.

        resale_ton_only (``bool``, *optional*):
            Whether the gift can be bought only using Grams.

        theme_available (``bool``, *optional*):
            A chat theme associated to this gift is available, see here » for more info on how to use it.

        burned (``bool``, *optional*):
            This gift was already used as an ingredient for crafting another collectible gift ».

        crafted (``bool``, *optional*):
            This collectible gift was obtained by crafting », not by upgrading a regular gift.

        owner_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            The owner of the gift.

        owner_name (``str``, *optional*):
            The name of the owner if neither owner_id nor owner_address are set.

        owner_address (``str``, *optional*):
            For NFTs on the TON blockchain, contains the address of the owner (append it to the ton_blockchain_explorer_url client configuration value » to obtain a link with information about the address).

        gift_address (``str``, *optional*):
            For NFTs on the TON blockchain, contains the address of the NFT (append it to the ton_blockchain_explorer_url client configuration value » to obtain a link with information about the address).

        resell_amount (List of :obj:`StarsAmount <pyrogram.raw.base.StarsAmount>`, *optional*):
            Resale price of the gift.

        released_by (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            This gift was released by the specified peer.

        value_amount (``int`` ``64-bit``, *optional*):
            Estimated price of the gift.

        value_currency (``str``, *optional*):
            Currency for the gift's estimated price.

        value_usd_amount (``int`` ``64-bit``, *optional*):
            Estimated price of the gift in USD cents.

        theme_peer (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            The current chat where the associated chat theme is installed, if any (gift-based themes can only be installed in one chat at a time).

        peer_color (:obj:`PeerColor <pyrogram.raw.base.PeerColor>`, *optional*):
            Can contain a collectible message palette ».

        host_id (:obj:`Peer <pyrogram.raw.base.Peer>`, *optional*):
            If set, the gift is currently hosted on the specified user or channel profile », while ownership remains with the TON wallet in owner_address.

        offer_min_stars (``int`` ``32-bit``, *optional*):
            If set, you can send a purchase offer for this gift »: the minimum offer price is specified in this flag.

        craft_chance_permille (``int`` ``32-bit``, *optional*):
            Success probability, per 1000, contributed by this gift when it is used for crafting ».

    """

    __slots__: List[str] = ["id", "gift_id", "title", "slug", "num", "attributes", "availability_issued", "availability_total", "require_premium", "resale_ton_only", "theme_available", "burned", "crafted", "owner_id", "owner_name", "owner_address", "gift_address", "resell_amount", "released_by", "value_amount", "value_currency", "value_usd_amount", "theme_peer", "peer_color", "host_id", "offer_min_stars", "craft_chance_permille"]

    ID = 0x85f0a9cd
    QUALNAME = "types.StarGiftUnique"

    def __init__(self, *, id: int, gift_id: int, title: str, slug: str, num: int, attributes: List["raw.base.StarGiftAttribute"], availability_issued: int, availability_total: int, require_premium: Optional[bool] = None, resale_ton_only: Optional[bool] = None, theme_available: Optional[bool] = None, burned: Optional[bool] = None, crafted: Optional[bool] = None, owner_id: "raw.base.Peer" = None, owner_name: Optional[str] = None, owner_address: Optional[str] = None, gift_address: Optional[str] = None, resell_amount: Optional[List["raw.base.StarsAmount"]] = None, released_by: "raw.base.Peer" = None, value_amount: Optional[int] = None, value_currency: Optional[str] = None, value_usd_amount: Optional[int] = None, theme_peer: "raw.base.Peer" = None, peer_color: "raw.base.PeerColor" = None, host_id: "raw.base.Peer" = None, offer_min_stars: Optional[int] = None, craft_chance_permille: Optional[int] = None) -> None:
        self.id = id  # long
        self.gift_id = gift_id  # long
        self.title = title  # string
        self.slug = slug  # string
        self.num = num  # int
        self.attributes = attributes  # Vector<StarGiftAttribute>
        self.availability_issued = availability_issued  # int
        self.availability_total = availability_total  # int
        self.require_premium = require_premium  # flags.6?true
        self.resale_ton_only = resale_ton_only  # flags.7?true
        self.theme_available = theme_available  # flags.9?true
        self.burned = burned  # flags.14?true
        self.crafted = crafted  # flags.15?true
        self.owner_id = owner_id  # flags.0?Peer
        self.owner_name = owner_name  # flags.1?string
        self.owner_address = owner_address  # flags.2?string
        self.gift_address = gift_address  # flags.3?string
        self.resell_amount = resell_amount  # flags.4?Vector<StarsAmount>
        self.released_by = released_by  # flags.5?Peer
        self.value_amount = value_amount  # flags.8?long
        self.value_currency = value_currency  # flags.8?string
        self.value_usd_amount = value_usd_amount  # flags.8?long
        self.theme_peer = theme_peer  # flags.10?Peer
        self.peer_color = peer_color  # flags.11?PeerColor
        self.host_id = host_id  # flags.12?Peer
        self.offer_min_stars = offer_min_stars  # flags.13?int
        self.craft_chance_permille = craft_chance_permille  # flags.16?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftUnique":
        
        flags = Int.read(b)
        
        require_premium = True if flags & (1 << 6) else False
        resale_ton_only = True if flags & (1 << 7) else False
        theme_available = True if flags & (1 << 9) else False
        burned = True if flags & (1 << 14) else False
        crafted = True if flags & (1 << 15) else False
        id = Long.read(b)
        
        gift_id = Long.read(b)
        
        title = String.read(b)
        
        slug = String.read(b)
        
        num = Int.read(b)
        
        owner_id = TLObject.read(b) if flags & (1 << 0) else None
        
        owner_name = String.read(b) if flags & (1 << 1) else None
        owner_address = String.read(b) if flags & (1 << 2) else None
        attributes = TLObject.read(b)
        
        availability_issued = Int.read(b)
        
        availability_total = Int.read(b)
        
        gift_address = String.read(b) if flags & (1 << 3) else None
        resell_amount = TLObject.read(b) if flags & (1 << 4) else []
        
        released_by = TLObject.read(b) if flags & (1 << 5) else None
        
        value_amount = Long.read(b) if flags & (1 << 8) else None
        value_currency = String.read(b) if flags & (1 << 8) else None
        value_usd_amount = Long.read(b) if flags & (1 << 8) else None
        theme_peer = TLObject.read(b) if flags & (1 << 10) else None
        
        peer_color = TLObject.read(b) if flags & (1 << 11) else None
        
        host_id = TLObject.read(b) if flags & (1 << 12) else None
        
        offer_min_stars = Int.read(b) if flags & (1 << 13) else None
        craft_chance_permille = Int.read(b) if flags & (1 << 16) else None
        return StarGiftUnique(id=id, gift_id=gift_id, title=title, slug=slug, num=num, attributes=attributes, availability_issued=availability_issued, availability_total=availability_total, require_premium=require_premium, resale_ton_only=resale_ton_only, theme_available=theme_available, burned=burned, crafted=crafted, owner_id=owner_id, owner_name=owner_name, owner_address=owner_address, gift_address=gift_address, resell_amount=resell_amount, released_by=released_by, value_amount=value_amount, value_currency=value_currency, value_usd_amount=value_usd_amount, theme_peer=theme_peer, peer_color=peer_color, host_id=host_id, offer_min_stars=offer_min_stars, craft_chance_permille=craft_chance_permille)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 6) if self.require_premium else 0
        flags |= (1 << 7) if self.resale_ton_only else 0
        flags |= (1 << 9) if self.theme_available else 0
        flags |= (1 << 14) if self.burned else 0
        flags |= (1 << 15) if self.crafted else 0
        flags |= (1 << 0) if self.owner_id is not None else 0
        flags |= (1 << 1) if self.owner_name is not None else 0
        flags |= (1 << 2) if self.owner_address is not None else 0
        flags |= (1 << 3) if self.gift_address is not None else 0
        flags |= (1 << 4) if self.resell_amount else 0
        flags |= (1 << 5) if self.released_by is not None else 0
        flags |= (1 << 8) if self.value_amount is not None else 0
        flags |= (1 << 8) if self.value_currency is not None else 0
        flags |= (1 << 8) if self.value_usd_amount is not None else 0
        flags |= (1 << 10) if self.theme_peer is not None else 0
        flags |= (1 << 11) if self.peer_color is not None else 0
        flags |= (1 << 12) if self.host_id is not None else 0
        flags |= (1 << 13) if self.offer_min_stars is not None else 0
        flags |= (1 << 16) if self.craft_chance_permille is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.gift_id))
        
        b.write(String(self.title))
        
        b.write(String(self.slug))
        
        b.write(Int(self.num))
        
        if self.owner_id is not None:
            b.write(self.owner_id.write())
        
        if self.owner_name is not None:
            b.write(String(self.owner_name))
        
        if self.owner_address is not None:
            b.write(String(self.owner_address))
        
        b.write(Vector(self.attributes))
        
        b.write(Int(self.availability_issued))
        
        b.write(Int(self.availability_total))
        
        if self.gift_address is not None:
            b.write(String(self.gift_address))
        
        if self.resell_amount is not None:
            b.write(Vector(self.resell_amount))
        
        if self.released_by is not None:
            b.write(self.released_by.write())
        
        if self.value_amount is not None:
            b.write(Long(self.value_amount))
        
        if self.value_currency is not None:
            b.write(String(self.value_currency))
        
        if self.value_usd_amount is not None:
            b.write(Long(self.value_usd_amount))
        
        if self.theme_peer is not None:
            b.write(self.theme_peer.write())
        
        if self.peer_color is not None:
            b.write(self.peer_color.write())
        
        if self.host_id is not None:
            b.write(self.host_id.write())
        
        if self.offer_min_stars is not None:
            b.write(Int(self.offer_min_stars))
        
        if self.craft_chance_permille is not None:
            b.write(Int(self.craft_chance_permille))
        
        return b.getvalue()
