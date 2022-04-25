# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import chain
import logging
from typing import Dict, List, Any, Optional, Type, Union, TYPE_CHECKING, cast, TypeVar, Generic

from .utils import OrderedSet

from .base_builder import BaseBuilder
from .imports import FileImport, ImportType, TypingSection
from .response import Response
from .parameter import MultipartBodyParameter, MultipleTypeBodyParameter, SingleTypeBodyParameter, Parameter, UrlEncodedBodyParameter, ParameterLocation
from .parameter_list import ParameterList, OverloadedOperationParameterList
from .model_type import ModelType
from .request_builder import OverloadedRequestBuilder, RequestBuilder

if TYPE_CHECKING:
    from .code_model import CodeModel

ParameterListType = TypeVar("ParameterListType", bound=Union[ParameterList, OverloadedOperationParameterList])

_LOGGER = logging.getLogger(__name__)

class OperationBase(BaseBuilder[ParameterListType]):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        request_builder: Union[RequestBuilder, OverloadedRequestBuilder],
        parameters: ParameterListType,
        responses: List[Response],
        *,
        overloads: Optional[List["Operation"]] = None,
        want_description_docstring: bool = True,
        want_tracing: bool = True,
        abstract: bool = False,
    ) -> None:
        super().__init__(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            parameters=parameters,
            overloads=overloads,
            abstract=abstract,
            want_tracing=want_tracing,
        )
        self.overloads = overloads
        self.responses = responses
        self.want_description_docstring = want_description_docstring
        self.request_builder = request_builder
        self.deprecated = False
        self.operation_type = "operation"

    @property
    def has_optional_return_type(self) -> bool:
        """Has optional return type if there are multiple successful response types where some have
        bodies and some are None
        """
        # means if we have at least one successful response with a body and one without
        successful_responses = [r for r in self.responses if not r.is_error]
        successful_response_with_body = any(
            r for r in successful_responses if r.type
        )
        successful_response_without_body = any(
            r for r in successful_responses if not r.type
        )
        return successful_response_with_body and successful_response_without_body

    def response_type_annotation(self, **kwargs) -> str:
        if self.code_model.options["head_as_boolean"] and self.request_builder.method.lower() == "head":
            return "bool"
        response_body_annotations: OrderedSet[str] = {}
        for response in [r for r in self.responses if r.type]:
            response_body_annotations[response.type_annotation()] = None
        response_str = ", ".join(response_body_annotations.keys()) or "None"
        if len(response_body_annotations) > 1:
            return f"Union[{response_str}]"
        if self.has_optional_return_type:
            return f"Optional[{response_str}]"
        return response_str

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        return f"ClsType[{self.response_type_annotation(async_mode=async_mode)}]"

    def _response_docstring_helper(self, attr_name: str) -> str:
        responses_with_body = [r for r in self.responses if r.type]
        if (self.request_builder.method.lower() == "head" and self.code_model.options["head_as_boolean"]):
            return "bool"
        if responses_with_body:
            response_docstring_values: OrderedSet[str] = {
                getattr(response, attr_name): None for response in responses_with_body
            }
            retval = " or ".join(response_docstring_values.keys())
            if self.has_optional_return_type:
                retval += " or None"
            return retval
        return "None"

    def response_docstring_text(self, **kwargs) -> str:
        retval = self._response_docstring_helper("docstring_text")
        if not self.code_model.options["version_tolerant"]:
            retval += " or the result of cls(response)"
        return retval


    def response_docstring_type(self, **kwargs) -> str:
        return self._response_docstring_helper("docstring_type")

    @property
    def has_response_body(self) -> bool:
        """Tell if at least one response has a body."""
        return any(
            response.type
            for response in self.responses
        )

    @property
    def any_response_has_headers(self) -> bool:
        return any(response.headers for response in self.responses)

    @property
    def default_error_deserialization(self) -> Optional[str]:
        retval = [
            r for r in self.responses
            if r.is_error and "*" in r.status_codes
        ]
        if not retval:
            return None
        excep_schema = retval[0].type
        if isinstance(excep_schema, ModelType):
            return f"_models.{excep_schema.name}"
        # in this case, it's just an AnyType
        return "'object'"


    @property
    def non_default_errors(self) -> List[Response]:
        return [
            r for r in self.responses if r.is_error and "*" not in r.status_codes
        ]

    @property
    def non_default_error_status_codes(self) -> List[Union[str, int]]:
        """Actually returns all of the status codes from exceptions (besides default)"""
        return list(
            chain.from_iterable(
                [error.status_codes for error in self.non_default_errors]
            )
        )

    def _imports_shared(
        self, async_mode: bool  # pylint: disable=unused-argument
    ) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        for param in self.parameters.method:
            if self.abstract and isinstance(param, (MultipartBodyParameter, UrlEncodedBodyParameter)):
                continue
            file_import.merge(param.imports())

        for response in self.responses:
            file_import.merge(response.imports())

        response_types = [
            r.type_annotation()
            for r in self.responses
            if r.type
        ]
        if len(set(response_types)) > 1:
            file_import.add_submodule_import(
                "typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        return file_import

    def imports_for_multiapi(
        self, async_mode: bool
    ) -> FileImport:  # pylint: disable=unused-argument
        return self._imports_shared(async_mode)

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_base(async_mode, is_python3_file)
        if self.abstract:
            return file_import
        if (
            self.has_response_body
            and not self.has_optional_return_type
            and not self.code_model.options["models_mode"]
        ):
            file_import.add_submodule_import("typing", "cast", ImportType.STDLIB)
        return file_import

    @staticmethod
    def has_kwargs_to_pop_with_default(
        kwargs_to_pop: List[Parameter], location: ParameterLocation
    ) -> bool:
        return any(
            (kwarg.client_default_value or kwarg.optional) and kwarg.location == location
            for kwarg in kwargs_to_pop
        )

    def get_request_builder_import(self, request_builder: Union[RequestBuilder, OverloadedRequestBuilder], async_mode: bool) -> FileImport:
        """Helper method to get a request builder import."""
        file_import = FileImport()
        if self.code_model.options["builders_visibility"] != "embedded":
            group_name = request_builder.group_name
            rest_import_path = "..." if async_mode else ".."
            if group_name:
                file_import.add_submodule_import(
                    f"{rest_import_path}{self.code_model.rest_layer_name}",
                    group_name,
                    import_type=ImportType.LOCAL,
                    alias=f"rest_{group_name}",
                )
            else:
                file_import.add_submodule_import(
                    rest_import_path,
                    self.code_model.rest_layer_name,
                    import_type=ImportType.LOCAL,
                    alias="rest",
                )
        if self.code_model.options["builders_visibility"] == "embedded" and async_mode:
            suffix = (
                "_py3" if self.code_model.options["add_python3_operation_files"] else ""
            )
            file_import.add_submodule_import(
                f"...{self.code_model.operations_folder_name}.{self.filename}{suffix}",
                request_builder.name,
                import_type=ImportType.LOCAL,
            )
        return file_import

    def _imports_base(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)

        # Exceptions
        if self.abstract:
            file_import.add_import("abc", ImportType.STDLIB)
        else:
            file_import.add_submodule_import(
                "azure.core.exceptions", "map_error", ImportType.AZURECORE
            )
            if self.code_model.options["azure_arm"]:
                file_import.add_submodule_import(
                    "azure.mgmt.core.exceptions", "ARMErrorFormat", ImportType.AZURECORE
                )
            file_import.add_submodule_import(
                "azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE
            )
            file_import.add_submodule_import(
                "azure.core.exceptions",
                "ClientAuthenticationError",
                ImportType.AZURECORE,
            )
            file_import.add_submodule_import(
                "azure.core.exceptions", "ResourceNotFoundError", ImportType.AZURECORE
            )
            file_import.add_submodule_import(
                "azure.core.exceptions", "ResourceExistsError", ImportType.AZURECORE
            )

            kwargs_to_pop = self.parameters.kwargs_to_pop(is_python3_file)
            if self.has_kwargs_to_pop_with_default(
                kwargs_to_pop, ParameterLocation.HEADER
            ) or self.has_kwargs_to_pop_with_default(
                kwargs_to_pop, ParameterLocation.QUERY
            ):
                file_import.add_submodule_import(
                    "azure.core.utils", "case_insensitive_dict", ImportType.AZURECORE
                )
            if self.deprecated:
                file_import.add_import("warnings", ImportType.STDLIB)

            if self.code_model.need_request_converter:
                relative_path = "..." if async_mode else ".."
                file_import.add_submodule_import(
                    f"{relative_path}_vendor", "_convert_request", ImportType.LOCAL
                )
        if async_mode:
            file_import.add_submodule_import(
                "azure.core.pipeline.transport",
                "AsyncHttpResponse",
                ImportType.AZURECORE,
            )
        else:
            file_import.add_submodule_import(
                "azure.core.pipeline.transport", "HttpResponse", ImportType.AZURECORE
            )
        if (
            self.code_model.options["builders_visibility"] == "embedded"
            and not async_mode
        ):
            file_import.merge(self.request_builder.imports())
        file_import.add_submodule_import(
            "azure.core.pipeline", "PipelineResponse", ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "azure.core.rest", "HttpRequest", ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "typing", "Callable", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import(
            "typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import(
            "typing", "Dict", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import(
            "typing", "TypeVar", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        if self.code_model.options["tracing"] and self.want_tracing:
            file_import.add_submodule_import(
                f"azure.core.tracing.decorator{'_async' if async_mode else ''}",
                f"distributed_trace{'_async' if async_mode else ''}",
                ImportType.AZURECORE,
            )
        file_import.merge(self.get_request_builder_import(self.request_builder, async_mode))
        return file_import

    def get_response_from_status(
        self, status_code: Optional[Union[str, int]]
    ) -> Response:
        try:
            return next(r for r in self.responses if status_code in r.status_codes)
        except StopIteration:
            raise ValueError(f"Incorrect status code {status_code}, operation {self.name}")

    @property
    def success_status_codes(self) -> List[Union[str, int]]:
        """The list of all successfull status code."""
        return [
            code
            for response in self.responses
            for code in response.status_codes
            if not response.is_error
        ]

    @property
    def filename(self) -> str:
        basename = self.group_name
        if basename == "":
            # in a mixin
            basename = self.code_model.module_name

        if (
            basename == "operations"
            or self.code_model.options["combine_operation_files"]
        ):
            return f"_operations"
        return f"_{basename}_operations"

    @property
    def has_stream_response(self) -> bool:
        return any(r.is_stream_response for r in self.responses)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> Union["Operation", "OverloadedOperation"]:
        if yaml_data["discriminator"] == "paging":
            from .paging_operation import PagingOperation
            return PagingOperation.from_yaml(yaml_data, code_model)
        if yaml_data.get("overloads"):
            return OverloadedOperation.from_yaml(yaml_data, code_model)
        return Operation.from_yaml(yaml_data, code_model)

class Operation(OperationBase[ParameterList]):

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Operation":
        name = yaml_data["name"]
        parameters = [Parameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        request_builder = code_model.lookup_request_builder(id(yaml_data))
        responses = [Response.from_yaml(r, code_model) for r in yaml_data["responses"]]
        if yaml_data["bodyParameter"]:
            body_parameter = SingleTypeBodyParameter.from_yaml(yaml_data["bodyParameter"], code_model)
        else:
            body_parameter = None
        parameter_list = ParameterList(code_model, parameters, body_parameter)
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            request_builder=request_builder,
            name=name,
            parameters=parameter_list,
            responses=responses,
            want_tracing=not yaml_data["isOverload"],
        )

class OverloadedOperation(OperationBase[OverloadedOperationParameterList]):

    def _imports_shared(self, async_mode: bool) -> FileImport:
        file_import = super()._imports_shared(async_mode)
        file_import.add_submodule_import("typing", "overload", ImportType.STDLIB)
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "OverloadedOperation":
        name = yaml_data["name"]
        parameters = [Parameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        request_builder = code_model.lookup_request_builder(id(yaml_data))
        responses = [Response.from_yaml(r, code_model) for r in yaml_data["responses"]]
        if yaml_data["bodyParameter"]:
            body_parameter = MultipleTypeBodyParameter.from_yaml(yaml_data["bodyParameter"], code_model)
        else:
            body_parameter = None
        overloads = [Operation.from_yaml(overload_yaml_data, code_model) for overload_yaml_data in yaml_data["overloads"]]
        parameter_list = OverloadedOperationParameterList(code_model, parameters, body_parameter)
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            request_builder=request_builder,
            overloads=overloads,
            name=name,
            parameters=parameter_list,
            responses=responses,
        )
