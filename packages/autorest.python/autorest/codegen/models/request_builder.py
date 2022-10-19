# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
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
from .imports import FileImport, ImportType, TypingSection, MsrestImportType

if TYPE_CHECKING:
    from .code_model import NamespaceModel
    from .client import Client

ParameterListType = TypeVar(
    "ParameterListType",
    bound=Union[RequestBuilderParameterList, OverloadedRequestBuilderParameterList],
)


class RequestBuilderBase(BaseBuilder[ParameterListType]):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        namespace_model: "NamespaceModel",
        client: "Client",
        name: str,
        parameters: ParameterListType,
        *,
        overloads: Optional[List["RequestBuilder"]] = None,
    ) -> None:
        super().__init__(
            namespace_model=namespace_model,
            client=client,
            yaml_data=yaml_data,
            name=name,
            parameters=parameters,
            overloads=overloads,
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
            file_import.merge(parameter.imports(async_mode=False, import_literal=True))

        file_import.add_submodule_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
        )

        if self.parameters.path:
            relative_path = ".."
            if (
                not self.namespace_model.options["builders_visibility"] == "embedded"
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
        file_import.add_msrest_import(
            self.namespace_model,
            "..."
            if (
                not self.namespace_model.options["builders_visibility"] == "embedded"
                and self.group_name
            )
            else "..",
            MsrestImportType.Serializer,
            TypingSection.REGULAR,
        )
        if (
            self.overloads
            and self.namespace_model.options["builders_visibility"] != "embedded"
        ):
            file_import.add_submodule_import("typing", "overload", ImportType.STDLIB)
        return file_import

    @staticmethod
    @abstractmethod
    def parameter_list_type() -> Callable[
        [Dict[str, Any], "NamespaceModel"], ParameterListType
    ]:
        ...

    @classmethod
    def from_yaml(
        cls,
        yaml_data: Dict[str, Any],
        namespace_model: "NamespaceModel",
        client: "Client",
    ):
        # when combine embedded builders into one operation file, we need to avoid duplicated build function name.
        # So add operation group name is effective method
        additional_mark = ""
        if (
            namespace_model.options["combine_operation_files"]
            and namespace_model.options["builders_visibility"] == "embedded"
        ):
            additional_mark = (
                yaml_data["groupName"] or client.yaml_data["builderPadName"]
            )
        names = [
            "build",
            additional_mark,
            yaml_data["name"],
            "request",
        ]
        name = "_".join([n for n in names if n])
        overloads = [
            RequestBuilder.from_yaml(rb_yaml_data, namespace_model, client)
            for rb_yaml_data in yaml_data.get("overloads", [])
        ]
        parameter_list = cls.parameter_list_type()(yaml_data, namespace_model)

        return cls(
            yaml_data=yaml_data,
            namespace_model=namespace_model,
            client=client,
            name=name,
            parameters=parameter_list,
            overloads=overloads,
        )


class RequestBuilder(RequestBuilderBase[RequestBuilderParameterList]):
    @staticmethod
    def parameter_list_type() -> Callable[
        [Dict[str, Any], "NamespaceModel"], RequestBuilderParameterList
    ]:
        return RequestBuilderParameterList.from_yaml


class OverloadedRequestBuilder(
    RequestBuilderBase[OverloadedRequestBuilderParameterList]
):
    @staticmethod
    def parameter_list_type() -> Callable[
        [Dict[str, Any], "NamespaceModel"], OverloadedRequestBuilderParameterList
    ]:
        return OverloadedRequestBuilderParameterList.from_yaml


def get_request_builder(
    yaml_data: Dict[str, Any], namespace_model: "NamespaceModel", client: "Client"
) -> Union[RequestBuilder, OverloadedRequestBuilder]:
    if yaml_data.get("overloads"):
        return OverloadedRequestBuilder.from_yaml(yaml_data, namespace_model, client)
    return RequestBuilder.from_yaml(yaml_data, namespace_model, client)
