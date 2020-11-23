# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import cast, Dict, List, Any, Optional, Set, Union

from .operation import Operation
from .parameter import Parameter
from .schema_response import SchemaResponse
from .schema_request import SchemaRequest
from .imports import ImportType, FileImport, TypingSection
from .object_schema import ObjectSchema
from .primitive_schemas import StringSchema
from .parameter import ParameterLocation

_LOGGER = logging.getLogger(__name__)

def _get_paging_method_import(async_mode):
    file_import = FileImport()
    paging_file = "async_paging" if async_mode else "paging"
    async_prefix = "Async" if async_mode else ""
    file_import.add_from_import(
        f"azure.core.{paging_file}_method", f"{async_prefix}BasicPagingMethod", ImportType.AZURECORE
    )
    return file_import


class PagingOperation(Operation):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        url: str,
        method: str,
        multipart: bool,
        api_versions: Set[str],
        requests: List[SchemaRequest],
        summary: Optional[str] = None,
        parameters: Optional[List[Parameter]] = None,
        multiple_media_type_parameters: Optional[List[Parameter]] = None,
        responses: Optional[List[SchemaResponse]] = None,
        exceptions: Optional[List[SchemaResponse]] = None,
        want_description_docstring: bool = True,
        want_tracing: bool = True,
        *,
        override_success_response_to_200: bool = False
    ) -> None:
        super(PagingOperation, self).__init__(
            yaml_data,
            name,
            description,
            url,
            method,
            multipart,
            api_versions,
            requests,
            summary,
            parameters,
            multiple_media_type_parameters,
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
        self.coroutine_when_async = False
        self.token_param_name = "next_link"

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

    @property
    def item_name(self) -> str:
        if self._item_name is None:
            # Default value. I still check if I find it,  so I can do a nice message.
            item_name = "value"
            try:
                return self._find_python_name(item_name, "itemName")
            except ValueError:
                response = self._get_response()
                raise ValueError(
                    f"While scanning x-ms-pageable, itemName was not defined and object"
                    + f" {response.schema.name} has no array called 'value'"
                )
        return self._find_python_name(self._item_name, "itemName")

    @property
    def next_link_name(self) -> Optional[str]:
        if not self._next_link_name:
            # That's an ok scenario, it just means no next page possible
            return None
        return self._find_python_name(self._next_link_name, "nextLinkName")

    @property
    def has_optional_return_type(self) -> bool:
        """A paging will never have an optional return type, we will always return a pager"""
        return False

    def get_pager_path(self, async_mode: bool) -> str:
        extension_name = "pager-async" if async_mode else "pager-sync"
        return self.yaml_data["extensions"][extension_name]

    def get_pager(self, async_mode: bool) -> str:
        return self.get_pager_path(async_mode).split(".")[-1]

    @property
    def success_status_code(self) -> List[Union[str, int]]:
        """The list of all successfull status code.
        """
        if self.override_success_response_to_200:
            return [200]
        return super(PagingOperation, self).success_status_code

    @property
    def initial_request(self) -> Operation:
        """
        Initial requests will have the URL to make their calls against as the first parameter.
        They will have this parameter if there's no separate next operation, since if there's
        a next operation, the subsequent requests go to that separate next operation.

        Once we add support for token param name not being "next_link", we will still
        insert a next_link parameter for initial requests, but we will add an additional
        parameter before it for the token input param (provided there's no separate next operation)
        """
        parameters = self.parameters.parameters.copy()
        url_initialization = None
        if not self.next_operation:
            schema = StringSchema("", {"type": "str"})
            next_link_param = Parameter(
                schema=schema,
                yaml_data={},
                rest_api_name="next_link",
                serialized_name="next_link",
                description="Parameter to take in url for next call",
                implementation="Method",
                required=True,
                location=ParameterLocation.Other,
                skip_url_encoding=True,
                constraints=[],
            )
            parameters.insert(0, next_link_param)
            url_initialization = "url = next_link"
        return Operation(
            yaml_data={},
            name="_" + self.name + "_initial",
            description="",
            url=self.url,
            method=self.method,
            multipart=self.multipart,
            api_versions=self.api_versions,
            parameters=parameters,
            requests=self.requests,
            responses=self.responses,
            exceptions=self.exceptions,
            want_description_docstring=False,
            want_tracing=False,
            makes_network_call=False,
            url_initialization=url_initialization,
        )

    @property
    def next_request(self) -> Operation:
        next_operation = cast(Operation, self.next_operation)

        # Currently only supported param name is nextLink, will be updated
        # to allow more with tokenParamName support in swagger
        params = next_operation.parameters.parameters
        token_param = [
            param for param in params
            if param.serialized_name == self.token_param_name
        ]
        if token_param:
            # make sure the token param name is first in line, and that it's required.
            # (If the token is empty, we will be exiting before passing it into the next operation)
            token_param[0].required = True
            token_param_index = params.index(token_param[0])
            params.insert(0, params.pop(token_param_index))
        return Operation(
            yaml_data={},
            name="_" + self.name + "_next",
            description="",
            url=next_operation.url,
            method=next_operation.method,
            multipart=next_operation.multipart,
            api_versions=next_operation.api_versions,
            parameters=params,
            requests=next_operation.requests,
            responses=next_operation.responses,
            exceptions=next_operation.exceptions,
            want_description_docstring=False,
            want_tracing=False,
            makes_network_call=False,
        )

    def imports(self, code_model, async_mode: bool) -> FileImport:
        file_import = super(PagingOperation, self).imports(code_model, async_mode)


        async_prefix = "Async" if async_mode else ""

        file_import.merge(_get_paging_method_import(async_mode))
        file_import.add_import("functools", ImportType.STDLIB)

        file_import.add_from_import("typing", f"{async_prefix}Iterable", ImportType.STDLIB, TypingSection.CONDITIONAL)

        if async_mode:
            file_import.add_from_import("azure.core.async_paging", "AsyncList", ImportType.AZURECORE)

        pager_import_path = ".".join(self.get_pager_path(async_mode).split(".")[:-1])
        pager = self.get_pager(async_mode)

        file_import.add_from_import(pager_import_path, pager, ImportType.AZURECORE)

        if code_model.options["tracing"]:
            file_import.add_from_import(
                "azure.core.tracing.decorator", "distributed_trace", ImportType.AZURECORE,
            )

        return file_import
