# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any, Optional, Union

from .base_model import BaseModel
from .imports import FileImport, ImportType
from .schema_response import SchemaResponse
from .parameter import Parameter, ParameterLocation, ParameterStyle
from .constant_schema import ConstantSchema


_LOGGER = logging.getLogger(__name__)


class Operation(BaseModel):  # pylint: disable=too-many-public-methods
    """Represent an operation.
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        url: str,
        method: str,
        parameters: List[Parameter] = None,
        responses: List[SchemaResponse] = None,
        exceptions: List[SchemaResponse] = None,
        media_types: List[str] = None,
        want_description_docstring: Optional[bool] = True,
        want_tracing: Optional[bool] = True
    ) -> None:
        super().__init__(yaml_data)
        if responses is None:
            responses = []
        if exceptions is None:
            exceptions = []
        if media_types is None:
            media_types = []

        self.name = name
        self.description = description
        self.url = url
        self.method = method
        self.parameters = parameters
        self.responses = responses
        self.exceptions = exceptions
        self.media_types = media_types
        self.want_description_docstring = want_description_docstring
        self.want_tracing = want_tracing

    @property
    def python_name(self):
        return self.name

    @staticmethod
    def _suggest_content_type(
        media_types: List[str]
    ) -> str:
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
        return ",".join(media_types)

    @property
    def accept_content_type(self):
        media_types = set(
            media_type
            for response in self.responses
            for media_type in response.media_types
        )
        return self._suggest_content_type(list(media_types))

    @property
    def request_content_type(self):
        return self._suggest_content_type(self.media_types)

    @property
    def is_stream_request(self):
        """Is the request is a stream, like an upload."""
        # FIXME look for input
        return False

    @property
    def is_stream_response(self):
        """Is the response expected to be streamable, like a download."""
        return any(response.is_stream_response for response in self.responses)

    @property
    def has_request_body(self):
        return any(parameter.location == ParameterLocation.Body for parameter in self.parameters)

    @property
    def body_parameter(self) -> Parameter:
        if not self.has_request_body or not self.parameters:
            raise ValueError(f"There are no body parameters for operation {self.name}")
        # Should we check if there is two body? Modeler role right?
        return [
            parameter for parameter in self.parameters if parameter.location == ParameterLocation.Body
        ][0]

    @property
    def path_parameters(self) -> List[Parameter]:
        if not self.parameters:
            raise ValueError(f"There are no path parameters for operation {self.name}")
        return [
            parameter for parameter in self.parameters
            if parameter.location in [ParameterLocation.Uri, ParameterLocation.Path] and
            parameter.rest_api_name != "$host"
        ]

    @property
    def query_parameters(self) -> List[Parameter]:
        if not self.parameters:
            raise ValueError(f"There are no query parameters for operation {self.name}")
        return [
            parameter for parameter in self.parameters if parameter.location == ParameterLocation.Query
        ]

    @property
    def headers_parameters(self) -> List[Parameter]:
        if not self.parameters:
            raise ValueError(f"There are no header parameters for operation {self.name}")
        return [
            parameter for parameter in self.parameters if parameter.location == ParameterLocation.Header
        ]

    @property
    def constant_parameters(self) -> List[Parameter]:
        if not self.parameters:
            raise ValueError(f"There are no constant parameters for operation {self.name}")
        return [
            parameter for parameter in self.parameters if isinstance(parameter.schema, ConstantSchema)
        ]

    @property
    def method_parameters(self) -> List[Parameter]:
        """The list of parameter used in method signature.
        """
        def is_parameter_in_signature(parameter):
            """A predicate to tell if this parmater deserves to be in the signature.
            """
            return not (isinstance(parameter.schema, ConstantSchema) or parameter.implementation == "Client")
        if not self.parameters:
            raise ValueError(f"There are no method parameters for operation {self.name}")
        signature_parameters_required = []
        signature_parameters_optional = []
        for parameter in self.parameters:
            if is_parameter_in_signature(parameter):
                if parameter.is_required:
                    signature_parameters_required.append(parameter)
                else:
                    signature_parameters_optional.append(parameter)

        signature_parameters = signature_parameters_required + signature_parameters_optional
        if self.is_flattened:
            signature_parameters.remove(self.body_parameter)
        return signature_parameters

    @staticmethod
    def build_serialize_data_call(parameter: Parameter, function_name: str) -> str:

        optional_parameters = []

        if parameter.skip_url_encoding:
            optional_parameters.append("skip_quote=True")

        if parameter.style:
            if parameter.style in [ParameterStyle.simple, ParameterStyle.form]:
                div_char = ','
            elif parameter.style in [ParameterStyle.spaceDelimited]:
                div_char = ' '
            elif parameter.style in [ParameterStyle.pipeDelimited]:
                div_char = '|'
            elif parameter.style in [ParameterStyle.tabDelimited]:
                div_char = '\t'
            else:
                raise ValueError(f"Do not support {parameter.style} yet")
            optional_parameters.append(f"div='{div_char}'")

        serialization_constraints = parameter.schema.get_serialization_constraints()
        optional_parameters += serialization_constraints if serialization_constraints else ""

        optional_parameters_string = "" if not optional_parameters else ", " + ", ".join(optional_parameters)

        origin_name = parameter.full_serialized_name

        return (f"""self._serialize.{function_name}("{origin_name}", {origin_name}, """ +
        f"""'{parameter.schema.get_serialization_type()}'{optional_parameters_string})""")

    @property
    def serialization_context(self):
        # FIXME Do the serialization context (XML)
        return ""

    @property
    def has_response_body(self):
        """Tell if at least one response has a body.
        """
        return any(response.has_body or response.is_stream_response for response in self.responses)

    def get_response_from_status(self, status_code: int) -> SchemaResponse:
        for response in self.responses:
            if status_code in response.status_codes:
                return response
        raise ValueError(f"Incorrect status code {status_code}, operation {self.name}")

    @property
    def any_response_has_headers(self):
        return any(response.has_headers for response in self.responses)

    @property
    def success_status_code(self) -> List[Union[str, int]]:
        """The list of all successfull status code.
        """
        return [
            code
            for response in self.responses
            for code in response.status_codes
            if code != "default"
        ]

    @property
    def default_exception(self) -> SchemaResponse:
        default_excp = [
            excp
            for excp in self.exceptions
            for code in excp.status_codes
            if code == "default"
        ]
        if default_excp:
            return default_excp[0]
        return None

    @property
    def status_code_exceptions(self) -> List[SchemaResponse]:
        return [
            excp
            for excp in self.exceptions
            if list(excp.status_codes) != ["default"]
        ]

    def imports(self, code_model, async_mode):
        file_import = FileImport()

        # Exceptions
        file_import.add_from_import(
            "azure.core.exceptions", "map_error", ImportType.AZURECORE
        )
        if not self.default_exception:
            if code_model.options['azure_arm']:
                file_import.add_from_import("azure.mgmt.core.exceptions", "ARMError", ImportType.AZURECORE)
            else:
                file_import.add_from_import(
                    "azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE
                )

        # If ARM, I always generated a client request id
        if code_model.options['azure_arm']:
            file_import.add_import("uuid", ImportType.STDLIB)

        # Deprecation
        # FIXME: Replace with "the YAML contains deprecated:true"
        if True:  # pylint: disable=using-constant-test
            file_import.add_import("warnings", ImportType.STDLIB)

        # Models
        if self.has_request_body or self.has_response_body or self.exceptions:
            if async_mode:
                file_import.add_from_import("...", "models", ImportType.LOCAL)
            else:
                file_import.add_from_import("..", "models", ImportType.LOCAL)

        return file_import

    @property
    def method_signature(self):

        signature = ", ".join([
            parameter.for_method_signature for parameter in self.method_parameters
        ])
        if signature:
            signature = ", "+signature
        return signature

    @property
    def is_flattened(self):
        return bool([
            parameter for parameter in self.parameters if parameter.location == ParameterLocation.Other
        ])

    def build_flattened_object(self):
        if not self.is_flattened:
            raise ValueError("This method can't be called if the operation doesn't need parameter flattening")

        parameters = [
            parameter for parameter in self.parameters if parameter.location == ParameterLocation.Other
        ]
        parameter_string = ",".join([f"{param.serialized_name}={param.serialized_name}" for param in parameters])

        return f"{self.body_parameter.serialized_name} = models.{self.body_parameter.schema.name}({parameter_string})"

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any]) -> "Operation":
        name = yaml_data["language"]["python"]["name"]
        _LOGGER.debug("Parsing %s operation", name)

        return cls(
            yaml_data=yaml_data,
            name=name,
            description=yaml_data["language"]["python"]["description"],
            url=yaml_data["request"]["protocol"]["http"]["path"],
            method=yaml_data["request"]["protocol"]["http"]["method"],
            parameters=[
                Parameter.from_yaml(yaml)
                for yaml in yaml_data["request"].get("parameters", [])
            ],
            responses=[
                SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("responses", [])
            ],
            # Exception with no schema means default exception, we don't store them
            exceptions=[
                SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("exceptions", []) if "schema" in yaml
            ],
            media_types=yaml_data["request"]["protocol"]["http"].get("mediaTypes", [])
        )
