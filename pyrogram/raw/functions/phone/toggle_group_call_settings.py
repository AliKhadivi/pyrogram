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


class ToggleGroupCallSettings(TLObject["raw.base.Updates"]):
    """Change group call settings. Each setting supports different group call types, see here » for more info.


    Details:
        - Layer: ``228``
        - ID: ``974392F2``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            Group call whose settings should be changed

        reset_invite_hash (``bool``, *optional*):
            Invalidate existing invite links for video chats, livestreams and conferences

        join_muted (``bool``, *optional*):
            Whether users joining a non-RTMP video chat/livestream should be muted by default

        messages_enabled (``bool``, *optional*):
            Enable or disable the in-call message overlay in video chats/livestreams, conferences and live stories, including in RTMP mode

        send_paid_messages_stars (``int`` ``64-bit``, *optional*):
            Set the minimum Telegram Stars donation required from users other than the live story owner for each comment; the owner may always comment without donating, and 0 allows free comments for everyone

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "reset_invite_hash", "join_muted", "messages_enabled", "send_paid_messages_stars"]

    ID = 0x974392f2
    QUALNAME = "functions.phone.ToggleGroupCallSettings"

    def __init__(self, *, call: "raw.base.InputGroupCall", reset_invite_hash: Optional[bool] = None, join_muted: Optional[bool] = None, messages_enabled: Optional[bool] = None, send_paid_messages_stars: Optional[int] = None) -> None:
        self.call = call  # InputGroupCall
        self.reset_invite_hash = reset_invite_hash  # flags.1?true
        self.join_muted = join_muted  # flags.0?Bool
        self.messages_enabled = messages_enabled  # flags.2?Bool
        self.send_paid_messages_stars = send_paid_messages_stars  # flags.3?long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleGroupCallSettings":
        
        flags = Int.read(b)
        
        reset_invite_hash = True if flags & (1 << 1) else False
        call = TLObject.read(b)
        
        join_muted = Bool.read(b) if flags & (1 << 0) else None
        messages_enabled = Bool.read(b) if flags & (1 << 2) else None
        send_paid_messages_stars = Long.read(b) if flags & (1 << 3) else None
        return ToggleGroupCallSettings(call=call, reset_invite_hash=reset_invite_hash, join_muted=join_muted, messages_enabled=messages_enabled, send_paid_messages_stars=send_paid_messages_stars)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.reset_invite_hash else 0
        flags |= (1 << 0) if self.join_muted is not None else 0
        flags |= (1 << 2) if self.messages_enabled is not None else 0
        flags |= (1 << 3) if self.send_paid_messages_stars is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        if self.join_muted is not None:
            b.write(Bool(self.join_muted))
        
        if self.messages_enabled is not None:
            b.write(Bool(self.messages_enabled))
        
        if self.send_paid_messages_stars is not None:
            b.write(Long(self.send_paid_messages_stars))
        
        return b.getvalue()
