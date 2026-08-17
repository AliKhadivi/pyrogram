#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  Jalgo-specific client defaults.

import inspect
import platform

from . import __version__
from .client import Client as _BaseClient


class Client(_BaseClient):
    """Pyrogram client using Jalgo Desktop connection metadata by default.

    Explicit ``app_version``, ``device_model`` and ``system_version`` values
    supplied by the caller are preserved. Only omitted values receive the
    Jalgo Desktop defaults.
    """

    APP_VERSION = f"Jalgo Desktop {__version__}"
    DEVICE_MODEL = "Jalgo Desktop"
    SYSTEM_VERSION = f"{platform.system()} {platform.release()}"

    _BASE_INIT_SIGNATURE = inspect.signature(_BaseClient.__init__)

    def __init__(self, *args, **kwargs):
        bound = self._BASE_INIT_SIGNATURE.bind_partial(self, *args, **kwargs)

        if "app_version" not in bound.arguments:
            kwargs["app_version"] = self.APP_VERSION

        if "device_model" not in bound.arguments:
            kwargs["device_model"] = self.DEVICE_MODEL

        if "system_version" not in bound.arguments:
            kwargs["system_version"] = self.SYSTEM_VERSION

        super().__init__(*args, **kwargs)


# Keep introspection/help output compatible with the original Client signature.
Client.__init__.__signature__ = inspect.signature(_BaseClient.__init__)
