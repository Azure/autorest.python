# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from typing import Any, Dict
from pathlib import Path
from .imports import FileImport

class OperationMixinGroup(object):
    def __init__(self, version_path_to_metadata: Dict[Path, Dict[str, Any]]):
        self.version_path_to_metadata = version_path_to_metadata


    def imports(self, async_mode: bool) -> str:
        imports = FileImport()
        imports_to_load = "async_imports" if async_mode else "sync_imports"
        for version_path, metadata_json in self.version_path_to_metadata.items():
            if not metadata_json.get('operation_mixins'):
                continue
            current_version_imports = FileImport(json.loads(metadata_json[imports_to_load]))
            imports.merge(current_version_imports)
        return imports
