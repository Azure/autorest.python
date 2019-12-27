# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import ABC, abstractmethod

from .jsonrpc import AutorestAPI
from ._version import VERSION


__version__ = VERSION


class Plugin(ABC):
    """A base class for autorest plugin.

    :param autorestapi: An autorest API instance
    """

    def __init__(self, autorestapi: AutorestAPI):
        self._autorestapi = autorestapi

    @abstractmethod
    def process(self) -> bool:
        """The plugin process.

        :rtype: bool
        :returns: True if everything's ok, False optherwise
        :raises Exception: Could raise any exception, stacktrace will be sent to autorest API
        """
        raise NotImplementedError()

__all__ = ["Plugin"]
