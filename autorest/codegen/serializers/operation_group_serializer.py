# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from .import_serializer import FileImportSerializer
from ..models import LROOperation, PagingOperation, CodeModel, OperationGroup, Operation

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

    def serialize(self) -> str:
        def _is_lro(operation):
            return isinstance(operation, LROOperation)
        def _is_paging(operation):
            return isinstance(operation, PagingOperation)

        operation_group_template = self.env.get_template("operations_container.py.jinja2")
        if self.operation_group.is_empty_operation_group:
            operation_group_template = self.env.get_template("operations_container_mixin.py.jinja2")

        return operation_group_template.render(
            code_model=self.code_model,
            operation_group=self.operation_group,
            imports=FileImportSerializer(self.operation_group.imports(self.async_mode)),
            async_mode=self.async_mode,
            is_lro=_is_lro,
            is_paging=_is_paging,
            operation_typing_comment=OperationGroupSerializer.operation_typing_comment
        )

    def filename(self) -> str:
        basename = self.operation_group.name
        if self.operation_group.is_empty_operation_group:
            basename = self.code_model.module_name
        async_suffix = "_async" if self.async_mode else ""

        return f"_{basename}_operations{async_suffix}.py"

    @staticmethod
    def operation_typing_comment(operation: Operation, lro: bool = False) -> str:
        response = "None"
        if any(r.has_body for r in operation.responses):
            if len(operation.responses) == 1:
                response = operation.responses[0].schema.type_annotation
            else:
                response_parameters_string = ", ".join([
                    r.schema.type_annotation if r.has_body else "None"
                    for r in operation.responses
                ])
                response = f"Union[{response_parameters_string}]"
        if not operation.parameters.method:
            if lro:
                return f"# type: (Optional[Any], Optional[bool], **Any) -> {response}"
            return f"# type: (Optional[Any], **Any) -> {response}"
        parameters_typing = [
            p.schema.type_annotation if p.required else f"Optional[{p.schema.type_annotation}]"
            for p in operation.parameters.method
        ]
        if lro:
            return f"# type: ({', '.join(parameters_typing)}, Optional[Any], Optional[bool], **Any) -> {response}"
        return f"# type: ({', '.join(parameters_typing)}, Optional[Any], **Any) -> {response}"
