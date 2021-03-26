# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import cast, Dict, List, Any, Optional, Union, Set

from .base_model import BaseModel
from .imports import FileImport, ImportType, TypingSection
from .schema_response import SchemaResponse
from .parameter import Parameter
from .parameter_list import ParameterList
from .base_schema import BaseSchema
from .object_schema import ObjectSchema
from .preparer import Preparer
from .utils import get_converted_parameters


_LOGGER = logging.getLogger(__name__)

class Operation(BaseModel):  # pylint: disable=too-many-public-methods, too-many-instance-attributes
    """Represent an operation.
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        api_versions: Set[str],
        parameters: ParameterList,
        multiple_media_type_parameters: ParameterList,
        summary: Optional[str] = None,
        responses: Optional[List[SchemaResponse]] = None,
        exceptions: Optional[List[SchemaResponse]] = None,
        want_description_docstring: bool = True,
        want_tracing: bool = True
    ) -> None:
        super().__init__(yaml_data)
        self.name = name
        self.description = description
        self.api_versions = api_versions
        self.parameters = parameters
        self.multiple_media_type_parameters = multiple_media_type_parameters
        self.summary = summary
        self.responses = responses or []
        self.exceptions = exceptions or []
        self.want_description_docstring = want_description_docstring
        self.want_tracing = want_tracing
        self._preparer: Optional[Preparer] = None

    @property
    def default_content_type_declaration(self) -> str:
        return f'"{self.parameters.default_content_type}"'

    @property
    def python_name(self) -> str:
        return self.name

    @property
    def preparer(self) -> Preparer:
        if not self._preparer:
            raise ValueError(
                "You're calling preparer when you haven't linked up operation to its "
                "request preparer through the code model"
            )
        return self._preparer

    @preparer.setter
    def preparer(self, r: Preparer) -> None:
        self._preparer = r

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return any(response.is_stream_response for response in self.responses)

    @property
    def body_kwarg_to_pass_to_preparer(self) -> str:
        if self.preparer.multipart:
            return "files"
        elif self.parameters.has_partial_body:
            return "data"
        return "content"

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
        # in this case, it's just an AnyObjectSchema
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

        for param in self.parameters.method:
            file_import.merge(param.imports())

        for param in self.multiple_media_type_parameters:
            file_import.merge(param.imports())

        for response in [r for r in self.responses if r.has_body]:
            file_import.merge(cast(BaseSchema, response.schema).imports())

        if len([r for r in self.responses if r.has_body]) > 1:
            file_import.add_from_import("typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL)

        for schema_request in self.preparer.schema_requests:
            if any([c for c in schema_request.pre_semicolon_media_types if "application/json" in c]):
                file_import.add_import("json", ImportType.STDLIB)

        file_import.add_from_import("typing", "Callable", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "Dict", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "TypeVar", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("typing", "Generic", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import("azure.core.pipeline", "PipelineResponse", ImportType.AZURECORE)
        file_import.add_from_import("azure.core.rest", "HttpRequest", ImportType.AZURECORE)
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

        parameters, multiple_media_type_parameters = get_converted_parameters(yaml_data, Parameter.from_yaml)

        return cls(
            yaml_data=yaml_data,
            name=name,
            description=yaml_data["language"]["python"]["description"],
            api_versions=set(value_dict["version"] for value_dict in yaml_data["apiVersions"]),
            parameters=ParameterList(parameters),
            multiple_media_type_parameters=ParameterList(multiple_media_type_parameters),
            summary=yaml_data["language"]["python"].get("summary"),
            responses=[SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("responses", [])],
            # Exception with no schema means default exception, we don't store them
            exceptions=[SchemaResponse.from_yaml(yaml) for yaml in yaml_data.get("exceptions", []) if "schema" in yaml],
        )
