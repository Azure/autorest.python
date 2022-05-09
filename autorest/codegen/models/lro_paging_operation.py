# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .imports import FileImport
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .operation import Operation


class LROPagingOperation(LROOperation, PagingOperation):
    @property
    def success_status_codes(self):
        """The list of all successfull status code."""
        return [200]

    @property
    def operation_type(self) -> str:
        return "lropaging"

    def response_type_annotation(self, **kwargs) -> str:
        paging_type_annotation = PagingOperation.response_type_annotation(
            self, **kwargs
        )
        return f"{self.get_poller(kwargs.pop('async_mode'))}[{paging_type_annotation}]"

    def response_docstring_type(self, **kwargs) -> str:
        paging_docstring_type = PagingOperation.response_docstring_type(self, **kwargs)
        return f"~{self.get_poller_path(kwargs.pop('async_mode'))}[{paging_docstring_type}]"

    def response_docstring_text(self, **kwargs) -> str:
        base_description = (
            "An instance of LROPoller that returns an iterator like instance of "
        )
        if not self.code_model.options["version_tolerant"]:
            base_description += "either "
        return base_description + Operation.response_docstring_text(self)

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        return f"ClsType[{Operation.response_type_annotation(self, async_mode=async_mode)}]"

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        lro_imports = LROOperation.imports(self, async_mode, is_python3_file)
        paging_imports = PagingOperation.imports(self, async_mode, is_python3_file)

        file_import = lro_imports
        file_import.merge(paging_imports)
        return file_import
