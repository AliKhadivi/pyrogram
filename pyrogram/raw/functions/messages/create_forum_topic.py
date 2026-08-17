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


class CreateForumTopic(TLObject["raw.base.Updates"]):
    """Create a forum topic.


    Details:
        - Layer: ``228``
        - ID: ``2F98C3D5``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            The supergroup, private chat (for forum-enabled bots) or forum bot (for users) where to create the topic.

        title (``str``):
            Topic title (maximum UTF-8 length: 128)

        random_id (``int`` ``64-bit``):
            Unique client message ID to prevent duplicate sending of the same event

        title_missing (``bool``, *optional*):
            If set, the topic has no user-defined title, can only be set for the per-user topics of bot forums; if this field is set, the topic title likely needs to be changed by the bot.

        icon_color (``int`` ``32-bit``, *optional*):
            If no custom emoji icon is specified, specifies the color of the fallback topic icon (RGB), one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F.

        icon_emoji_id (``int`` ``64-bit``, *optional*):
            ID of the custom emoji used as topic icon. Telegram Premium users can use any custom emoji, other users can only use the custom emojis contained in the inputStickerSetEmojiDefaultTopicIcons emoji pack.

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            Create the topic as the specified peer

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "title", "random_id", "title_missing", "icon_color", "icon_emoji_id", "send_as"]

    ID = 0x2f98c3d5
    QUALNAME = "functions.messages.CreateForumTopic"

    def __init__(self, *, peer: "raw.base.InputPeer", title: str, random_id: int, title_missing: Optional[bool] = None, icon_color: Optional[int] = None, icon_emoji_id: Optional[int] = None, send_as: Optional["raw.base.InputPeer"] = None) -> None:
        self.peer = peer  # InputPeer
        self.title = title  # string
        self.random_id = random_id  # long
        self.title_missing = title_missing  # flags.4?true
        self.icon_color = icon_color  # flags.0?int
        self.icon_emoji_id = icon_emoji_id  # flags.3?long
        self.send_as = send_as  # flags.2?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CreateForumTopic":
        
        flags = Int.read(b)
        
        title_missing = True if flags & (1 << 4) else False
        peer = TLObject.read(b)
        
        title = String.read(b)
        
        icon_color = Int.read(b) if flags & (1 << 0) else None
        icon_emoji_id = Long.read(b) if flags & (1 << 3) else None
        random_id = Long.read(b)
        
        send_as = TLObject.read(b) if flags & (1 << 2) else None
        
        return CreateForumTopic(peer=peer, title=title, random_id=random_id, title_missing=title_missing, icon_color=icon_color, icon_emoji_id=icon_emoji_id, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 4) if self.title_missing else 0
        flags |= (1 << 0) if self.icon_color is not None else 0
        flags |= (1 << 3) if self.icon_emoji_id is not None else 0
        flags |= (1 << 2) if self.send_as is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.title))
        
        if self.icon_color is not None:
            b.write(Int(self.icon_color))
        
        if self.icon_emoji_id is not None:
            b.write(Long(self.icon_emoji_id))
        
        b.write(Long(self.random_id))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()
