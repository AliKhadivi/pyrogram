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


class InputKeyboardButtonRequestPeer(TLObject):
    """Prompts the user to select and share one or more peers with the bot using messages.sendBotRequestedPeer.

    Constructor of :obj:`~pyrogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``228``
        - ID: ``2B78156``

    Parameters:
        text (``str``):
            Button text

        button_id (``int`` ``32-bit``):
            Button ID, to be passed to messages.sendBotRequestedPeer.

        peer_type (:obj:`RequestPeerType <pyrogram.raw.base.RequestPeerType>`):
            Filtering criteria to use for the peer selection list shown to the user. The list should display all existing peers of the specified type, and should also offer an option for the user to create and immediately use one or more (up to max_quantity) peers of the specified type, if needed.

        max_quantity (``int`` ``32-bit``):
            Maximum number of peers that can be chosen.

        name_requested (``bool``, *optional*):
            Set this flag to request the peer's name.

        username_requested (``bool``, *optional*):
            Set this flag to request the peer's @username (if any).

        photo_requested (``bool``, *optional*):
            Set this flag to request the peer's photo (if any).

        style (:obj:`KeyboardButtonStyle <pyrogram.raw.base.KeyboardButtonStyle>`, *optional*):
            Button style, see here » for more info on button styles.

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            bots.GetRequestedWebViewButton
    """

    __slots__: List[str] = ["text", "button_id", "peer_type", "max_quantity", "name_requested", "username_requested", "photo_requested", "style"]

    ID = 0x2b78156
    QUALNAME = "types.InputKeyboardButtonRequestPeer"

    def __init__(self, *, text: str, button_id: int, peer_type: "raw.base.RequestPeerType", max_quantity: int, name_requested: Optional[bool] = None, username_requested: Optional[bool] = None, photo_requested: Optional[bool] = None, style: Optional["raw.base.KeyboardButtonStyle"] = None) -> None:
        self.text = text  # string
        self.button_id = button_id  # int
        self.peer_type = peer_type  # RequestPeerType
        self.max_quantity = max_quantity  # int
        self.name_requested = name_requested  # flags.0?true
        self.username_requested = username_requested  # flags.1?true
        self.photo_requested = photo_requested  # flags.2?true
        self.style = style  # flags.10?KeyboardButtonStyle

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputKeyboardButtonRequestPeer":
        
        flags = Int.read(b)
        
        name_requested = True if flags & (1 << 0) else False
        username_requested = True if flags & (1 << 1) else False
        photo_requested = True if flags & (1 << 2) else False
        style = TLObject.read(b) if flags & (1 << 10) else None
        
        text = String.read(b)
        
        button_id = Int.read(b)
        
        peer_type = TLObject.read(b)
        
        max_quantity = Int.read(b)
        
        return InputKeyboardButtonRequestPeer(text=text, button_id=button_id, peer_type=peer_type, max_quantity=max_quantity, name_requested=name_requested, username_requested=username_requested, photo_requested=photo_requested, style=style)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.name_requested else 0
        flags |= (1 << 1) if self.username_requested else 0
        flags |= (1 << 2) if self.photo_requested else 0
        flags |= (1 << 10) if self.style is not None else 0
        b.write(Int(flags))
        
        if self.style is not None:
            b.write(self.style.write())
        
        b.write(String(self.text))
        
        b.write(Int(self.button_id))
        
        b.write(self.peer_type.write())
        
        b.write(Int(self.max_quantity))
        
        return b.getvalue()
