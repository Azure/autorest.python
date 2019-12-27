# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from ..models.imports import ImportType


class FileImportSerializer:
    def __init__(self, file_import):
        self._file_import = file_import

    def __str__(self):
        import_clause = []
        for import_type in ImportType:
            if import_type in self._file_import.imports:
                import_clause.append(self._serialize_type(self._file_import.imports[import_type]))
        return "\n\n".join(import_clause)

    def _serialize_package(self, package_name, module_list):
        buffer = []
        if None in module_list:
            buffer.append(f"import {package_name}")
        if module_list != {None}:
            buffer.append(
                "from {} import {}".format(
                    package_name,
                    ", ".join(sorted([mod for mod in module_list if mod is not None]))
                )
            )
        return "\n".join(buffer)

    def _serialize_type(self, import_type_dict):
        """Serialize a given import type."""
        import_list = []
        for package_name in sorted(list(import_type_dict.keys())):
            module_list = import_type_dict[package_name]
            import_list.append(self._serialize_package(package_name, module_list))
        return "\n".join(import_list)
