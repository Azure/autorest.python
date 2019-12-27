# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum, auto


class ImportType(Enum):
    STDLIB = auto()
    THIRDPARTY = auto()
    AZURECORE = auto()
    LOCAL = auto()

class FileImport:
    def __init__(self):
        # Basic implementation
        # First level dict: ImportType
        # Second level dict: the package name.
        # Thirs level set: None if this import is a "import", the name to import if it's a "from"
        self._imports = dict()

    def add_from_import(self, from_section, name_import, import_type):
        """Add an import to this import block.
        """
        self._imports.setdefault(
            import_type,
            dict()
        ).setdefault(
            from_section,
            set()
        ).add(name_import)

    def add_import(self, name_import, import_type):
        # Implementation detail: a regular import is just a "from" with no from
        self.add_from_import(name_import, None, import_type)

    @property
    def imports(self):
        return self._imports

    def merge(self, file_import):
        """Merge the given file import format."""
        for import_type, package_list in file_import.imports.items():
            for package_name, module_list in package_list.items():
                for module_name in module_list:
                    self.add_from_import(package_name, module_name, import_type)
