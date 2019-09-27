# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from enum import Enum, auto


class ImportType(Enum):
    STDLIB = auto()
    THIRPARTY = auto()
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



