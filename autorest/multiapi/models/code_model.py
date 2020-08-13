# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import Any, Dict, List
from pathlib import Path
from .client import Client
from .config import Config
from .operation_group import OperationGroup
from ..utils import _extract_version

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
        self.version_path_to_metadata = version_path_to_metadata
        self.service_client = Client(default_version_metadata, version_path_to_metadata)
        self.config = Config(default_version_metadata)
        self.mixin_operations = None
        self.global_parameters = None

    @property
    def operation_groups(self) -> List[OperationGroup]:
        operation_groups = []
        for version_path, metadata_json in self.version_path_to_metadata.items():
            operation_groups_metadata = metadata_json['operation_groups']
            version = _extract_version(metadata_json, version_path)
            for operation_group_name, operation_group_class_name in operation_groups_metadata.items():
                try:
                    operation_group = [og for og in operation_groups if og.name == operation_group_name][0]
                except IndexError:
                    operation_group = OperationGroup(operation_group_name, operation_group_class_name)
                    operation_groups.append(operation_group)
                operation_group.append_available_api(version_path.name)
        return operation_groups
