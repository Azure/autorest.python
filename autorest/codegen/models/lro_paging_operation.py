# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .imports import FileImport
from .lro_operation import LROOperationBase
from .paging_operation import PagingOperationBase
from .operation import OperationBase
from .response import LROPagingResponse


class LROPagingOperation(LROOperationBase[LROPagingResponse], PagingOperationBase[LROPagingResponse]):
    @property
    def success_status_codes(self):
        """The list of all successfull status code."""
        return [200]

    @property
    def operation_type(self) -> str:
        return "lropaging"

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        return f"ClsType[{OperationBase.response_type_annotation(self, async_mode=async_mode)}]"

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        lro_imports = LROOperationBase.imports(self, async_mode, is_python3_file)
        paging_imports = PagingOperationBase.imports(self, async_mode, is_python3_file)

        file_import = lro_imports
        file_import.merge(paging_imports)
        return file_import
