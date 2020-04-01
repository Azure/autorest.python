# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Set, Optional
from ..models.imports import ImportType, FileImport


class FileImportSerializer:
    def __init__(self, file_import: FileImport) -> None:
        self._file_import = file_import
        self._imports_to_serialize: Optional[Dict[ImportType, Dict[str, Set[Optional[str]]]]] = None

    @property
    def has_typing(self) -> bool:
        return bool(self._file_import.imports.get(True))

    def non_typing(self) -> "FileImportSerializer":
        self._imports_to_serialize = self._file_import.imports[False]
        return self

    def typing(self) -> "FileImportSerializer":
        self._imports_to_serialize = self._file_import.imports[True]
        return self

    def __str__(self) -> str:
        if not self._imports_to_serialize:
            raise TypeError("Must call typing() or non_typing() on imports object in jinja templatte")
        import_clause = []
        for import_type in ImportType:
            if import_type in self._imports_to_serialize:
                import_clause.append(FileImportSerializer._serialize_type(self._imports_to_serialize[import_type]))
        return "\n\n".join(import_clause)

    @staticmethod
    def _serialize_package(package_name: str, module_list: Set[Optional[str]]) -> str:
        buffer = []
        if None in module_list:
            buffer.append(f"import {package_name}")
        if module_list != {None}:
            buffer.append(
                "from {} import {}".format(
                    package_name, ", ".join(sorted([mod for mod in module_list if mod is not None]))
                )
            )
        return "\n".join(buffer)

    @staticmethod
    def _serialize_type(import_type_dict: Dict[str, Set[Optional[str]]]) -> str:
        """Serialize a given import type."""
        import_list = []
        for package_name in sorted(list(import_type_dict.keys())):
            module_list = import_type_dict[package_name]
            import_list.append(FileImportSerializer._serialize_package(package_name, module_list))
        return "\n".join(import_list)
