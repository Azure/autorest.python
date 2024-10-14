# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging

_LOGGER = logging.getLogger(__name__)

from . import PluginAutorest


class PostProcessPluginAutorest(PluginAutorest):
    def process(self) -> bool:
        _LOGGER.warning("There is no need for this plugin anymore, mypy will work with all customizations to generated code. Please remove this plugin from your configuration.")
        return True
