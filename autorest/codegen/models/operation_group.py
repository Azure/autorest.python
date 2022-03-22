# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any, Set

from .base_model import BaseModel
from .operation import Operation
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .lro_paging_operation import LROPagingOperation
from .imports import FileImport, ImportType


_LOGGER = logging.getLogger(__name__)

def _get_operation(code_model, yaml_data: Dict[str, Any]) -> Operation:
    lro_operation = yaml_data.get("extensions", {}).get("x-ms-long-running-operation")
    paging_operation = yaml_data.get("extensions", {}).get("x-ms-pageable")
    operation_schema = Operation
    if lro_operation and paging_operation:
        operation_schema = LROPagingOperation
    elif lro_operation:
        operation_schema = LROOperation
    elif paging_operation:
        operation_schema = PagingOperation
    operation = operation_schema.from_yaml(yaml_data, code_model=code_model)
    return operation


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

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = FileImport()
        for operation in self.operations:
            file_import.merge(operation.imports_for_multiapi(async_mode))
        file_import.add_submodule_import(".." if async_mode else ".", "models", ImportType.LOCAL, alias="_models")
        return file_import

    def imports(self, async_mode: bool) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import("azure.core.exceptions", "ClientAuthenticationError", ImportType.AZURECORE)
        file_import.add_submodule_import("azure.core.exceptions", "ResourceNotFoundError", ImportType.AZURECORE)
        file_import.add_submodule_import("azure.core.exceptions", "ResourceExistsError", ImportType.AZURECORE)
        for operation in self.operations:
            file_import.merge(operation.imports(async_mode))
        local_path = "..." if async_mode else ".."
        if self.code_model.has_schemas and self.code_model.options["models_mode"]:
            file_import.add_submodule_import(local_path, "models", ImportType.LOCAL, alias="_models")
        if self.code_model.options["builders_visibility"] == "embedded" and async_mode:
            if not self.code_model.options["combine_operation_files"]:
                operation_group_name = "" if self.is_empty_operation_group else self.name
                operation_group_builders = [
                    r for r in self.code_model.rest.request_builders
                    if r.operation_group_name == operation_group_name
                ]
            else:
                operation_group_builders = self.code_model.rest.request_builders
            for request_builder in operation_group_builders:
                python3_only = self.code_model.options["python3_only"]
                typed_sync_operation_file = self.code_model.options["add_python3_operation_files"]
                suffix = "_py3" if typed_sync_operation_file and not python3_only else ""
                file_import.add_submodule_import(
                    f"...{self.code_model.operations_folder_name}.{self.filename}{suffix}",
                    request_builder.name,
                    import_type=ImportType.LOCAL
                )
        if self.code_model.need_mixin_abc:
            file_import.add_submodule_import(
                ".._vendor", "MixinABC", ImportType.LOCAL
            )
        type_value = "Optional[Callable[[PipelineResponse[HttpRequest, {}HttpResponse], T, Dict[str, Any]], Any]]"
        file_import.define_mypy_type(
            "ClsType",
            type_value.format(""),
            type_value.format("Async")
        )
        return file_import


    @property
    def filename(self) -> str:
        basename = self.name
        if self.is_empty_operation_group:
            basename = self.code_model.module_name

        if basename == "operations" or self.code_model.options["combine_operation_files"]:
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
            operation = _get_operation(code_model, operation_yaml)
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
