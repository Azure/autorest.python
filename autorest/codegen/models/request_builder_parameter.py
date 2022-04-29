# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING, Any, Dict, Union
from .parameter import (
    ParameterLocation,
    ParameterMethodLocation,
    Parameter,
    BodyParameter,
    _MultipartBodyParameter,
)
from .base_type import BaseType
from .primitive_types import BinaryType, StringType
from .constant_type import ConstantType

if TYPE_CHECKING:
    from .code_model import CodeModel

class RequestBuilderBodyParameter(BodyParameter):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if isinstance(self.type, (BinaryType, StringType)) or any("xml" in ct for ct in self.content_types):
            self.client_name = "content"
        else:
            self.client_name = "json"

    @property
    def method_location(self) -> ParameterMethodLocation:
        return ParameterMethodLocation.KWARG if self.constant else ParameterMethodLocation.KEYWORD_ONLY

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "RequestBuilderBodyParameter":
        return super().from_yaml(yaml_data, code_model)  # type: ignore

    @property
    def name_in_high_level_operation(self) -> str:
        if self.client_name == "json":
            return "_json"
        return "_content"

class RequestBuilderMultipartBodyParameter(_MultipartBodyParameter[RequestBuilderBodyParameter]):

    @property
    def name_in_high_level_operation(self) -> str:
        return self.client_name

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "RequestBuilderMultipartBodyParameter":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"])),
            entries=[RequestBuilderBodyParameter.from_yaml(entry, code_model) for entry in yaml_data["entries"]]
        )

class RequestBuilderParameter(Parameter):

    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", type: BaseType) -> None:
        super().__init__(yaml_data, code_model, type)
        # we don't want any default content type behavior in request builder
        if self.rest_api_name == "Content-Type":
            self.client_default_value = None

    @property
    def in_method_signature(self) -> bool:
        return super().in_method_signature and self.location != ParameterLocation.ENDPOINT_PATH

    @property
    def full_client_name(self) -> str:
        return self.client_name

    @property
    def method_location(self) -> ParameterMethodLocation:
        super_method_location = super().method_location
        if self.in_overriden and super_method_location == ParameterMethodLocation.KEYWORD_ONLY:
            return ParameterMethodLocation.KWARG
        return super_method_location

    @property
    def name_in_high_level_operation(self) -> str:
        if self.implementation == "Client":
            return f"self._config.{self.client_name}"
        return self.client_name

def get_request_body_parameter(yaml_data: Dict[str, Any], code_model: "CodeModel") -> Union[RequestBuilderBodyParameter, RequestBuilderMultipartBodyParameter]:
    if yaml_data.get("entries"):
        return RequestBuilderMultipartBodyParameter.from_yaml(yaml_data, code_model)
    return RequestBuilderBodyParameter.from_yaml(yaml_data, code_model)
