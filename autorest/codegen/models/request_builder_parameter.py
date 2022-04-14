# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, TYPE_CHECKING
from .parameter import (
    BodyParameter,
    ParameterMethodLocation,
    Parameter,
    OverloadBodyParameter
)
from .model_type import ModelType
from .list_type import ListType
from .dictionary_type import DictionaryType

if TYPE_CHECKING:
    from .code_model import CodeModel

class RequestBuilderBodyParameter(BodyParameter):
    @property
    def method_location(self) -> ParameterMethodLocation:
        return ParameterMethodLocation.KEYWORD_ONLY

class RequestBuilderOverloadBodyParameter(OverloadBodyParameter):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if isinstance(self.type, (ModelType, ListType, DictionaryType)):
            self.client_name = "json"
        else:
            self.client_name = "content"

class RequestBuilderParameter(Parameter):

    @property
    def name_in_high_level_operation(self) -> str:
        return self.client_name
