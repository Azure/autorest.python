# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .imports import FileImport
from .lro_operation import LROOperation
from .paging_operation import PagingOperation, NoModelPagingOperation

class LROPagingOperation(PagingOperation, LROOperation):

    def imports(self, code_model, async_mode: bool) -> FileImport:
        lro_imports = LROOperation.imports(self, code_model, async_mode)
        paging_imports = PagingOperation.imports(self, code_model, async_mode)

        file_import = lro_imports
        file_import.merge(paging_imports)
        return file_import

    @property
    def paging_success_status_code(self):
        # hardcode paging's success status code in lro + paging to be 200
        return [200]

class NoModelLROPagingOperation(LROPagingOperation, NoModelPagingOperation):
    pass