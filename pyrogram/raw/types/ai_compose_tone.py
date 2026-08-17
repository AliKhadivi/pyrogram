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


class AiComposeTone(TLObject):
    """A custom AI composer tone », used to rephrase messages in a specific style with the AI message composer.

    Constructor of :obj:`~pyrogram.raw.base.AiComposeTone`.

    Details:
        - Layer: ``228``
        - ID: ``CFF63EA9``

    Parameters:
        id (``int`` ``64-bit``):
            Tone identifier

        access_hash (``int`` ``64-bit``):
            Tone access hash

        slug (``str``):
            Unique tone slug, used to share and install the tone via AI compose tone links »

        title (``str``):
            Human-readable tone name, up to aicompose_tone_title_length_max » UTF-8 characters long

        creator (``bool``, *optional*):
            Whether the current user is the creator of this tone

        emoji_id (``int`` ``64-bit``, *optional*):
            Custom emoji ID of the tone's icon

        prompt (``str``, *optional*):
            The prompt that describes how the AI should rephrase messages using this tone, up to aicompose_tone_prompt_length_max » UTF-8 characters long; only present for tones created by the current user

        installs_count (``int`` ``32-bit``, *optional*):
            Number of users that have installed this tone

        author_id (``int`` ``64-bit``, *optional*):
            ID of the user that created this tone, if made public by the author.

        example_english (:obj:`AiComposeToneExample <pyrogram.raw.base.AiComposeToneExample>`, *optional*):
            An example showing how a sample English message is rephrased by this tone; use aicompose.getToneExample to fetch more examples.

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            aicompose.CreateTone
            aicompose.UpdateTone
    """

    __slots__: List[str] = ["id", "access_hash", "slug", "title", "creator", "emoji_id", "prompt", "installs_count", "author_id", "example_english"]

    ID = 0xcff63ea9
    QUALNAME = "types.AiComposeTone"

    def __init__(self, *, id: int, access_hash: int, slug: str, title: str, creator: Optional[bool] = None, emoji_id: Optional[int] = None, prompt: Optional[str] = None, installs_count: Optional[int] = None, author_id: Optional[int] = None, example_english: Optional["raw.base.AiComposeToneExample"] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.slug = slug  # string
        self.title = title  # string
        self.creator = creator  # flags.0?true
        self.emoji_id = emoji_id  # flags.1?long
        self.prompt = prompt  # flags.4?string
        self.installs_count = installs_count  # flags.2?int
        self.author_id = author_id  # flags.3?long
        self.example_english = example_english  # flags.5?AiComposeToneExample

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AiComposeTone":
        
        flags = Int.read(b)
        
        creator = True if flags & (1 << 0) else False
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        slug = String.read(b)
        
        title = String.read(b)
        
        emoji_id = Long.read(b) if flags & (1 << 1) else None
        prompt = String.read(b) if flags & (1 << 4) else None
        installs_count = Int.read(b) if flags & (1 << 2) else None
        author_id = Long.read(b) if flags & (1 << 3) else None
        example_english = TLObject.read(b) if flags & (1 << 5) else None
        
        return AiComposeTone(id=id, access_hash=access_hash, slug=slug, title=title, creator=creator, emoji_id=emoji_id, prompt=prompt, installs_count=installs_count, author_id=author_id, example_english=example_english)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 1) if self.emoji_id is not None else 0
        flags |= (1 << 4) if self.prompt is not None else 0
        flags |= (1 << 2) if self.installs_count is not None else 0
        flags |= (1 << 3) if self.author_id is not None else 0
        flags |= (1 << 5) if self.example_english is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.slug))
        
        b.write(String(self.title))
        
        if self.emoji_id is not None:
            b.write(Long(self.emoji_id))
        
        if self.prompt is not None:
            b.write(String(self.prompt))
        
        if self.installs_count is not None:
            b.write(Int(self.installs_count))
        
        if self.author_id is not None:
            b.write(Long(self.author_id))
        
        if self.example_english is not None:
            b.write(self.example_english.write())
        
        return b.getvalue()
