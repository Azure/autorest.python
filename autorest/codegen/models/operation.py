# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import cast, Dict, List, Any, Optional, Union, Set

from .base_builder import BaseBuilder, create_parameters
from .imports import FileImport, ImportType, TypingSection
from .schema_response import SchemaResponse
from .parameter import Parameter, get_parameter, ParameterLocation
from .parameter_list import ParameterList, get_parameter_list
from .base_schema import BaseSchema
from .object_schema import ObjectSchema
from .request_builder import RequestBuilder
from .schema_request import SchemaRequest
from .primitive_schemas import IOSchema

_LOGGER = logging.getLogger(__name__)

class Operation(BaseBuilder):  # pylint: disable=too-many-public-methods, too-many-instance-attributes
    """Represent an self.
    """

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
    ) -> None:
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
        self.multiple_content_type_parameters = multiple_content_type_parameters
        self.api_versions = api_versions
        self.multiple_content_type_parameters = multiple_content_type_parameters
        self.exceptions = exceptions or []
        self.want_description_docstring = want_description_docstring
        self.want_tracing = want_tracing
        self._request_builder: Optional[RequestBuilder] = None
        self.deprecated = False

    @property
    def python_name(self) -> str:
        return self.name

    @property
    def request_builder(self) -> RequestBuilder:
        if not self._request_builder:
            raise ValueError(
                "You're calling request_builder when you haven't linked up operation to its "
                "request builder through the code model"
            )
        return self._request_builder

    @request_builder.setter
    def request_builder(self, r: RequestBuilder) -> None:
        self._request_builder = r

    @property
    def is_stream_response(self) -> bool:
        """Is the response expected to be streamable, like a download."""
        return any(response.is_stream_response for response in self.responses)

    @property
    def body_kwargs_to_pass_to_request_builder(self) -> List[str]:
        return [p.serialized_name for p in self.request_builder.body_kwargs_to_get]

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

    @property
    def any_response_has_headers(self) -> bool:
        return any(response.has_headers for response in self.responses)

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

    def _imports_shared(self, async_mode: bool) -> FileImport: # pylint: disable=unused-argument
        file_import = FileImport()
        file_import.add_submodule_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
        for param in self.parameters.method:
            file_import.merge(param.imports())

        for param in self.multiple_content_type_parameters:
            file_import.merge(param.imports())

        for response in self.responses:
            file_import.merge(response.imports(self.code_model))
            if response.has_body:
                file_import.merge(cast(BaseSchema, response.schema).imports())

        response_types = [r.type_annotation(is_operation_file=True) for r in self.responses if r.has_body]
        if len(set(response_types)) > 1:
            file_import.add_submodule_import("typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL)

        if self.is_stream_response:
            file_import.add_submodule_import("typing", "IO", ImportType.STDLIB, TypingSection.CONDITIONAL)
        return file_import


    def imports_for_multiapi(self, async_mode: bool) -> FileImport:  # pylint: disable=unused-argument
        return self._imports_shared(async_mode)

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_base(async_mode, is_python3_file)
        if self.has_response_body and not self.has_optional_return_type and not self.code_model.options["models_mode"]:
            file_import.add_submodule_import("typing", "cast", ImportType.STDLIB)
        return file_import

    @staticmethod
    def has_kwargs_to_pop_with_default(kwargs_to_pop: List[Parameter], location: ParameterLocation) -> bool:
        return any(kwarg.has_default_value and kwarg.location == location for kwarg in kwargs_to_pop)

    def _imports_base(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)

        # Exceptions
        file_import.add_submodule_import("azure.core.exceptions", "map_error", ImportType.AZURECORE)
        if self.code_model.options["azure_arm"]:
            file_import.add_submodule_import("azure.mgmt.core.exceptions", "ARMErrorFormat", ImportType.AZURECORE)
        file_import.add_submodule_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)

        file_import.add_submodule_import("typing", "Callable", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_submodule_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_submodule_import("typing", "Dict", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_submodule_import("typing", "TypeVar", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_submodule_import("azure.core.pipeline", "PipelineResponse", ImportType.AZURECORE)
        file_import.add_submodule_import("azure.core.rest", "HttpRequest", ImportType.AZURECORE)
        kwargs_to_pop = self.parameters.kwargs_to_pop(is_python3_file)
        if (self.has_kwargs_to_pop_with_default(kwargs_to_pop, ParameterLocation.Header) or
            self.has_kwargs_to_pop_with_default(kwargs_to_pop, ParameterLocation.Query)):
            file_import.add_submodule_import("azure.core.utils", "case_insensitive_dict", ImportType.AZURECORE)
        if async_mode:
            file_import.add_submodule_import("azure.core.pipeline.transport", "AsyncHttpResponse", ImportType.AZURECORE)
        else:
            file_import.add_submodule_import("azure.core.pipeline.transport", "HttpResponse", ImportType.AZURECORE)

        if self.deprecated:
            file_import.add_import("warnings", ImportType.STDLIB)

        if self.code_model.options["builders_visibility"] != "embedded":
            builder_group_name = self.request_builder.builder_group_name
            rest_import_path = "..." if async_mode else ".."
            if builder_group_name:
                file_import.add_submodule_import(
                    f"{rest_import_path}{self.code_model.rest_layer_name}",
                    builder_group_name,
                    import_type=ImportType.LOCAL,
                    alias=f"rest_{builder_group_name}"
                )
            else:
                file_import.add_submodule_import(
                    rest_import_path,
                    self.code_model.rest_layer_name,
                    import_type=ImportType.LOCAL,
                    alias="rest"
                )
        if self.code_model.options["builders_visibility"] == "embedded" and not async_mode:
            file_import.merge(self.request_builder.imports(async_mode))
        if self.code_model.need_request_converter:
            relative_path = "..." if async_mode else ".."
            file_import.add_submodule_import(
                f"{relative_path}_vendor", "_convert_request", ImportType.LOCAL
            )

        if self.code_model.options["tracing"] and self.want_tracing:
            file_import.add_submodule_import(
                f"azure.core.tracing.decorator{'_async' if async_mode else ''}",
                f"distributed_trace{'_async' if async_mode else ''}",
                ImportType.AZURECORE,
            )
        return file_import

    def _get_body_param_from_body_kwarg(self, body_kwarg: Parameter) -> Parameter:
        # determine which of the body parameters returned from m4 corresponds to this body_kwarg
        if not self.multiple_content_type_parameters.has_body:
            return self.parameters.body[0]
        if body_kwarg.serialized_name == "data":
            return next(p for p in self.multiple_content_type_parameters.body if p.is_data_input)
        if body_kwarg.serialized_name == "files":
            return next(p for p in self.multiple_content_type_parameters.body if p.is_multipart)
        if body_kwarg.serialized_name == "json":
            # first check if there's any non-binary. In the case of multiple content types, there's
            # usually one binary (for content), and one schema parameter (for json)
            try:
                return next(
                    p for p in self.multiple_content_type_parameters.body
                    if not isinstance(p.schema, IOSchema)
                )
            except StopIteration:
                return next(p for p in self.multiple_content_type_parameters.body if p.is_json_parameter)
        return self.multiple_content_type_parameters.body[0]

    def link_body_kwargs_to_body_params(self) -> None:
        if not self.parameters.has_body:
            return
        body_kwargs = [
            p for p in self.request_builder.parameters.body
            if p.content_types
        ]
        if len(body_kwargs) == 1:
            self.parameters.body[0].body_kwargs = [body_kwargs[0]]
            return
        for body_kwarg in body_kwargs:
            body_param = self._get_body_param_from_body_kwarg(body_kwarg)
            body_param.body_kwargs.append(body_kwarg)

    def convert_multiple_content_type_parameters(self) -> None:
        type_annot = ", ".join([
            param.schema.type_annotation(is_operation_file=True)
            for param in self.multiple_content_type_parameters
        ])
        docstring_type = " or ".join([
            param.schema.docstring_type for param in self.multiple_content_type_parameters
        ])
        try:
            # get an optional param with object first. These params are the top choice
            # bc they have more info about how to serialize the body
            chosen_parameter = next(
                p for p in self.multiple_content_type_parameters
                if not p.required and isinstance(p.schema, ObjectSchema)
            )
        except StopIteration:  # pylint: disable=broad-except
            # otherwise, we get the first optional param, if that exists. If not, we just grab the first one
            optional_parameters = [p for p in self.multiple_content_type_parameters if not p.required]
            chosen_parameter = (
                optional_parameters[0] if optional_parameters else self.multiple_content_type_parameters[0]
            )
        if not chosen_parameter:
            raise ValueError("You are missing a parameter that has multiple media types")
        chosen_parameter.multiple_content_types_type_annot = f"Union[{type_annot}]"
        chosen_parameter.multiple_content_types_docstring_type = docstring_type
        self.parameters.append(chosen_parameter)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], *, code_model) -> "Operation":
        name = yaml_data["language"]["python"]["name"]
        _LOGGER.debug("Parsing %s operation", name)

        parameter_creator = get_parameter(code_model).from_yaml
        parameter_list_creator = get_parameter_list(code_model)
        schema_requests = [SchemaRequest.from_yaml(yaml, code_model=code_model) for yaml in yaml_data["requests"]]
        parameters, multiple_content_type_parameters = create_parameters(
            yaml_data, code_model, parameter_creator
        )
        parameter_list = parameter_list_creator(code_model, parameters, schema_requests)
        multiple_content_type_parameter_list = parameter_list_creator(
            code_model, multiple_content_type_parameters, schema_requests
        )

        if len(parameter_list.content_types) > 1:
            for p in parameter_list.parameters:
                if p.rest_api_name == "Content-Type":
                    p.is_keyword_only = True

        return cls(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            description=yaml_data["language"]["python"]["description"],
            api_versions=set(value_dict["version"] for value_dict in yaml_data["apiVersions"]),
            parameters=parameter_list,
            multiple_content_type_parameters=multiple_content_type_parameter_list,
            schema_requests=schema_requests,
            summary=yaml_data["language"]["python"].get("summary"),
            responses=[
                SchemaResponse.from_yaml(yaml, code_model=code_model)
                for yaml in yaml_data.get("responses", [])
            ],
            # Exception with no schema means default exception, we don't store them
            exceptions=[
                SchemaResponse.from_yaml(yaml, code_model=code_model)
                for yaml in yaml_data.get("exceptions", []) if "schema" in yaml
            ],
        )
