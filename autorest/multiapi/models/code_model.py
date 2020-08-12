# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import Any, Dict
from pathlib import Path
from .client import Client
from .config import Config


class CodeModel(object):
    def __init__(
        self,
        module_name: str,
        default_api_version: str,
        default_version_metadata: Dict[str, Any],
        mod_to_api_version: Dict[str, str],
        version_path_to_metadata: Dict[Path, Dict[str, Any]]
    ):
        self.module_name = module_name
        self.azure_arm = default_version_metadata["client"]["azure_arm"]
        self.default_version_metadata = default_version_metadata
        self.service_client = Client(default_version_metadata, version_path_to_metadata)
        self.config = Config(default_version_metadata)
        self.operation_groups = None
        self.mixin_operations = None
        self.global_parameters = None
