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


class StarGiftAuctionState(TLObject):
    """Represents an active or pending auction ».

    Constructor of :obj:`~pyrogram.raw.base.StarGiftAuctionState`.

    Details:
        - Layer: ``228``
        - ID: ``771A4E66``

    Parameters:
        version (``int`` ``32-bit``):
            Only apply incoming starGiftAuctionState constructors if the received version is bigger than the locally cached version.

        start_date (``int`` ``32-bit``):
            UNIX timestamp indicating when the auction will start (or when it started, if it's in the past).

        end_date (``int`` ``32-bit``):
            UNIX timestamp indicating when the auction will end

        min_bid_amount (``int`` ``64-bit``):
            Minumum allowed bid amount in Telegram Stars: only applicable if the user hasn't made a bid yet, otherwise must be overridden to the value of starGiftAuctionUserState.min_bid_amount (which will be set if and only if the user already made a bid to this auction).

        bid_levels (List of :obj:`AuctionBidLevel <pyrogram.raw.base.AuctionBidLevel>`):
            Contains a sparse list of bids starting from the top bids, a more detailed description is available in the docs.

        top_bidders (List of ``int`` ``64-bit``):
            User IDs of the top 3 bidders (the user constructors will be returned as min constructors in the containing object).

        next_round_at (``int`` ``32-bit``):
            UNIX timestamp indicating when the current auction round will end, distributing starGift.gifts_per_round gifts to the top starGift.gifts_per_round bidders.

        last_gift_num (``int`` ``32-bit``):
            The number of gifts that were distributed in the previous round (also used to compute the approximated index of the gift that the current user will receive, last_gift_num + approx_pos, see here » for more info).

        gifts_left (``int`` ``32-bit``):
            The remaining number of gifts that are yet to be distributed.

        current_round (``int`` ``32-bit``):
            The current round number (starting from 1).

        total_rounds (``int`` ``32-bit``):
            The total number of rounds in this auction.

        rounds (List of :obj:`StarGiftAuctionRound <pyrogram.raw.base.StarGiftAuctionRound>`):
            Detailed round information.

    """

    __slots__: List[str] = ["version", "start_date", "end_date", "min_bid_amount", "bid_levels", "top_bidders", "next_round_at", "last_gift_num", "gifts_left", "current_round", "total_rounds", "rounds"]

    ID = 0x771a4e66
    QUALNAME = "types.StarGiftAuctionState"

    def __init__(self, *, version: int, start_date: int, end_date: int, min_bid_amount: int, bid_levels: List["raw.base.AuctionBidLevel"], top_bidders: List[int], next_round_at: int, last_gift_num: int, gifts_left: int, current_round: int, total_rounds: int, rounds: List["raw.base.StarGiftAuctionRound"]) -> None:
        self.version = version  # int
        self.start_date = start_date  # int
        self.end_date = end_date  # int
        self.min_bid_amount = min_bid_amount  # long
        self.bid_levels = bid_levels  # Vector<AuctionBidLevel>
        self.top_bidders = top_bidders  # Vector<long>
        self.next_round_at = next_round_at  # int
        self.last_gift_num = last_gift_num  # int
        self.gifts_left = gifts_left  # int
        self.current_round = current_round  # int
        self.total_rounds = total_rounds  # int
        self.rounds = rounds  # Vector<StarGiftAuctionRound>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StarGiftAuctionState":
        # No flags
        
        version = Int.read(b)
        
        start_date = Int.read(b)
        
        end_date = Int.read(b)
        
        min_bid_amount = Long.read(b)
        
        bid_levels = TLObject.read(b)
        
        top_bidders = TLObject.read(b, Long)
        
        next_round_at = Int.read(b)
        
        last_gift_num = Int.read(b)
        
        gifts_left = Int.read(b)
        
        current_round = Int.read(b)
        
        total_rounds = Int.read(b)
        
        rounds = TLObject.read(b)
        
        return StarGiftAuctionState(version=version, start_date=start_date, end_date=end_date, min_bid_amount=min_bid_amount, bid_levels=bid_levels, top_bidders=top_bidders, next_round_at=next_round_at, last_gift_num=last_gift_num, gifts_left=gifts_left, current_round=current_round, total_rounds=total_rounds, rounds=rounds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.version))
        
        b.write(Int(self.start_date))
        
        b.write(Int(self.end_date))
        
        b.write(Long(self.min_bid_amount))
        
        b.write(Vector(self.bid_levels))
        
        b.write(Vector(self.top_bidders, Long))
        
        b.write(Int(self.next_round_at))
        
        b.write(Int(self.last_gift_num))
        
        b.write(Int(self.gifts_left))
        
        b.write(Int(self.current_round))
        
        b.write(Int(self.total_rounds))
        
        b.write(Vector(self.rounds))
        
        return b.getvalue()
