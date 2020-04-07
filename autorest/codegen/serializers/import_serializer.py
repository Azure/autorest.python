# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import copy
from typing import Dict, Set, Optional, List
from ..models.imports import ImportType, FileImport, IsTypingImport

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
    def __init__(self, file_import: FileImport, is_python_2_file: bool) -> None:
        self._file_import = file_import
        self.is_python_2_file = is_python_2_file

    def _get_typing_imports_dict(self):
        typing_imports_dict = {}
        if self._file_import.imports.get(IsTypingImport.ALWAYS):
            typing_imports_dict = copy.copy(self._file_import.imports[IsTypingImport.ALWAYS])
        if self.is_python_2_file and self._file_import.imports.get(IsTypingImport.PYTHON2):
            typing_imports_dict.update(self._file_import.imports[IsTypingImport.PYTHON2])
        return typing_imports_dict

    def _get_non_typing_imports_dict(self):
        non_typing_imports_dict = {}
        if self._file_import.imports.get(IsTypingImport.NEVER):
            non_typing_imports_dict = copy.copy(self._file_import.imports[IsTypingImport.NEVER])
        if not self.is_python_2_file and self._file_import.imports.get(IsTypingImport.PYTHON2):
            non_typing_imports_dict.update(self._file_import.imports[IsTypingImport.PYTHON2])
        return non_typing_imports_dict

    def __str__(self) -> str:
        non_typing_imports = ""
        non_typing_imports_dict = self._get_non_typing_imports_dict()

        if non_typing_imports_dict:
            non_typing_imports = "\n\n".join(
                _get_import_clauses(non_typing_imports_dict, "\n")
            )

        typing_imports = ""
        typing_imports_dict = self._get_typing_imports_dict()
        if typing_imports_dict:
            typing_imports = "\n\ntry:\n    from typing import TYPE_CHECKING\nexcept:\n    TYPE_CHECKING = False"
            typing_imports += "\n\nif TYPE_CHECKING:\n    # pylint: disable=unused-import\n    "
            typing_imports += "\n\n    ".join(_get_import_clauses(typing_imports_dict, "\n    "))

        return non_typing_imports + typing_imports
