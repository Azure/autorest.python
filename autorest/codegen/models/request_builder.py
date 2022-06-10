# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import (
    Any,
    Callable,
    Dict,
    List,
    TypeVar,
    TYPE_CHECKING,
    Union,
    Optional,
)
from abc import abstractmethod

from .base_builder import BaseBuilder
from .parameter_list import (
    RequestBuilderParameterList,
    OverloadedRequestBuilderParameterList,
)
from .imports import FileImport, ImportType, TypingSection
from .request_builder_parameter import RequestBuilderMultipartBodyParameter

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)
ParameterListType = TypeVar(
    "ParameterListType",
    bound=Union[RequestBuilderParameterList, OverloadedRequestBuilderParameterList],
)


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
        self.overloads: List["RequestBuilder"] = overloads or []
        self.url: str = yaml_data["url"]
        self.method: str = yaml_data["method"]

    def response_type_annotation(self, **kwargs) -> str:
        return "HttpRequest"

    def response_docstring_text(self, **kwargs) -> str:
        return (
            "Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's "
            + "`send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to "
            + "incorporate this response into your code flow."
        )

    def response_docstring_type(self, **kwargs) -> str:
        return "~azure.core.rest.HttpRequest"

    def imports(self) -> FileImport:
        file_import = FileImport()
        if self.abstract:
            return file_import
        for parameter in self.parameters.method:
            file_import.merge(parameter.imports(async_mode=False))

        file_import.add_submodule_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
        )

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
        if (
            self.overloads
            and self.code_model.options["builders_visibility"] != "embedded"
        ):
            file_import.add_submodule_import("typing", "overload", ImportType.STDLIB)
        return file_import

    @staticmethod
    @abstractmethod
    def parameter_list_type() -> Callable[
        [Dict[str, Any], "CodeModel"], ParameterListType
    ]:
        ...

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel"):
        # when combine embedded builders into one operation file, we need to avoid duplicated build function name.
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
        overloads = [
            RequestBuilder.from_yaml(rb_yaml_data, code_model)
            for rb_yaml_data in yaml_data.get("overloads", [])
        ]
        abstract = False
        parameter_list = cls.parameter_list_type()(yaml_data, code_model)
        if (
            code_model.options["version_tolerant"]
            and parameter_list.has_body
            and isinstance(
                parameter_list.body_parameter, RequestBuilderMultipartBodyParameter
            )
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
            name=name,
            parameters=parameter_list,
            overloads=overloads,
            abstract=abstract,
        )


class RequestBuilder(RequestBuilderBase[RequestBuilderParameterList]):
    @staticmethod
    def parameter_list_type() -> Callable[
        [Dict[str, Any], "CodeModel"], RequestBuilderParameterList
    ]:
        return RequestBuilderParameterList.from_yaml


class OverloadedRequestBuilder(
    RequestBuilderBase[OverloadedRequestBuilderParameterList]
):
    @staticmethod
    def parameter_list_type() -> Callable[
        [Dict[str, Any], "CodeModel"], OverloadedRequestBuilderParameterList
    ]:
        return OverloadedRequestBuilderParameterList.from_yaml


def get_request_builder(
    yaml_data: Dict[str, Any], code_model: "CodeModel"
) -> Union[RequestBuilder, OverloadedRequestBuilder]:
    if yaml_data.get("overloads"):
        return OverloadedRequestBuilder.from_yaml(yaml_data, code_model)
    return RequestBuilder.from_yaml(yaml_data, code_model)
