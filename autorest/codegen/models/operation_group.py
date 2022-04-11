# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any, Set, TYPE_CHECKING

from .base_model import BaseModel
from .operation import Operation
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .lro_paging_operation import LROPagingOperation
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


_LOGGER = logging.getLogger(__name__)


def _get_operation(yaml_data: Dict[str, Any], code_model: "CodeModel") -> Operation:
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
    """Represent an operation group."""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        class_name: str,
        operations: List[Operation],
        api_versions: Set[str],
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.name = name
        self.class_name = class_name
        self.operations = operations
        self.api_versions = api_versions

    @property
    def has_abstract_operations(self) -> bool:
        return any(o for o in self.operations if o.abstract)

    def base_class(self, async_mode: bool) -> str:
        base_classes: List[str] = []
        if self.is_empty_operation_group and self.code_model.need_mixin_abc:
            base_classes.append("MixinABC")
        if not (async_mode or self.code_model.options["python3_only"]):
            base_classes.append("object")
        if self.has_abstract_operations:
            base_classes.append("abc.ABC")
        return ", ".join(base_classes)

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = FileImport()
        for operation in self.operations:
            file_import.merge(operation.imports_for_multiapi(async_mode))
        file_import.add_submodule_import(
            ".." if async_mode else ".", "models", ImportType.LOCAL, alias="_models"
        )
        return file_import

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = FileImport()

        for operation in self.operations:
            file_import.merge(operation.imports(async_mode, is_python3_file))
        local_path = "..." if async_mode else ".."
        if self.code_model.has_schemas and self.code_model.options["models_mode"]:
            file_import.add_submodule_import(
                local_path, "models", ImportType.LOCAL, alias="_models"
            )
        if self.code_model.options["builders_visibility"] == "embedded" and async_mode:
            if not self.code_model.options["combine_operation_files"]:
                operation_group_name = (
                    "" if self.is_empty_operation_group else self.name
                )
                operation_group_builders = [
                    r
                    for r in self.code_model.request_builders
                    if r.operation_group_name == operation_group_name
                ]
            else:
                operation_group_builders = self.code_model.request_builders
            for request_builder in operation_group_builders:
                if request_builder.abstract:
                    continue
                python3_only = self.code_model.options["python3_only"]
                typed_sync_operation_file = self.code_model.options[
                    "add_python3_operation_files"
                ]
                suffix = (
                    "_py3" if typed_sync_operation_file and not python3_only else ""
                )
                file_import.add_submodule_import(
                    f"...{self.code_model.operations_folder_name}.{self.filename}{suffix}",
                    request_builder.name,
                    import_type=ImportType.LOCAL,
                )
        if self.code_model.need_mixin_abc:
            file_import.add_submodule_import(".._vendor", "MixinABC", ImportType.LOCAL)
        file_import.add_submodule_import(
            "typing", "TypeVar", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.define_mypy_type("T", "TypeVar('T')")
        type_value = "Optional[Callable[[PipelineResponse[HttpRequest, {}HttpResponse], T, Dict[str, Any]], Any]]"
        file_import.define_mypy_type(
            "ClsType", type_value.format(""), type_value.format("Async")
        )
        return file_import

    @property
    def filename(self) -> str:
        basename = self.name
        if self.is_empty_operation_group:
            basename = self.code_model.module_name

        if (
            basename == "operations"
            or self.code_model.options["combine_operation_files"]
        ):
            return f"_operations"
        return f"_{basename}_operations"

    @property
    def is_empty_operation_group(self) -> bool:
        """The operation group with no name is the direct client methods."""
        return not self.yaml_data["language"]["default"]["name"]

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "OperationGroup":
        name = yaml_data["language"]["python"]["name"]
        _LOGGER.debug("Parsing %s operation group", name)

        operations = []
        api_versions: Set[str] = set()
        for operation_yaml in yaml_data["operations"]:
            operation = _get_operation(operation_yaml, code_model)
            operations.append(operation)
            api_versions.update(operation.api_versions)

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            name=name,
            class_name=yaml_data["language"]["python"]["className"],
            operations=operations,
            api_versions=api_versions,
        )
