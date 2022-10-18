# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Optional
import functools
from jinja2 import Environment

from ..models import (
    NamespaceModel,
    OperationGroup,
    FileImport,
)
from .import_serializer import FileImportSerializer
from .builder_serializer import get_operation_serializer, RequestBuilderSerializer


class OperationGroupsSerializer:
    def __init__(
        self,
        namespace_model: NamespaceModel,
        env: Environment,
        async_mode: bool,
        operation_group: Optional[OperationGroup] = None,
    ):
        self.namespace_model = namespace_model
        self.env = env
        self.async_mode = async_mode
        self.operation_group = operation_group

    def serialize(self) -> str:
        operation_groups = (
            [self.operation_group]
            if self.operation_group
            else self.namespace_model.operation_groups
        )
        imports = FileImport()
        for operation_group in operation_groups:
            imports.merge(
                operation_group.imports(
                    async_mode=self.async_mode,
                )
            )

        template = self.env.get_or_select_template(
            "operation_groups_container.py.jinja2"
        )
        return template.render(
            namespace_model=self.namespace_model,
            operation_groups=operation_groups,
            imports=FileImportSerializer(
                imports,
                async_mode=self.async_mode,
            ),
            async_mode=self.async_mode,
            get_operation_serializer=functools.partial(
                get_operation_serializer,
                namespace_model=self.namespace_model,
                async_mode=self.async_mode,
            ),
            request_builder_serializer=RequestBuilderSerializer(
                self.namespace_model,
                async_mode=False,
            ),
            request_builders=[
                rb
                for c in self.namespace_model.clients
                for rb in c.request_builders
                if not rb.abstract
            ],
        )
