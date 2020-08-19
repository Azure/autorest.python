# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import Any, Dict, List
from pathlib import Path
from ..utils import _extract_version

class Client():
    def __init__(
        self,
        azure_arm: bool,
        default_version_metadata: Dict[str, Any],
        version_path_to_metadata: Dict[Path, Dict[str, Any]]
    ):
        self.name = default_version_metadata["client"]["name"]
        self.pipeline_client = "ARMPipelineClient" if azure_arm else "PipelineClient"
        self.filename = default_version_metadata["client"]["filename"]
        self.base_url = default_version_metadata["client"]["base_url"]
        self.description = default_version_metadata["client"]["description"]
        self.version_path_to_metadata = version_path_to_metadata

    @property
    def custom_base_url_to_api_version(self) -> Dict[str, List[str]]:
        custom_base_url_to_api_version: Dict[str, List[str]] = {}
        for version_path, metadata_json in self.version_path_to_metadata.items():
            custom_base_url = metadata_json["client"]["custom_base_url"]
            version = _extract_version(metadata_json, version_path)
            custom_base_url_to_api_version.setdefault(custom_base_url, []).append(version)
        return custom_base_url_to_api_version

    @property
    def has_lro_operations(self) -> bool:
        has_lro_operations = False
        for version_path, metadata_json in self.version_path_to_metadata.items():
            current_client_has_lro_operations = metadata_json["client"]["has_lro_operations"]
            if current_client_has_lro_operations:
                has_lro_operations = True
        return has_lro_operations
