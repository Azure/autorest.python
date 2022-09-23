# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The preprocessing autorest plugin.
"""
from typing import Any, Dict
from coregen.preprocess import PreProcessPlugin
from .. import YamlUpdatePluginAutorest


class PreProcessPluginAutorest(YamlUpdatePluginAutorest, PreProcessPlugin):
    def get_options(self) -> Dict[str, Any]:
        options = {
            "version-tolerant": self._autorestapi.get_boolean_value("version-tolerant"),
            "azure-arm": self._autorestapi.get_boolean_value("azure-arm"),
        }
        return {k: v for k, v in options.items() if v is not None}
<<<<<<< HEAD
=======
