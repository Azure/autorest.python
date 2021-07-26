# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .imports import FileImport
from .lro_operation import LROOperation
from .paging_operation import PagingOperation

class LROPagingOperation(PagingOperation, LROOperation):

    def imports(self, code_model, async_mode: bool, is_python_3_file: bool) -> FileImport:
        lro_imports = LROOperation.imports(self, code_model, async_mode, is_python_3_file)
        paging_imports = PagingOperation.imports(self, code_model, async_mode, is_python_3_file)

        file_import = lro_imports
        file_import.merge(paging_imports)
        return file_import

    @property
    def success_status_code(self):
        """The list of all successfull status code.
        """
        return [200]
