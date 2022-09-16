# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict

from coregen.postprocess import PostProcessPlugin
from .. import PluginAutorest

class PostProcessPluginAutorest(PostProcessPlugin, PluginAutorest):
    def get_options(self) -> Dict[str, Any]:
        return {"outputFolderUri": self._autorestapi.get_value("outputFolderUri")}
