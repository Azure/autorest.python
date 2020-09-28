# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from typing import Any, Dict, List
from pathlib import Path
from .imports import FileImport
from .mixin_operation import MixinOperation

class OperationMixinGroup:
    def __init__(
        self,
        version_path_to_metadata: Dict[Path, Dict[str, Any]],
        mod_to_api_version: Dict[str, str],
        default_api_version: str,
    ):
        self.default_api_version = default_api_version
        self.version_path_to_metadata = version_path_to_metadata
        self._mod_to_api_version = mod_to_api_version

    def imports(self, async_mode: bool) -> FileImport:
        imports = FileImport()
        imports_to_load = "async_imports" if async_mode else "sync_imports"
        for metadata_json in self.version_path_to_metadata.values():
            if not metadata_json.get('operation_mixins'):
                continue
            current_version_imports = FileImport(json.loads(metadata_json[imports_to_load]))
            imports.merge(current_version_imports)
        return imports

    @property
    def mixin_operations(self) -> List[MixinOperation]:
        mixin_operations: List[MixinOperation] = []
        for version_path, metadata_json in self.version_path_to_metadata.items():
            if not metadata_json.get("operation_mixins"):
                continue
            mixin_operations_metadata = metadata_json["operation_mixins"]
            for mixin_operation_name, mixin_operation_metadata in mixin_operations_metadata.items():
                if mixin_operation_name.startswith("_"):
                    continue
                try:
                    mixin_operation = [mo for mo in mixin_operations if mo.name == mixin_operation_name][0]
                except IndexError:
                    mixin_operation = MixinOperation(
                        name=mixin_operation_name, mod_to_api_version=self._mod_to_api_version
                    )
                    mixin_operations.append(mixin_operation)
                mixin_operation.append_available_api(version_path.name, mixin_operation_metadata)

        mixin_operations.sort(key=lambda x: x.name)
        return mixin_operations

    @property
    def has_different_calls_across_api_versions(self):
        return any(
            mixin_operation.has_different_calls_across_api_versions
            for mixin_operation in self.mixin_operations
        )
