# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from jinja2 import Environment
from autorest.codegen.models.operation import Operation

from .import_serializer import FileImportSerializer
from ..models import LROOperation, PagingOperation, CodeModel, OperationGroup
from ..models import LROOperation, PagingOperation, CodeModel, OperationGroup, LROPagingOperation
from .builder_serializer import (
    OperationBaseSerializer,
    SyncOperationSerializer,
    AsyncOperationSerializer,
    SyncPagingOperationSerializer,
    AsyncPagingOperationSerializer,
    SyncLROOperationSerializer,
    AsyncLROOperationSerializer,
    SyncLROPagingOperationSerializer,
    AsyncLROPagingOperationSerializer,
)

class OperationGroupSerializer:
    def __init__(
        self, code_model: CodeModel, env: Environment, operation_group: OperationGroup, async_mode: bool
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.async_mode = async_mode

    def serialize(self) -> str:
        def _is_lro(operation):
            return isinstance(operation, LROOperation)

        def _is_paging(operation):
            return isinstance(operation, PagingOperation)

        def _get_operation_serializer(operation: Operation) -> OperationBaseSerializer:
            if isinstance(operation, LROPagingOperation):
                retcls = AsyncLROPagingOperationSerializer if self.async_mode else SyncLROPagingOperationSerializer
            elif isinstance(operation, LROOperation):
                retcls = AsyncLROOperationSerializer if self.async_mode else SyncLROOperationSerializer
            elif isinstance(operation, PagingOperation):
                retcls = AsyncPagingOperationSerializer if self.async_mode else SyncPagingOperationSerializer
            else:
                retcls = AsyncOperationSerializer if self.async_mode else SyncOperationSerializer
            return retcls(self.code_model)

        operation_group_template = self.env.get_template("operations_container.py.jinja2")
        if self.operation_group.is_empty_operation_group:
            operation_group_template = self.env.get_template("operations_container_mixin.py.jinja2")

        # has_schemas = not self.code_model.no_models and (self.code_model.schemas or self.code_model.enums)
        has_schemas = self.code_model.schemas or self.code_model.enums
        operation_serializer_cls = AsyncOperationSerializer if self.async_mode else SyncOperationSerializer
        paging_operation_serializer_cls = (
            AsyncPagingOperationSerializer if self.async_mode else SyncPagingOperationSerializer
        )
        lro_operation_serializer_cls = AsyncLROOperationSerializer if self.async_mode else SyncLROOperationSerializer
        lro_paging_operation_serializer_cls = (
            AsyncLROPagingOperationSerializer if self.async_mode else SyncLROPagingOperationSerializer
        )

        return operation_group_template.render(
            code_model=self.code_model,
            operation_group=self.operation_group,
            imports=FileImportSerializer(
                self.operation_group.imports(
                    self.async_mode,
                    bool(has_schemas)
                ),
                is_python_3_file=self.async_mode
            ),
            async_mode=self.async_mode,
            operation_serializer=operation_serializer_cls(self.code_model),
            paging_operation_serializer=paging_operation_serializer_cls(self.code_model),
            lro_operation_serializer=lro_operation_serializer_cls(self.code_model),
            lro_paging_operation_serializer=lro_paging_operation_serializer_cls(self.code_model),
            is_lro=_is_lro,
            is_paging=_is_paging,
            get_operation_serializer=_get_operation_serializer,
        )
