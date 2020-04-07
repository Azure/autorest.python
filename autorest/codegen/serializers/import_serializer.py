# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, Set, Optional, List
from ..models.imports import ImportType, FileImport

def _serialize_package(package_name: str, module_list: Set[Optional[str]], delimiter: str) -> str:
    buffer = []
    if None in module_list:
        buffer.append(f"import {package_name}")
    if module_list != {None}:
        buffer.append(
            "from {} import {}".format(
                package_name, ", ".join(sorted([mod for mod in module_list if mod is not None]))
            )
        )
    return delimiter.join(buffer)

def _serialize_type(import_type_dict: Dict[str, Set[Optional[str]]], delimiter: str) -> str:
    """Serialize a given import type."""
    import_list = []
    for package_name in sorted(list(import_type_dict.keys())):
        module_list = import_type_dict[package_name]
        import_list.append(_serialize_package(package_name, module_list, delimiter))
    return delimiter.join(import_list)

def _get_import_clauses(imports: Dict[ImportType, Dict[str, Set[Optional[str]]]], delimiter: str) -> List[str]:
    import_clause = []
    for import_type in ImportType:
        if import_type in imports:
            import_clause.append(_serialize_type(imports[import_type], delimiter))
    return import_clause


class FileImportSerializer:
    def __init__(self, file_import: FileImport) -> None:
        self._file_import = file_import

    def __str__(self) -> str:
        non_typing_imports = "\n\n".join(_get_import_clauses(self._file_import.imports[False], "\n"))

        if not self._file_import.imports.get(True):
            # this means we don't have typing imports
            return non_typing_imports
        typing_imports = "try:\n    from typing import TYPE_CHECKING\nexcept:\n    TYPE_CHECKING = False"
        typing_imports += "\n\nif TYPE_CHECKING:\n    # pylint: disable=unused-import\n    "
        typing_imports += "\n\n    ".join(_get_import_clauses(self._file_import.imports[True], "\n    "))

        return non_typing_imports + "\n\n" + typing_imports
