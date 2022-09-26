# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict
from coregen.black import BlackScriptPlugin
from .. import PluginAutorest


class BlackScriptPluginAutorest(BlackScriptPlugin, PluginAutorest):
    def get_options(self) -> Dict[str, Any]:
        return {"output_folder": self._autorestapi.get_value("outputFolderUri")}
