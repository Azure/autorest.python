# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import os
from ..jsonrpc import AutorestAPI

from .. import Plugin

_LOGGER = logging.getLogger(__name__)


class BlackFormattingScriptPlugin(Plugin):
    def process(self) -> bool:
        generator = BlackFormatting(self._autorestapi)
        return generator.process()


class BlackFormatting:

    def __init__(self, autorestapi) -> None:
        self._autorestapi = autorestapi

    def process(self) -> bool:
        black_formatting = self._autorestapi.get_boolean_value("black-formatting", False)
        if black_formatting:
            output_folder = self._autorestapi.get_value("output-folder")
            os.chdir(output_folder)
            os.system('black .')
        return True