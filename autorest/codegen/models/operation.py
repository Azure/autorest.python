# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from itertools import chain
from typing import (
    Dict,
    List,
    Any,
    Optional,
    Union,
    TYPE_CHECKING,
    Generic,
    TypeVar,
    cast,
)

from .request_builder_parameter import RequestBuilderParameter

from .utils import OrderedSet, add_to_pylint_disable

from .base_builder import BaseBuilder
from .imports import FileImport, ImportType, TypingSection
from .response import (
    Response,
    PagingResponse,
    LROResponse,
    LROPagingResponse,
    get_response,
)
from .parameter import (
    BodyParameter,
    MultipartBodyParameter,
    Parameter,
    ParameterLocation,
)
from .parameter_list import ParameterList
from .model_type import ModelType
from .request_builder import OverloadedRequestBuilder, RequestBuilder

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)

ResponseType = TypeVar(
    "ResponseType",
    bound=Union[Response, PagingResponse, LROResponse, LROPagingResponse],
)


class OperationBase(  # pylint: disable=too-many-public-methods
    Generic[ResponseType], BaseBuilder[ParameterList]
):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        request_builder: Union[RequestBuilder, OverloadedRequestBuilder],
        parameters: ParameterList,
        responses: List[ResponseType],
        exceptions: List[Response],
        *,
        overloads: Optional[List["Operation"]] = None,
        public: bool = True,
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
        self.overloads: List["Operation"] = overloads or []
        self.responses = responses
        self.public = public
        self.request_builder = request_builder
        self.deprecated = False
        self.exceptions = exceptions

    @property
    def operation_type(self) -> str:
        return "operation"

    @property
    def has_optional_return_type(self) -> bool:
        """Has optional return type if there are multiple successful response types where some have
        bodies and some are None
        """
        # means if we have at least one successful response with a body and one without
        successful_response_with_body = any(r for r in self.responses if r.type)
        successful_response_without_body = any(r for r in self.responses if not r.type)
        return successful_response_with_body and successful_response_without_body

    def response_type_annotation(self, **kwargs) -> str:
        if (
            self.code_model.options["head_as_boolean"]
            and self.request_builder.method.lower() == "head"
        ):
            return "bool"
        response_type_annotations: OrderedSet[str] = {
            response.type_annotation(**kwargs): None
            for response in self.responses
            if response.type
        }
        response_str = ", ".join(response_type_annotations.keys())
        if len(response_type_annotations) > 1:
            return f"Union[{response_str}]"
        if self.has_optional_return_type:
            return f"Optional[{response_str}]"
        if self.responses:
            return self.responses[0].type_annotation(**kwargs)
        return "None"

    @property
    def pylint_disable(self) -> str:
        retval: str = ""
        if self.response_type_annotation(async_mode=False) == "None":
            # doesn't matter if it's async or not
            retval = add_to_pylint_disable(retval, "inconsistent-return-statements")
        return retval

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        if (
            self.request_builder.method.lower() == "head"
            and self.code_model.options["head_as_boolean"]
        ):
            return "ClsType[None]"
        return f"ClsType[{self.response_type_annotation(async_mode=async_mode)}]"

    def _response_docstring_helper(self, attr_name: str, **kwargs: Any) -> str:
        responses_with_body = [r for r in self.responses if r.type]
        if (
            self.request_builder.method.lower() == "head"
            and self.code_model.options["head_as_boolean"]
        ):
            return "bool"
        if responses_with_body:
            response_docstring_values: OrderedSet[str] = {
                getattr(response, attr_name)(**kwargs): None
                for response in responses_with_body
            }
            retval = " or ".join(response_docstring_values.keys())
            if self.has_optional_return_type:
                retval += " or None"
            return retval
        if self.responses:
            return getattr(self.responses[0], attr_name)(**kwargs)
        return "None"

    def response_docstring_text(self, **kwargs) -> str:
        retval = self._response_docstring_helper("docstring_text", **kwargs)
        if not self.code_model.options["version_tolerant"]:
            retval += " or the result of cls(response)"
        return retval

    def response_docstring_type(self, **kwargs) -> str:
        return self._response_docstring_helper("docstring_type", **kwargs)

    @property
    def has_response_body(self) -> bool:
        """Tell if at least one response has a body."""
        return any(response.type for response in self.responses)

    @property
    def any_response_has_headers(self) -> bool:
        return any(response.headers for response in self.responses)

    @property
    def default_error_deserialization(self) -> Optional[str]:
        default_exceptions = [
            e for e in self.exceptions if "default" in e.status_codes and e.type
        ]
        if not default_exceptions:
            return None
        excep_schema = default_exceptions[0].type
        if isinstance(excep_schema, ModelType):
            return f"_models.{excep_schema.name}"
        # in this case, it's just an AnyType
        return "'object'"

    @property
    def non_default_errors(self) -> List[Response]:
        return [e for e in self.exceptions if "default" not in e.status_codes]

    @property
    def non_default_error_status_codes(self) -> List[Union[str, int]]:
        """Actually returns all of the status codes from exceptions (besides default)"""
        return list(
            chain.from_iterable(
                [error.status_codes for error in self.non_default_errors]
            )
        )

    def _imports_shared(self, async_mode: bool, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        if not self.abstract:
            for param in self.parameters.method:
                file_import.merge(param.imports(async_mode, **kwargs))

        response_types = [
            r.type_annotation(async_mode=async_mode) for r in self.responses if r.type
        ]
        if len(set(response_types)) > 1:
            file_import.add_submodule_import(
                "typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        return file_import

    def imports_for_multiapi(self, async_mode: bool, **kwargs: Any) -> FileImport:
        file_import = self._imports_shared(async_mode, **kwargs)
        for response in self.responses:
            file_import.merge(
                response.imports_for_multiapi(async_mode=async_mode, **kwargs)
            )
        if self.code_model.options["models_mode"]:
            for exception in self.exceptions:
                file_import.merge(
                    exception.imports_for_multiapi(async_mode=async_mode, **kwargs)
                )
        return file_import

    @staticmethod
    def has_kwargs_to_pop_with_default(
        kwargs_to_pop: List[
            Union[
                Parameter,
                RequestBuilderParameter,
                BodyParameter,
                MultipartBodyParameter,
            ]
        ],
        location: ParameterLocation,
    ) -> bool:
        return any(
            (kwarg.client_default_value or kwarg.optional)
            and kwarg.location == location
            for kwarg in kwargs_to_pop
        )

    def get_request_builder_import(
        self,
        request_builder: Union[RequestBuilder, OverloadedRequestBuilder],
        async_mode: bool,
    ) -> FileImport:
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
                "_py3"
                if self.code_model.options["add_python3_operation_files"]
                and not self.code_model.options["python3_only"]
                else ""
            )
            file_import.add_submodule_import(
                f"...{self.code_model.operations_folder_name}.{self.filename}{suffix}",
                request_builder.name,
                import_type=ImportType.LOCAL,
            )
        return file_import

    def imports(
        self, async_mode: bool, is_python3_file: bool, **kwargs: Any
    ) -> FileImport:
        file_import = self._imports_shared(async_mode, **kwargs)

        for response in self.responses:
            file_import.merge(response.imports(async_mode=async_mode, **kwargs))
        if self.code_model.options["models_mode"]:
            for exception in self.exceptions:
                file_import.merge(exception.imports(async_mode=async_mode, **kwargs))

        if self.parameters.has_body and self.parameters.body_parameter.flattened:
            file_import.merge(self.parameters.body_parameter.type.imports(**kwargs))

        # Exceptions
        if not self.abstract:
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
        if (
            self.code_model.options["tracing"]
            and self.want_tracing
            and not async_mode
            and not self.abstract
        ):
            file_import.add_submodule_import(
                f"azure.core.tracing.decorator",
                f"distributed_trace",
                ImportType.AZURECORE,
            )
        if not self.abstract:
            file_import.merge(
                self.get_request_builder_import(self.request_builder, async_mode)
            )
        if self.overloads:
            file_import.add_submodule_import("typing", "overload", ImportType.STDLIB)
        return file_import

    def get_response_from_status(
        self, status_code: Optional[Union[str, int]]
    ) -> ResponseType:
        try:
            return next(r for r in self.responses if status_code in r.status_codes)
        except StopIteration:
            raise ValueError(
                f"Incorrect status code {status_code}, operation {self.name}"
            )

    @property
    def success_status_codes(self) -> List[Union[str, int]]:
        """The list of all successfull status code."""
        return [code for response in self.responses for code in response.status_codes]

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
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel"):
        name = yaml_data["name"]
        request_builder = code_model.lookup_request_builder(id(yaml_data))
        responses = [
            cast(ResponseType, get_response(r, code_model))
            for r in yaml_data["responses"]
        ]
        exceptions = [
            Response.from_yaml(e, code_model) for e in yaml_data["exceptions"]
        ]
        parameter_list = ParameterList.from_yaml(yaml_data, code_model)
        overloads = [
            cls.from_yaml(overload, code_model)
            for overload in yaml_data.get("overloads", [])
        ]
        abstract = False
        if (
            code_model.options["version_tolerant"]
            and parameter_list.has_body
            and isinstance(parameter_list.body_parameter, MultipartBodyParameter)
        ):
            _LOGGER.warning(
                'Not going to generate operation "%s" because it has multipart / urlencoded body parameters. '
                "Multipart / urlencoded body parameters are not supported for version tolerant generation right now. "
                'Please write your own custom operation in the "_patch.py" file '
                "following https://aka.ms/azsdk/python/dpcodegen/python/customize",
                name,
            )
            abstract = True

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            request_builder=request_builder,
            name=name,
            parameters=parameter_list,
            overloads=overloads,
            responses=responses,
            exceptions=exceptions,
            want_tracing=not yaml_data["isOverload"],
            abstract=abstract,
        )


class Operation(OperationBase[Response]):
    def imports(
        self, async_mode: bool, is_python3_file: bool, **kwargs: Any
    ) -> FileImport:
        file_import = super().imports(async_mode, is_python3_file, **kwargs)
        if async_mode and not self.abstract:
            file_import.add_submodule_import(
                f"azure.core.tracing.decorator_async",
                f"distributed_trace_async",
                ImportType.AZURECORE,
            )
        if self.abstract:
            return file_import
        if (
            self.has_response_body
            and not self.has_optional_return_type
            and not self.code_model.options["models_mode"]
        ):
            file_import.add_submodule_import("typing", "cast", ImportType.STDLIB)

        return file_import


def get_operation(yaml_data: Dict[str, Any], code_model: "CodeModel") -> OperationBase:
    if yaml_data["discriminator"] == "lropaging":
        from .lro_paging_operation import LROPagingOperation as OperationCls
    elif yaml_data["discriminator"] == "lro":
        from .lro_operation import LROOperation as OperationCls  # type: ignore
    elif yaml_data["discriminator"] == "paging":
        from .paging_operation import PagingOperation as OperationCls  # type: ignore
    else:
        from . import Operation as OperationCls  # type: ignore
    return OperationCls.from_yaml(yaml_data, code_model)
