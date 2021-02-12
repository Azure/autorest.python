# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import cast, Dict, List, Any, Optional, Union, Set, TypeVar

from .base_model import BaseModel
from .imports import FileImport, ImportType, TypingSection
from .schema_response import SchemaResponse
from .parameter import Parameter
from .parameter_list import ParameterList
from .base_schema import BaseSchema
from .schema_request import SchemaRequest
from .object_schema import ObjectSchema
from .constant_schema import ConstantSchema


_LOGGER = logging.getLogger(__name__)

T = TypeVar('T')
OrderedSet = Dict[T, None]

_M4_HEADER_PARAMETERS = ["content_type", "accept"]

def _non_binary_schema_media_types(media_types: List[str]) -> OrderedSet[str]:
    response_media_types: OrderedSet[str] = {}

    json_media_types = [media_type for media_type in media_types if "json" in media_type]
    xml_media_types = [media_type for media_type in media_types if "xml" in media_type]

    if not sorted(json_media_types + xml_media_types) == sorted(media_types):
        raise ValueError("The non-binary responses with schemas of {self.name} have incorrect json or xml mime types")
    if json_media_types:
        if "application/json" in json_media_types:
            response_media_types["application/json"] = None
        else:
            response_media_types[json_media_types[0]] = None
    if xml_media_types:
        if "application/xml" in xml_media_types:
            response_media_types["application/xml"] = None
        else:
            response_media_types[xml_media_types[0]] = None
    return response_media_types

def _remove_multiple_m4_header_parameters(parameters: List[Parameter]) -> List[Parameter]:
    m4_header_params_in_schema = {
        k: [p for p in parameters if p.serialized_name == k]
        for k in _M4_HEADER_PARAMETERS
    }
    remaining_params = [p for p in parameters if p.serialized_name not in _M4_HEADER_PARAMETERS]
    json_m4_header_params = {
        k: [p for p in m4_header_params_in_schema[k] if p.yaml_data["schema"]["type"] == "constant"]
        for k in m4_header_params_in_schema
    }
    for k, v in json_m4_header_params.items():
        if v:
            remaining_params.append(v[0])
        else:
            remaining_params.append(m4_header_params_in_schema[k][0])

    return remaining_params

class Operation(BaseModel):  # pylint: disable=too-many-public-methods, too-many-instance-attributes
    """Represent an operation.
    """

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
        want_tracing: bool = True
    ) -> None:
        super().__init__(yaml_data)
        self.name = name
        self.description = description
        self.url = url
        self.method = method
        self.multipart = multipart
        self.api_versions = api_versions
        self.requests = requests
        self.summary = summary
        self.parameters = ParameterList(parameters)
        self.multiple_media_type_parameters = ParameterList(multiple_media_type_parameters)
        self.responses = responses or []
        self.exceptions = exceptions or []
        self.want_description_docstring = want_description_docstring
        self.want_tracing = want_tracing

    @property
    def python_name(self) -> str:
        return self.name

    @property
    def request_content_type(self) -> str:
        return next(iter(
            [
                p.schema.get_declaration(cast(ConstantSchema, p.schema).value)
                for p in self.parameters.constant if p.serialized_name == "content_type"
            ]
        ))

    @property
    def is_stream_request(self) -> bool:
        """Is the request is a stream, like an upload."""
        return any(request.is_stream_request for request in self.requests)

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return any(response.is_stream_response for response in self.responses)

    @property
    def any_param_default_to_sentinel(self) -> bool:
        return (
            self.parameters.any_param_default_to_sentinel or
            self.multiple_media_type_parameters.any_param_default_to_sentinel
        )

    @property
    def has_optional_return_type(self) -> bool:
        """Has optional return type if there are multiple successful response types where some have
        bodies and some are None
        """

        # successful status codes of responses that have bodies
        status_codes_for_responses_with_bodies = [
            code for code in self.success_status_code
            if isinstance(code, int) and self.get_response_from_status(code).has_body
        ]

        successful_responses = [
            response for response in self.responses
            if any(code in self.success_status_code for code in response.status_codes)
        ]

        return (
            self.has_response_body and
            len(successful_responses) > 1 and
            len(self.success_status_code) != len(status_codes_for_responses_with_bodies)
        )

    @property
    def serialization_context(self) -> str:
        # FIXME Do the serialization context (XML)
        return ""

    @property
    def has_response_body(self) -> bool:
        """Tell if at least one response has a body.
        """
        return any(response.has_body or response.is_stream_response for response in self.responses)

    def get_response_from_status(self, status_code: int) -> SchemaResponse:
        for response in self.responses:
            if status_code in response.status_codes:
                return response
        raise ValueError(f"Incorrect status code {status_code}, operation {self.name}")

    @property
    def any_response_has_headers(self) -> bool:
        return any(response.has_headers for response in self.responses)

    @property
    def success_status_code(self) -> List[Union[str, int]]:
        """The list of all successfull status code.
        """
        return [code for response in self.responses for code in response.status_codes if code != "default"]

    @property
    def default_exception(self) -> Optional[str]:
        default_excp = [excp for excp in self.exceptions for code in excp.status_codes if code == "default"]
        if not default_excp:
            return None
        excep_schema = default_excp[0].schema
        if isinstance(excep_schema, ObjectSchema):
            return f"_models.{excep_schema.name}"
        # in this case, it's just an AnySchema
        return "\'object\'"


    @property
    def status_code_exceptions(self) -> List[SchemaResponse]:
        return [excp for excp in self.exceptions if list(excp.status_codes) != ["default"]]

    @property
    def status_code_exceptions_status_codes(self) -> List[Union[str, int]]:
        """Actually returns all of the status codes from exceptions (besides default)"""
        return list(chain.from_iterable([
            excp.status_codes for excp in self.status_code_exceptions
        ]))

    def imports(self, code_model, async_mode: bool) -> FileImport:
        file_import = FileImport()

        # Exceptions
        file_import.add_from_import("azure.core.exceptions", "map_error", ImportType.AZURECORE)
        if code_model.options["azure_arm"]:
            file_import.add_from_import("azure.mgmt.core.exceptions", "ARMErrorFormat", ImportType.AZURECORE)
        file_import.add_from_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)
        for parameter in self.parameters:
            file_import.merge(parameter.imports())

        if self.multiple_media_type_parameters:
            for parameter in self.multiple_media_type_parameters:
                file_import.merge(parameter.imports())

        for response in [r for r in self.responses if r.has_body]:
            file_import.merge(cast(BaseSchema, response.schema).imports())

        if len([r for r in self.responses if r.has_body]) > 1:
            file_import.add_from_import("typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL)

        file_import.add_from_import("typing", "Callable", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "Dict", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "TypeVar", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "Generic", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("azure.core.pipeline", "PipelineResponse", ImportType.AZURECORE)
        file_import.add_from_import("azure.core.pipeline.transport", "HttpRequest", ImportType.AZURECORE)
        if async_mode:
            file_import.add_from_import("azure.core.pipeline.transport", "AsyncHttpResponse", ImportType.AZURECORE)
        else:
            file_import.add_from_import("azure.core.pipeline.transport", "HttpResponse", ImportType.AZURECORE)

        # Deprecation
        # FIXME: Replace with "the YAML contains deprecated:true"
        if True:  # pylint: disable=using-constant-test
            file_import.add_import("warnings", ImportType.STDLIB)

        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any]) -> "Operation":
        name = yaml_data["language"]["python"]["name"]
        _LOGGER.debug("Parsing %s operation", name)

        first_request = yaml_data["requests"][0]

        multiple_requests = len(yaml_data["requests"]) > 1

        multiple_media_type_parameters: List[Parameter] = []
        parameters = [Parameter.from_yaml(yaml) for yaml in yaml_data.get("parameters", [])]

        for request in yaml_data["requests"]:
            for yaml in request.get("parameters", []):
                parameter = Parameter.from_yaml(yaml)
                if yaml["language"]["python"]["name"] in _M4_HEADER_PARAMETERS:
                    parameter.is_kwarg = True
                    parameters.append(parameter)
                elif multiple_requests:
                    multiple_media_type_parameters.append(parameter)
                else:
                    parameters.append(parameter)

        if multiple_requests:
            parameters = _remove_multiple_m4_header_parameters(parameters)
            chosen_parameter = multiple_media_type_parameters[0]

            # binary body parameters are required, while object
            # ones are not. We default to optional in this case.
            optional_parameters = [p for p in multiple_media_type_parameters if not p.required]
            if optional_parameters:
                chosen_parameter = optional_parameters[0]
            else:
                chosen_parameter = multiple_media_type_parameters[0]
            chosen_parameter.has_multiple_media_types = True
            parameters.append(chosen_parameter)

        if multiple_media_type_parameters:
            body_parameters_name_set = set(
                p.serialized_name for p in multiple_media_type_parameters
            )
            if len(body_parameters_name_set) > 1:
                raise ValueError(
                f"The body parameter with multiple media types has different names: {body_parameters_name_set}"
            )


        parameters_index = {id(parameter.yaml_data): parameter for parameter in parameters}

        # Need to connect the groupBy and originalParameter
        for parameter in parameters:
            parameter_grouped_by_id = id(parameter.grouped_by)
            if parameter_grouped_by_id in parameters_index:
                parameter.grouped_by = parameters_index[parameter_grouped_by_id]

            parameter_original_id = id(parameter.original_parameter)
            if parameter_original_id in parameters_index:
                parameter.original_parameter = parameters_index[parameter_original_id]

        return cls(
            yaml_data=yaml_data,
            name=name,
            description=yaml_data["language"]["python"]["description"],
            url=first_request["protocol"]["http"]["path"],
            method=first_request["protocol"]["http"]["method"],
            multipart=first_request["protocol"]["http"].get("multipart", False),
            api_versions=set(value_dict["version"] for value_dict in yaml_data["apiVersions"]),
            requests=[SchemaRequest.from_yaml(yaml) for yaml in yaml_data["requests"]],
            summary=yaml_data["language"]["python"].get("summary"),
            parameters=parameters,
            multiple_media_type_parameters=multiple_media_type_parameters,
            responses=[SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("responses", [])],
            # Exception with no schema means default exception, we don't store them
            exceptions=[SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("exceptions", []) if "schema" in yaml],
        )
