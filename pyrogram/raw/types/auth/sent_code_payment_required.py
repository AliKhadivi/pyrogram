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


class SentCodePaymentRequired(TLObject):
    """Official apps may receive this constructor, indicating that due to the high cost of SMS verification codes for the user's country/provider, the user must purchase a Telegram Premium subscription in order to proceed with the login/signup, see here » for more info.

    Constructor of :obj:`~pyrogram.raw.base.auth.SentCode`.

    Details:
        - Layer: ``228``
        - ID: ``F8827EBF``

    Parameters:
        store_product (``str``):
            For official apps, tore identifier of the Telegram Premium subscription.

        phone_code_hash (``str``):
            Phone code hash, to be stored and later re-used with auth.signIn

        support_email_address (``str``):
            An email address that can be contacted for more information about this request.

        support_email_subject (``str``):
            The mandatory subject for the email.

        premium_days (``int`` ``32-bit``):
            Duration in days of the Telegram Premium subscription granted by this purchase.

        currency (``str``):
            Three-letter ISO 4217 currency code.

        amount (``int`` ``64-bit``):
            Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145. See the exp parameter in currencies.json, it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).

    Functions:
        This object can be returned by 7 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.SendCode
            auth.ResendCode
            auth.ResetLoginEmail
            auth.CheckPaidAuth
            account.SendChangePhoneCode
            account.SendConfirmPhoneCode
            account.SendVerifyPhoneCode
    """

    __slots__: List[str] = ["store_product", "phone_code_hash", "support_email_address", "support_email_subject", "premium_days", "currency", "amount"]

    ID = 0xf8827ebf
    QUALNAME = "types.auth.SentCodePaymentRequired"

    def __init__(self, *, store_product: str, phone_code_hash: str, support_email_address: str, support_email_subject: str, premium_days: int, currency: str, amount: int) -> None:
        self.store_product = store_product  # string
        self.phone_code_hash = phone_code_hash  # string
        self.support_email_address = support_email_address  # string
        self.support_email_subject = support_email_subject  # string
        self.premium_days = premium_days  # int
        self.currency = currency  # string
        self.amount = amount  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodePaymentRequired":
        # No flags
        
        store_product = String.read(b)
        
        phone_code_hash = String.read(b)
        
        support_email_address = String.read(b)
        
        support_email_subject = String.read(b)
        
        premium_days = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return SentCodePaymentRequired(store_product=store_product, phone_code_hash=phone_code_hash, support_email_address=support_email_address, support_email_subject=support_email_subject, premium_days=premium_days, currency=currency, amount=amount)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.store_product))
        
        b.write(String(self.phone_code_hash))
        
        b.write(String(self.support_email_address))
        
        b.write(String(self.support_email_subject))
        
        b.write(Int(self.premium_days))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
