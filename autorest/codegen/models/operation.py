# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import cast, Dict, List, Any, Optional, Union, Set

from .base_model import BaseModel
from .imports import FileImport, ImportType
from .schema_response import SchemaResponse
from .parameter import Parameter, ParameterStyle
from .parameter_list import ParameterList
from .base_schema import BaseSchema
from .schema_request import SchemaRequest


_LOGGER = logging.getLogger(__name__)


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
        api_versions: Set[str],
        requests: List[SchemaRequest],
        summary: Optional[str] = None,
        parameters: Optional[List[Parameter]] = None,
        multiple_media_type_parameters: Optional[List[Parameter]] = None,
        responses: Optional[List[SchemaResponse]] = None,
        exceptions: Optional[List[SchemaResponse]] = None,
        want_description_docstring: Optional[bool] = True,
        want_tracing: Optional[bool] = True,
    ) -> None:
        super().__init__(yaml_data)
        self.name = name
        self.description = description
        self.url = url
        self.method = method
        self.api_versions = api_versions
        self.requests = requests
        self.summary = summary
        self.parameters = ParameterList(parameters)
        self.multiple_media_type_parameters = multiple_media_type_parameters
        self.responses = responses or []
        self.exceptions = exceptions or []
        self.want_description_docstring = want_description_docstring
        self.want_tracing = want_tracing

    @property
    def python_name(self) -> str:
        return self.name

    @staticmethod
    def _suggest_content_type(media_types: List[str], list_all_if_not_found: bool) -> str:
        """Return the prefered media-type.

        Assumes "media_types" attributes as a list exist.
        """
        if len(media_types) == 1:
            return media_types[0]

        if "application/json" in media_types:
            return "application/json"
        # If more type are supported, if JSON is supported, ask JSON only
        for media_type in media_types:
            if "json" in media_type:
                return media_type
        # If no JSON, and still several content type, chain them
        if list_all_if_not_found:
            return ",".join(media_types)
        return media_types[0]

    @property
    def accept_content_type(self) -> str:
        media_types = set(media_type for response in self.responses for media_type in response.media_types)
        return self._suggest_content_type(list(media_types), list_all_if_not_found=True)

    @property
    def request_content_type(self) -> str:
        media_types = set(media_type for request in self.requests for media_type in request.media_types)
        return self._suggest_content_type(list(media_types), list_all_if_not_found=False)

    @property
    def is_stream_request(self) -> bool:
        """Is the request is a stream, like an upload."""
        return any(request.is_stream_request for request in self.requests)

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return any(response.is_stream_response for response in self.responses)

    @staticmethod
    def build_serialize_data_call(parameter: Parameter, function_name: str) -> str:

        optional_parameters = []

        if parameter.skip_url_encoding:
            optional_parameters.append("skip_quote=True")

        if parameter.style:
            if parameter.style in [ParameterStyle.simple, ParameterStyle.form]:
                div_char = ","
            elif parameter.style in [ParameterStyle.spaceDelimited]:
                div_char = " "
            elif parameter.style in [ParameterStyle.pipeDelimited]:
                div_char = "|"
            elif parameter.style in [ParameterStyle.tabDelimited]:
                div_char = "\t"
            else:
                raise ValueError(f"Do not support {parameter.style} yet")
            optional_parameters.append(f"div='{div_char}'")

        serialization_constraints = parameter.schema.serialization_constraints
        optional_parameters += serialization_constraints if serialization_constraints else ""

        optional_parameters_string = "" if not optional_parameters else ", " + ", ".join(optional_parameters)

        origin_name = parameter.full_serialized_name

        return (
            f"""self._serialize.{function_name}("{origin_name.lstrip('_')}", {origin_name}, """
            + f"""'{parameter.schema.serialization_type}'{optional_parameters_string})"""
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
    def default_exception(self) -> Optional[SchemaResponse]:
        default_excp = [excp for excp in self.exceptions for code in excp.status_codes if code == "default"]
        if default_excp:
            return default_excp[0]
        return None

    @property
    def status_code_exceptions(self) -> List[SchemaResponse]:
        return [excp for excp in self.exceptions if list(excp.status_codes) != ["default"]]

    def imports(self, code_model, async_mode: bool) -> FileImport:
        file_import = FileImport()

        # Exceptions
        file_import.add_from_import("azure.core.exceptions", "map_error", ImportType.AZURECORE)
        if not self.default_exception:
            if code_model.options["azure_arm"]:
                file_import.add_from_import("azure.mgmt.core.exceptions", "ARMError", ImportType.AZURECORE)
            else:
                file_import.add_from_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)
        for parameter in self.parameters:
            file_import.merge(parameter.imports())

        for response in [r for r in self.responses if r.has_body]:
            file_import.merge(cast(BaseSchema, response.schema).imports())

        if len([r for r in self.responses if r.has_body]) > 1:
            file_import.add_from_import("typing", "Union", ImportType.STDLIB)

        file_import.add_from_import("typing", "Callable", ImportType.STDLIB)
        file_import.add_from_import("typing", "Optional", ImportType.STDLIB)
        file_import.add_from_import("typing", "Dict", ImportType.STDLIB)
        file_import.add_from_import("typing", "Any", ImportType.STDLIB)
        file_import.add_from_import("typing", "TypeVar", ImportType.STDLIB)
        file_import.add_from_import("typing", "Generic", ImportType.STDLIB)
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

        # Models
        if self.parameters.has_body or self.has_response_body or self.exceptions:
            if async_mode:
                file_import.add_from_import("...", "models", ImportType.LOCAL)
            else:
                file_import.add_from_import("..", "models", ImportType.LOCAL)

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
                if yaml["language"]["python"]["name"] == "content_type":
                    parameter.is_kwarg = True
                    parameters.append(parameter)
                elif multiple_requests:
                    multiple_media_type_parameters.append(parameter)

        if multiple_requests:
            chosen_parameter = multiple_media_type_parameters[0]
            chosen_parameter.has_multiple_media_types = True
            parameters.append(chosen_parameter)

        else:
            parameters += [
                Parameter.from_yaml(yaml)
                for yaml in first_request.get("parameters", [])
            ]

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
            api_versions=set(value_dict["version"] for value_dict in yaml_data["apiVersions"]),
            requests=[SchemaRequest.from_yaml(yaml) for yaml in yaml_data["requests"]],
            summary=yaml_data["language"]["python"].get("summary"),
            parameters=parameters,
            multiple_media_type_parameters=multiple_media_type_parameters,
            responses=[SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("responses", [])],
            # Exception with no schema means default exception, we don't store them
            exceptions=[SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("exceptions", []) if "schema" in yaml],
        )
