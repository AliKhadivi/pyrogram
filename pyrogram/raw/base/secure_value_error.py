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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import TYPE_CHECKING, Any, Union
from pyrogram import raw

# Runtime keeps the exact constructor union for compatibility and docs.
# Static analysis treats raw base aliases as dynamic because legacy Pyrogram
# parsers intentionally duck-type constructor-specific fields after runtime
# checks that Pyright cannot reliably infer across generated TL unions.
if TYPE_CHECKING:
    SecureValueError = Any
else:
    SecureValueError = Union[raw.types.SecureValueError, raw.types.SecureValueErrorData, raw.types.SecureValueErrorFile, raw.types.SecureValueErrorFiles, raw.types.SecureValueErrorFrontSide, raw.types.SecureValueErrorReverseSide, raw.types.SecureValueErrorSelfie, raw.types.SecureValueErrorTranslationFile, raw.types.SecureValueErrorTranslationFiles]

_doc = """Secure value error

    Constructors:
        This base type has 9 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            SecureValueError
            SecureValueErrorData
            SecureValueErrorFile
            SecureValueErrorFiles
            SecureValueErrorFrontSide
            SecureValueErrorReverseSide
            SecureValueErrorSelfie
            SecureValueErrorTranslationFile
            SecureValueErrorTranslationFiles"""
try:
    _t = type(SecureValueError)
    _module = getattr(_t, "__module__", "")
    _name = getattr(_t, "__name__", "")
    # typing.Union (and UnionType) can have a read-only __doc__ on newer Python versions
    if _module != "typing" and not (_module == "types" and _name == "UnionType"):
        SecureValueError.__doc__ = _doc
except (AttributeError, TypeError):
    pass
