# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, TypeVar, TYPE_CHECKING, cast, Union
import logging


from .base_builder import BaseBuilder
from .parameter_list import ParameterList, RequestBuilderParameterList
from .imports import FileImport, ImportType, TypingSection
from .parameter import MultipartBodyParameter, UrlEncodedBodyParameter
from .request_builder_parameter import RequestBuilderOverloadBodyParameter, RequestBuilderParameter

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)

T = TypeVar("T")
OrderedSet = Dict[T, None]

def _get_overloads(
    overload_body_parameters: List[RequestBuilderOverloadBodyParameter],
    yaml_data: Dict[str, Any],
    code_model: "CodeModel",
    parameters: List[RequestBuilderParameter],
    name: str,
):
    overloads: List[RequestBuilder] = []
    if overload_body_parameters:
        # we have overloads now, one for each type
        for obp in overload_body_parameters:
            overloads.append(RequestBuilder(
                yaml_data=yaml_data,
                code_model=code_model,
                name=name,
                parameters=RequestBuilderParameterList(
                    code_model=code_model,
                    parameters=parameters,
                    body_parameter=obp
                ),
                overloads=[],
                want_tracing=False,
            ))
    return overloads


class RequestBuilder(BaseBuilder[RequestBuilderParameterList]):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        parameters: RequestBuilderParameterList,
        overloads: List["RequestBuilder"],
        *,
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
        return file_import

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "RequestBuilder":

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

        parameters = [RequestBuilderParameter.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        abstract = False
        parameter_list, overload_body_parameters = cls.create_parameters_and_overloads(
            yaml_data, code_model, is_operation=True
        )
        overloads = _get_overloads(
            cast(List[RequestBuilderOverloadBodyParameter], overload_body_parameters),
            yaml_data,
            code_model,
            parameters,
            name,
        )
        # if (
        #     code_model.options["version_tolerant"]
        #     or code_model.options["low_level_client"]
        # ) and any(p for p in parameter_list if p.is_multipart or p.is_data_input):
        #     _LOGGER.warning(
        #         'Not going to generate request_builder "%s" because it has multipart / urlencoded '
        #         "body parameters. Multipart / urlencoded body parameters are not supported for version "
        #         "tolerant and low level generations right now. Please write your own custom operation "
        #         "in the _patch.py file following https://aka.ms/azsdk/python/dpcodegen/python/customize.",
        #         name,
        #     )
        #     abstract = True

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            name=name,
            parameters=parameter_list,
            overloads=overloads,
            abstract=abstract,
        )
