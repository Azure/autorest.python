# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""An autorest MD to RST plugin.
"""
from typing import Any, Dict
from coregen.m2r import M2R
from .. import YamlUpdatePluginAutorest

class M2RAutorest(YamlUpdatePluginAutorest, M2R):
    def get_options(self) -> Dict[str, Any]:
        return {}
