# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import cast, Dict, List, Any, Optional, Set

from .operation import Operation
from .schema_response import SchemaResponse
from .request_builder import RequestBuilder
from .imports import ImportType, FileImport, TypingSection
from .object_schema import ObjectSchema
from .schema_request import SchemaRequest
from .parameter_list import ParameterList

_LOGGER = logging.getLogger(__name__)


class PagingOperation(Operation):
    def __init__(
        self,
        code_model,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        api_versions: Set[str],
        parameters: ParameterList,
        multiple_content_type_parameters: ParameterList,
        schema_requests: List[SchemaRequest],
        summary: Optional[str] = None,
        responses: Optional[List[SchemaResponse]] = None,
        exceptions: Optional[List[SchemaResponse]] = None,
        want_description_docstring: bool = True,
        want_tracing: bool = True,
        *,
        override_success_response_to_200: bool = False
    ) -> None:
        super(PagingOperation, self).__init__(
            code_model,
            yaml_data,
            name,
            description,
            api_versions,
            parameters,
            multiple_content_type_parameters,
            schema_requests,
            summary,
            responses,
            exceptions,
            want_description_docstring,
            want_tracing
        )
        self._item_name: str = yaml_data["extensions"]["x-ms-pageable"].get("itemName")
        self._next_link_name: str = yaml_data["extensions"]["x-ms-pageable"].get("nextLinkName")
        self.operation_name: str = yaml_data["extensions"]["x-ms-pageable"].get("operationName")
        self.next_operation: Optional[Operation] = None
        self.override_success_response_to_200 = override_success_response_to_200

    def _get_response(self) -> SchemaResponse:
        response = self.responses[0]
        if not isinstance(response.schema, ObjectSchema):
            raise ValueError(
                "The response of a paging operation must be of type " + f"ObjectSchema but {response.schema} is not"
            )
        return response

    def _find_python_name(self, rest_api_name: str, log_name: str) -> str:
        response = self._get_response()
        response_schema = cast(ObjectSchema, response.schema)
        if response_schema:
            for prop in response_schema.properties:
                if prop.original_swagger_name == rest_api_name:
                    return prop.name
        raise ValueError(
            f"While scanning x-ms-pageable, was unable to find "
            + f"{log_name}:{rest_api_name} in model {response_schema.name}"
        )

    def _get_paging_extension(self, extension_name):
        return self.yaml_data["extensions"][extension_name]

    def item_name(self, code_model) -> str:
        item_name = self._item_name or "value"
        try:
            return (
                self._find_python_name(item_name, "itemName") if code_model.options["models_mode"]
                else item_name
            )
        except ValueError:
            response = self._get_response()
            raise ValueError(
                f"While scanning x-ms-pageable, itemName was not defined and object"
                + f" {cast(ObjectSchema, response.schema).name} has no array called 'value'"
            )

    @property
    def next_link_name(self) -> Optional[str]:
        if not self._next_link_name:
            # That's an ok scenario, it just means no next page possible
            return None
        if self.code_model.options["models_mode"]:
            return self._find_python_name(self._next_link_name, "nextLinkName")
        return self._next_link_name

    @property
    def has_optional_return_type(self) -> bool:
        """A paging will never have an optional return type, we will always return a pager"""
        return False

    def get_pager_path(self, async_mode: bool) -> str:
        extension_name = "pager-async" if async_mode else "pager-sync"
        return self._get_paging_extension(extension_name)

    def get_pager(self, async_mode: bool) -> str:
        return self.get_pager_path(async_mode).split(".")[-1]

    @property
    def next_request_builder(self) -> Optional[RequestBuilder]:
        if not self.next_operation:
            return None
        next_request_builder = self.next_operation.request_builder
        return next_request_builder

    def _imports_shared(self, async_mode: bool) -> FileImport:
        file_import = super()._imports_shared(async_mode)
        if async_mode:
            file_import.add_submodule_import("typing", "AsyncIterable", ImportType.STDLIB, TypingSection.CONDITIONAL)
        else:
            file_import.add_submodule_import("typing", "Iterable", ImportType.STDLIB, TypingSection.CONDITIONAL)
        if (
            self.next_request_builder and
            self.code_model.options["builders_visibility"] == "embedded"
            and not async_mode
        ):
            file_import.merge(self.next_request_builder.imports())
        return file_import

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = super().imports_for_multiapi(async_mode)
        pager_import_path = ".".join(self.get_pager_path(async_mode).split(".")[:-1])
        pager = self.get_pager(async_mode)

        file_import.add_submodule_import(pager_import_path, pager, ImportType.AZURECORE, TypingSection.CONDITIONAL)

        return file_import

    def imports(self, async_mode: bool) -> FileImport:
        file_import = self._imports_base(async_mode)
        # operation adds an import for distributed_trace_async, we don't want it
        file_import.imports = [i for i in file_import.imports if not i.submodule_name == "distributed_trace_async"]

        pager_import_path = ".".join(self.get_pager_path(async_mode).split(".")[:-1])
        pager = self.get_pager(async_mode)

        file_import.add_submodule_import(pager_import_path, pager, ImportType.AZURECORE)

        if async_mode:
            file_import.add_submodule_import("azure.core.async_paging", "AsyncList", ImportType.AZURECORE)

        if self.code_model.options["tracing"] and self.want_tracing:
            file_import.add_submodule_import(
                "azure.core.tracing.decorator", "distributed_trace", ImportType.AZURECORE,
            )

        return file_import
