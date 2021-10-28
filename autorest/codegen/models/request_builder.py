# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, TypeVar, Optional

from .base_builder import BaseBuilder, create_parameters
from .request_builder_parameter import RequestBuilderParameter
from .request_builder_parameter_list import RequestBuilderParameterList
from .schema_request import SchemaRequest
from .schema_response import SchemaResponse
from .imports import FileImport, ImportType, TypingSection
from .parameter import Parameter


T = TypeVar('T')
OrderedSet = Dict[T, None]

class RequestBuilder(BaseBuilder):
    def __init__(
        self,
        code_model,
        yaml_data: Dict[str, Any],
        name: str,
        url: str,
        method: str,
        multipart: bool,
        schema_requests: List[SchemaRequest],
        parameters: RequestBuilderParameterList,
        description: str,
        summary: str,
        responses: Optional[List[SchemaResponse]] = None,
    ):
        super().__init__(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            description=description,
            parameters=parameters,
            responses=responses,
            schema_requests=schema_requests,
            summary=summary,
        )
        self.url = url
        self.method = method
        self.multipart = multipart

    @property
    def is_stream(self) -> bool:
        """Is the request we're preparing a stream, like an upload."""
        return any(request.is_stream_request for request in self.schema_requests)

    @property
    def body_kwargs_to_get(self) -> List[Parameter]:
        return self.parameters.body_kwargs_to_get

    @property
    def operation_group_name(self) -> str:
        return self.yaml_data["language"]["python"]["operationGroupName"]

    @property
    def builder_group_name(self) -> str:
        return self.yaml_data["language"]["python"]["builderGroupName"]

    def imports(self) -> FileImport:
        file_import = FileImport()
        for parameter in self.parameters:
            file_import.merge(parameter.imports())

        file_import.add_from_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
        )
        if self.parameters.path:
            relative_path = ".."
            if not self.code_model.options["builders_visibility"] == "embedded" and self.operation_group_name:
                relative_path = "..." if self.operation_group_name else ".."
            file_import.add_from_import(
                f"{relative_path}_vendor", "_format_url_section", ImportType.LOCAL
            )
        file_import.add_from_import(
            "typing", "Any", ImportType.STDLIB, typing_section=TypingSection.CONDITIONAL
        )
        file_import.add_from_import("msrest", "Serializer", ImportType.AZURECORE)
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], *, code_model) -> "RequestBuilder":

        # when combine embeded builders into one operation file, we need to avoid duplicated build function name.
        # So add operation group name is effective method
        additional_mark = ""
        if code_model.options["combine_operation_files"] and code_model.options["builders_visibility"] == "embedded":
            additional_mark = yaml_data["language"]["python"]["builderGroupName"]
        names = [
            "build",
            additional_mark,
            yaml_data["language"]["python"]["name"],
            "request"
        ]
        name = "_".join([n for n in names if n])

        first_request = yaml_data["requests"][0]
        schema_requests = [SchemaRequest.from_yaml(yaml, code_model=code_model) for yaml in yaml_data["requests"]]
        parameters, multiple_content_type_parameters = (
            create_parameters(yaml_data, code_model, RequestBuilderParameter.from_yaml)
        )
        parameter_list = RequestBuilderParameterList(
            code_model, parameters + multiple_content_type_parameters, schema_requests
        )
        request_builder_class = cls(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            url=first_request["protocol"]["http"]["path"],
            method=first_request["protocol"]["http"]["method"].upper(),
            multipart=first_request["protocol"]["http"].get("multipart", False),
            schema_requests=schema_requests,
            parameters=parameter_list,
            description=yaml_data["language"]["python"]["description"],
            responses=[SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("responses", [])],
            summary=yaml_data["language"]["python"].get("summary"),
        )
        code_model.request_builder_ids[id(yaml_data)] = request_builder_class
        parameter_list.add_body_kwargs()
        return request_builder_class
