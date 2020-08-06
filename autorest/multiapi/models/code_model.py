# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import Any, Dict

class CodeModel(object):
    def __init__(
        self,
        module_name: str,
        default_api_version: str,
        default_version_metadata: Dict[str, Any],
        mod_to_api_version: Dict[str, str]
    ):
        self.module_name = module_name
        self.default_version_metadata = default_version_metadata
        self.service_client = None
        self.config = None
        self.operation_groups = None
        self.mixin_operations = None
        self.global_parameters = None
