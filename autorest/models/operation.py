# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Union, Iterable, Any

from ..common.utils import get_method_name
from .imports import FileImport, ImportType
from .schema_response import SchemaResponse
from .parameter import Parameter, ParameterLocation


_LOGGER = logging.getLogger(__name__)


class Operation:
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
    ) -> None:
        if responses is None:
            responses = []
        if exceptions is None:
            exceptions = []
        if media_types is None:
            media_types = []

        self.yaml_data = yaml_data
        self.name = name
        self.description = description
        self.url = url
        self.method = method
        self.parameters = parameters
        self.responses = responses
        self.exceptions = exceptions
        self.media_types = media_types

    @property
    def python_name(self):
        return get_method_name(self.name)

    @staticmethod
    def _suggest_content_type(
        media_types: List[str]
    ) -> str:
        """Return the prefered media-type.

        Assumes "media_types" attributes as a list exist.
        """
        if len(media_types) == 1:
            return media_types[0]

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
        # FIXME look for input
        return False

    @property
    def has_request_body(self):
        return any(parameter.location == ParameterLocation.Body for parameter in self.parameters)

    @property
    def body_parameter(self) -> Parameter:
        if not self.has_request_body:
            raise ValueError(f"There is body parameter for operation {self.name}")
        # Should we check if there is two body? Modeler role right?
        return [
            parameter for parameter in self.parameters if parameter.location == ParameterLocation.Body
        ][0]

    @property
    def query_parameters(self) -> List[Parameter]:
        return [
            parameter for parameter in self.parameters if parameter.location == ParameterLocation.Query
        ]

    @property
    def headers_parameters(self) -> List[Parameter]:
        return [
            parameter for parameter in self.parameters if parameter.location == ParameterLocation.Header
        ]

    @staticmethod
    def build_constraints(constraints: List) -> List[str]:
        constraints_params = []
        for constraint in constraints:
            pass
        return constraints_params

    @staticmethod
    def build_serialize_data_call(parameter: Parameter, function_name: str) -> str:

        optional_parameters = []

        if parameter.skip_url_encoding:
            optional_parameters.append("skip_quote=True")

        if False: # FIXME divChar = ClientModelExtensions.NeedsFormattedSeparator(parameter);
            div_char = '?'
            optional_parameters.append(f"div='{div_char}'")

        optional_parameters += Operation.build_constraints(parameter.constraints)

        optional_parameters_string = "" if not optional_parameters else "," + ", ".join(optional_parameters)

        return f"""self._serialize.{function_name}("{parameter.serialized_name}", {parameter.serialized_name}, '{parameter.schema.get_serialization_type()}'{optional_parameters_string})"""

    @property
    def serialization_context(self):
        # FIXME Do the serialization context (XML)
        return ""

    @property
    def has_response_body(self):
        """Tell if at least one response has a body.
        """
        return any(response.has_body for response in self.responses)

    def get_response_from_status(self, status_code: int) -> SchemaResponse:
        for response in self.responses:
            if status_code in response.status_codes:
                return response
        raise ValueError(f"Incorrect status code {status_code}, operation {self.name}")

    @property
    def any_response_has_headers(self):
        return any(response.headers for response in self.responses)

    @property
    def success_status_code(self) -> List[int]:
        """The list of all successfull status code.
        """
        return [
            code
            for response in self.responses
            for code in response.status_codes
            if code != "default"
        ]

    def imports(self):
        file_import = FileImport()

        # Exceptions
        file_import.add_from_import(
            "azure.core.exceptions", "map_error", ImportType.AZURECORE
        )
        if not self.exceptions:
            file_import.add_from_import(
                "azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE
            )

        # Tracings
        if True:  # Replace with "--tracing was passed to autorest"
            file_import.add_from_import(
                "azure.core.tracing.decorator",
                "distributed_trace",
                ImportType.AZURECORE,
            )

        # Deprecation
        if True:  # Replace with "the YAML contains deprecated:true"
            file_import.add_import("warnings", ImportType.STDLIB)

        # Models
        if self.has_request_body or self.has_response_body:
            file_import.add_from_import("..", "models", ImportType.LOCAL)

        return file_import

    @property
    def method_signature(self):
        signature = ", ".join([
            parameter.for_method_signature for parameter in self.parameters
        ])
        if signature:
            signature = ", "+signature
        return signature

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "Operation":
        name = yaml_data["language"]["default"]["name"]
        _LOGGER.info("Parsing %s operation", name)
        return cls(
            yaml_data=yaml_data,
            name=name,
            description=yaml_data["language"]["default"]["description"],
            url=yaml_data["request"]["protocol"]["http"]["path"],
            method=yaml_data["request"]["protocol"]["http"]["method"],
            parameters=[
                Parameter.from_yaml(yaml)
                for yaml in yaml_data["request"].get("parameters", [])
            ],
            responses=[
                SchemaResponse.from_yaml(yaml) for yaml in yaml_data["responses"]
            ],
            exceptions=[
                SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("exceptions", [])
            ],
            media_types=yaml_data["request"]["protocol"]["http"].get("mediaTypes", []),
        )
