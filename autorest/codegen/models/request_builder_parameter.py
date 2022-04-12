# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, TYPE_CHECKING
from .parameter import (
    BodyParameter,
    HeaderParameter,
    QueryParameter,
    PathParameter,
    ParameterMethodLocation,
    Parameter,
    OverloadBodyParameter
)
from .object_schema import ObjectSchema
from .list_schema import ListSchema
from .dictionary_schema import DictionarySchema

if TYPE_CHECKING:
    from .code_model import CodeModel

class RequestBuilderBodyParameter(BodyParameter):
    @property
    def method_location(self) -> ParameterMethodLocation:
        return ParameterMethodLocation.KEYWORD_ONLY

class RequestBuilderOverloadBodyParameter(OverloadBodyParameter):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if isinstance(self.type, (ObjectSchema, ListSchema, DictionarySchema)):
            self.serialized_name = "json"
        else:
            self.serialized_name = "content"

class RequestBuilderParameter(Parameter):

    @property
    def name_in_high_level_operation(self) -> str:
        return self.serialized_name

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Parameter":
        parameter_class = cls
        if yaml_data["location"] == "header":
            parameter_class = RequestBuilderHeaderParameter
        elif yaml_data["location"] == "query":
            parameter_class = RequestBuilderQueryParameter
        elif yaml_data["location"] == "path":
            parameter_class = RequestBuilderPathParameter
        return parameter_class(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_schema(id(yaml_data["type"]))
        )

class RequestBuilderHeaderParameter(RequestBuilderParameter, HeaderParameter):
    ...

class RequestBuilderPathParameter(RequestBuilderParameter, PathParameter):
    ...

class RequestBuilderQueryParameter(RequestBuilderParameter, QueryParameter):
    ...
