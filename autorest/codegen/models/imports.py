# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum, auto
from typing import Dict, Optional, Set


class ImportType(Enum):
    STDLIB = auto()
    THIRDPARTY = auto()
    AZURECORE = auto()
    LOCAL = auto()

class IsTypingImport(Enum):
    ALWAYS = auto()  # this import is always a typing import
    PYTHON2 = auto()  # is a typing import when we're dealing with files that py2 will use
    NEVER = auto()  # never a typing import


class FileImport:
    def __init__(self) -> None:
        # Basic implementation
        # First level dict: ImportType
        # Second level dict: the package name.
        # Thirs level set: None if this import is a "import", the name to import if it's a "from"
        self._imports: Dict[IsTypingImport, Dict[ImportType, Dict[str, Set[Optional[str]]]]] = dict()

    def _add_import(
        self,
        from_section: str,
        import_type: ImportType,
        name_import: Optional[str] = None,
        is_typing_import: IsTypingImport = IsTypingImport.NEVER
    ) -> None:
        self._imports.setdefault(
                is_typing_import, dict()
            ).setdefault(
                import_type, dict()
            ).setdefault(
                from_section, set()
            ).add(name_import)

    def add_from_import(
        self,
        from_section: str,
        name_import: str,
        import_type: ImportType,
        is_typing_import: IsTypingImport = IsTypingImport.NEVER
    ) -> None:
        """Add an import to this import block.
        """
        self._add_import(from_section, import_type, name_import, is_typing_import)

    def add_import(self, name_import: str, import_type: ImportType, is_typing_import: IsTypingImport = IsTypingImport.NEVER) -> None:
        # Implementation detail: a regular import is just a "from" with no from
        self._add_import(name_import, import_type, None, is_typing_import)

    @property
    def imports(self) -> Dict[IsTypingImport, Dict[ImportType, Dict[str, Set[Optional[str]]]]]:
        return self._imports

    def merge(self, file_import: "FileImport") -> None:
        """Merge the given file import format."""
        for is_typing_import, import_type_dict in file_import.imports.items():
            for import_type, package_list in import_type_dict.items():
                for package_name, module_list in package_list.items():
                    for module_name in module_list:
                        self._add_import(package_name, import_type, module_name, is_typing_import)
