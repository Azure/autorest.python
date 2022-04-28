# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from ctypes import cast
from typing import TYPE_CHECKING, Any, Dict
from .parameter import (
    ParameterMethodLocation,
    Parameter,
    BodyParameter
)
from .model_type import ModelType
from .list_type import ListType
from .base_type import BaseType
from .dictionary_type import DictionaryType

if TYPE_CHECKING:
    from .code_model import CodeModel

class RequestBuilderBodyParameter(BodyParameter):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if isinstance(self.type, (ModelType, ListType, DictionaryType)):
            self.client_name = "json"
        else:
            self.client_name = "content"

    @property
    def method_location(self) -> ParameterMethodLocation:
        return ParameterMethodLocation.KEYWORD_ONLY

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "RequestBuilderBodyParameter":
        return super().from_yaml(yaml_data, code_model)  # type: ignore

    @property
    def name_in_high_level_operation(self) -> str:
        if self.client_name == "json":
            return "_json"
        return "_content"

class RequestBuilderParameter(Parameter):

    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", type: BaseType) -> None:
        super().__init__(yaml_data, code_model, type)
        # we don't want any default content type behavior in request builder
        if self.rest_api_name == "Content-Type":
            self.client_default_value = None

    @property
    def name_in_high_level_operation(self) -> str:
        return self.client_name
