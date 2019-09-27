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
