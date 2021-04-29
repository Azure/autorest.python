# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any, Set

from .base_model import BaseModel
from .operation import NoModelOperation, Operation
from .lro_operation import LROOperation, NoModelLROOperation
from .paging_operation import NoModelPagingOperation, PagingOperation
from .lro_paging_operation import LROPagingOperation, NoModelLROPagingOperation
from .imports import FileImport, ImportType


_LOGGER = logging.getLogger(__name__)


class OperationGroup(BaseModel):
    """Represent an operation group.

    """
    def __init__(
        self,
        code_model,
        yaml_data: Dict[str, Any],
        name: str,
        class_name: str,
        operations: List[Operation],
        api_versions: Set[str]
    ) -> None:
        super().__init__(yaml_data)
        self.code_model = code_model
        self.name = name
        self.class_name = class_name
        self.operations = operations
        self.api_versions = api_versions

    def imports(self, async_mode: bool, has_schemas: bool) -> FileImport:
        file_import = FileImport()
        file_import.add_from_import("azure.core.exceptions", "ClientAuthenticationError", ImportType.AZURECORE)
        file_import.add_from_import("azure.core.exceptions", "ResourceNotFoundError", ImportType.AZURECORE)
        file_import.add_from_import("azure.core.exceptions", "ResourceExistsError", ImportType.AZURECORE)
        for operation in self.operations:
            file_import.merge(operation.imports(self.code_model, async_mode))
        if self.code_model.options["tracing"]:
            if async_mode:
                file_import.add_from_import(
                    "azure.core.tracing.decorator_async", "distributed_trace_async", ImportType.AZURECORE,
                )
            else:
                file_import.add_from_import(
                    "azure.core.tracing.decorator", "distributed_trace", ImportType.AZURECORE,
                )
        local_path = "..." if async_mode else ".."
        if has_schemas:
            file_import.add_from_import(local_path, "models", ImportType.LOCAL, alias="_models")

        # import request builders
        return file_import

    @property
    def filename(self) -> str:
        basename = self.name
        if self.is_empty_operation_group:
            basename = self.code_model.module_name

        if basename == "operations":
            return f"_operations"
        return f"_{basename}_operations"

    @property
    def is_empty_operation_group(self) -> bool:
        """The operation group with no name is the direct client methods.
        """
        return not self.yaml_data["language"]["default"]["name"]

    @classmethod
    def from_yaml(cls, code_model, yaml_data: Dict[str, Any]) -> "OperationGroup":
        name = yaml_data["language"]["python"]["name"]
        _LOGGER.debug("Parsing %s operation group", name)

        operations = []
        api_versions: Set[str] = set()
        for operation_yaml in yaml_data["operations"]:
            lro_operation = operation_yaml.get("extensions", {}).get("x-ms-long-running-operation")
            paging_operation = operation_yaml.get("extensions", {}).get("x-ms-pageable")
            if lro_operation and paging_operation:
                operation_schema = NoModelLROPagingOperation if code_model.no_models else LROPagingOperation
                operation = operation_schema.from_yaml(operation_yaml)
            elif lro_operation:
                operation_schema = NoModelLROOperation if code_model.no_models else LROOperation
                operation = operation_schema.from_yaml(operation_yaml)
            elif paging_operation:
                operation_schema = NoModelPagingOperation if code_model.no_models else PagingOperation
                operation = operation_schema.from_yaml(operation_yaml)
            else:
                operation_schema = NoModelOperation if code_model.no_models else Operation
                operation = operation_schema.from_yaml(operation_yaml)
            operations.append(operation)
            api_versions.update(operation.api_versions)

        return cls(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            class_name=yaml_data["language"]["python"]["className"],
            operations=operations,
            api_versions=api_versions
        )
