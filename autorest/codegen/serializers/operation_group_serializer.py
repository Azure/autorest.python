# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import functools
from copy import copy
from typing import List
from jinja2 import Environment

from .import_serializer import FileImportSerializer
from ..models import LROOperation, PagingOperation, CodeModel, OperationGroup
from .builder_serializer import get_operation_serializer, get_request_builder_serializer


class OperationGroupSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        operation_group: OperationGroup,
        operation_groups: List[OperationGroup],
        async_mode: bool,
        is_python_3_file: bool,
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.operation_groups = operation_groups
        self.async_mode = async_mode
        self.is_python_3_file = is_python_3_file

    def serialize(self) -> str:
        def _is_lro(operation):
            return isinstance(operation, LROOperation)

        def _is_paging(operation):
            return isinstance(operation, PagingOperation)

        operation_group_template = self.env.get_template("operations_container.py.jinja2")
        if self.operation_group and self.operation_group.is_empty_operation_group:
            operation_group_template = self.env.get_template("operations_container_mixin.py.jinja2")

        has_schemas = self.code_model.schemas or self.code_model.enums

        if self.operation_group:
            operation_group_temp = self.operation_group
        else:
            # extract all operations from operation_groups
            operaions_all = [operation for groups in self.operation_groups for operation in groups.operations]
            operation_group_temp = copy(self.operation_groups[0])
            operation_group_temp.operations = operaions_all


        return operation_group_template.render(
            code_model=self.code_model,
            operation_group=self.operation_group,
            operation_groups=self.operation_groups,
            imports=FileImportSerializer(
                operation_group_temp.imports(
                    async_mode=self.async_mode,
                    has_schemas=bool(has_schemas)
                ), is_python_3_file=self.is_python_3_file
            ),
            async_mode=self.async_mode,
            is_python_3_file=self.is_python_3_file,
            is_lro=_is_lro,
            is_paging=_is_paging,
            get_operation_serializer=functools.partial(
                get_operation_serializer,
                code_model=self.code_model,
                async_mode=self.async_mode,
                is_python_3_file=self.is_python_3_file,
            ),
            request_builder_serializer=get_request_builder_serializer(
                self.code_model, self.is_python_3_file,
            ),
        )
