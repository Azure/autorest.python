# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, TypeVar, TYPE_CHECKING, cast, Union, Optional, Type

from .base_builder import BaseBuilder
from .parameter_list import RequestBuilderParameterList, OverloadedRequestBuilderParameterList
from .imports import FileImport, ImportType, TypingSection
from .request_builder_parameter import RequestBuilderSingleTypeBodyParameter, RequestBuilderParameter, RequestBuilderMultipleTypeBodyParameter

if TYPE_CHECKING:
    from .code_model import CodeModel

ParameterListType = TypeVar("ParameterListType", bound=Union[RequestBuilderParameterList, OverloadedRequestBuilderParameterList])

class RequestBuilderBase(BaseBuilder[ParameterListType]):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        parameters: ParameterListType,
        *,
        overloads: Optional[List["RequestBuilder"]] = None,
        abstract: bool = False,
    ) -> None:
        super().__init__(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            parameters=parameters,
            overloads=overloads,
            abstract=abstract,
            want_tracing=False,
        )
        self.url = yaml_data["url"]
        self.method = yaml_data["method"]

    def response_type_annotation(self, **kwargs) -> str:
        return "HttpRequest"

    def response_docstring_text(self, **kwargs) -> str:
        return (
            "Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's "
            + "`send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to "
            + "incorporate this response into your code flow."
        )

    def response_docstring_type(self, **kwargs) -> str:
        return "~azure.core.rest.HttpRequest"

    def imports(self) -> FileImport:
        file_import = FileImport()
        for parameter in self.parameters.method:
            file_import.merge(parameter.imports())

        file_import.add_submodule_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
        )
        if not self.abstract:
            if self.parameters.path:
                relative_path = ".."
                if (
                    not self.code_model.options["builders_visibility"] == "embedded"
                    and self.group_name
                ):
                    relative_path = "..." if self.group_name else ".."
                file_import.add_submodule_import(
                    f"{relative_path}_vendor", "_format_url_section", ImportType.LOCAL
                )
            if self.parameters.headers or self.parameters.query:
                file_import.add_submodule_import(
                    "azure.core.utils", "case_insensitive_dict", ImportType.AZURECORE
                )
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, typing_section=TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import("msrest", "Serializer", ImportType.THIRDPARTY)
        if self.overloads:
            file_import.add_submodule_import("typing", "overload", ImportType.STDLIB)
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> Union["RequestBuilder", "OverloadedRequestBuilder"]:
        if yaml_data.get("overloads"):
            return OverloadedRequestBuilder.from_yaml(yaml_data, code_model)
        return RequestBuilder.from_yaml(yaml_data, code_model)

def _get_name(yaml_data: Dict[str, Any], code_model: "CodeModel") -> str:
    # when combine embeded builders into one operation file, we need to avoid duplicated build function name.
        # So add operation group name is effective method
    additional_mark = ""
    if (
        code_model.options["combine_operation_files"]
        and code_model.options["builders_visibility"] == "embedded"
    ):
        additional_mark = yaml_data["groupName"]
    names = [
        "build",
        additional_mark,
        yaml_data["name"],
        "request",
    ]
    name = "_".join([n for n in names if n])
    return name


class RequestBuilder(RequestBuilderBase[RequestBuilderParameterList]):

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "RequestBuilder":
        name = _get_name(yaml_data, code_model)
        parameters = [RequestBuilderParameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        if yaml_data["bodyParameter"]:
            body_parameter = RequestBuilderSingleTypeBodyParameter.from_yaml(yaml_data["bodyParameter"], code_model)
        else:
            body_parameter = None
        parameter_list = RequestBuilderParameterList(code_model, parameters, body_parameter)
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            name=name,
            parameters=parameter_list,
        )

class OverloadedRequestBuilder(RequestBuilderBase[OverloadedRequestBuilderParameterList]):
    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "OverloadedRequestBuilder":
        name = _get_name(yaml_data, code_model)
        parameters = [RequestBuilderParameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        if yaml_data["bodyParameter"]:
            body_parameter = RequestBuilderMultipleTypeBodyParameter.from_yaml(yaml_data["bodyParameter"], code_model)
        else:
            body_parameter = None
        parameter_list = OverloadedRequestBuilderParameterList(code_model, parameters, body_parameter)
        overloads=[RequestBuilder.from_yaml(rb_yaml_data, code_model) for rb_yaml_data in yaml_data["overloads"]]
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            name=name,
            parameters=parameter_list,
            overloads=overloads,
        )
