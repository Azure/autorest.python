# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from .import_serializer import FileImportSerializer
from ..models import LROOperation, PagingOperation, CodeModel, OperationGroup

class OperationGroupSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        operation_group: OperationGroup,
        async_mode: bool
    ):
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.async_mode = async_mode
        self._operation_group_file: str = ""

    def serialize(self) -> None:
        def _is_lro(operation):
            return isinstance(operation, LROOperation)
        def _is_paging(operation):
            return isinstance(operation, PagingOperation)

        operation_group_template = self.env.get_template("operations_container.py.jinja2")
        self.env.globals.update(is_lro=_is_lro, is_paging=_is_paging)
        if self.operation_group.is_empty_operation_group:
            operation_group_template = self.env.get_template("operations_container_mixin.py.jinja2")

        self._operation_group_file = operation_group_template.render(
            code_model=self.code_model,
            operation_group=self.operation_group,
            imports=FileImportSerializer(self.operation_group.imports(self.async_mode)),
            async_mode=self.async_mode
        )

    def filename(self) -> str:
        basename = self.operation_group.name
        if self.operation_group.is_empty_operation_group:
            basename = self.code_model.module_name
        async_suffix = "_async" if self.async_mode else ""

        return f"_{basename}_operations{async_suffix}.py"

    @property
    def operation_group_file(self) -> str:
        return self._operation_group_file
