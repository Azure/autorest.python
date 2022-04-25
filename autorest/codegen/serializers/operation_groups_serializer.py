# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Optional
import functools
from jinja2 import Environment

from ..models import (
    CodeModel,
    OperationGroup,
    FileImport,
    LROOperation,
    PagingOperation,
)
from .import_serializer import FileImportSerializer
from .builder_serializer import get_operation_serializer, RequestBuilderSerializer


class OperationGroupsSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        async_mode: bool,
        is_python3_file: bool,
        operation_group: Optional[OperationGroup] = None,
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.async_mode = async_mode
        self.is_python3_file = is_python3_file
        self.operation_group = operation_group

    def serialize(self) -> str:
        def _is_lro(operation):
            return isinstance(operation, LROOperation)

        def _is_paging(operation):
            return isinstance(operation, PagingOperation)

        operation_groups = (
            [self.operation_group]
            if self.operation_group
            else self.code_model.operation_groups
        )
        imports = FileImport()
        for operation_group in operation_groups:
            imports.merge(
                operation_group.imports(
                    async_mode=self.async_mode,
                    is_python3_file=self.is_python3_file,
                )
            )

        template = self.env.get_or_select_template(
            "operation_groups_container.py.jinja2"
        )
        return template.render(
            code_model=self.code_model,
            operation_groups=operation_groups,
            imports=FileImportSerializer(
                imports,
                is_python3_file=self.is_python3_file,
                async_mode=self.async_mode,
            ),
            async_mode=self.async_mode,
            is_python3_file=self.is_python3_file,
            is_lro=_is_lro,
            is_paging=_is_paging,
            get_operation_serializer=functools.partial(
                get_operation_serializer,
                code_model=self.code_model,
                async_mode=self.async_mode,
                is_python3_file=self.is_python3_file,
            ),
            request_builder_serializer=RequestBuilderSerializer(
                self.code_model,
                async_mode=False,
                is_python3_file=self.is_python3_file,
            ),
        )
