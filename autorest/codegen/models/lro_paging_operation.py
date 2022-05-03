# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, TYPE_CHECKING
from .imports import FileImport
from .lro_operation import LROOperation, _LROOperationBase, OverloadedLROOperation
from .paging_operation import (
    OverloadedPagingOperation,
    PagingOperation,
    _PagingOperationBase,
)
from .operation import OperationBase, Operation

if TYPE_CHECKING:
    from .code_model import CodeModel


class _LROPagingOperationBase(
    _LROOperationBase, _PagingOperationBase
):  # pylint: disable=abstract-method
    @property
    def success_status_codes(self):
        """The list of all successfull status code."""
        return [200]

    @property
    def operation_type(self) -> str:
        return "lropaging"

    def response_type_annotation(self, **kwargs) -> str:
        paging_type_annotation = _PagingOperationBase.response_type_annotation(
            self, **kwargs
        )
        return f"{self.get_poller(kwargs.pop('async_mode'))}[{paging_type_annotation}]"

    def response_docstring_type(self, **kwargs) -> str:
        paging_docstring_type = _PagingOperationBase.response_docstring_type(
            self, **kwargs
        )
        return f"~{self.get_poller_path(kwargs.pop('async_mode'))}[{paging_docstring_type}]"

    def response_docstring_text(self, **kwargs) -> str:
        base_description = (
            "An instance of LROPoller that returns an iterator like instance of "
        )
        if not self.code_model.options["version_tolerant"]:
            base_description += "either "
        return base_description + OperationBase.response_docstring_text(self)

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        return f"ClsType[{OperationBase.response_type_annotation(self, async_mode=async_mode)}]"


class LROPagingOperation(LROOperation, PagingOperation, _LROPagingOperationBase):
    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        lro_imports = LROOperation.imports(self, async_mode, is_python3_file)
        paging_imports = PagingOperation.imports(self, async_mode, is_python3_file)

        file_import = lro_imports
        file_import.merge(paging_imports)
        return file_import


class OverloadedLROPagingOperation(
    OverloadedLROOperation, OverloadedPagingOperation, _LROPagingOperationBase
):
    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        lro_imports = OverloadedLROOperation.imports(self, async_mode, is_python3_file)
        paging_imports = OverloadedPagingOperation.imports(
            self, async_mode, is_python3_file
        )

        file_import = lro_imports
        file_import.merge(paging_imports)
        return file_import

    @staticmethod
    def overload_operation_class() -> Callable[
        [Dict[str, Any], "CodeModel"], Operation
    ]:
        return LROPagingOperation.from_yaml
