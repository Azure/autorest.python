# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from collections.abc import MutableSequence
from enum import Enum
import logging
from typing import List, Optional, TYPE_CHECKING, Union, Generic, TypeVar
from .request_builder_parameter import RequestBuilderParameter
from .parameter import OverloadBodyParameter, Parameter, ParameterMethodLocation, BodyParameter

ParameterType = TypeVar("ParameterType", bound=Union[Parameter, RequestBuilderParameter])



if TYPE_CHECKING:
    from .code_model import CodeModel

class ParameterImplementation(Enum):
    METHOD = "method"
    CLIENT = "client"

_LOGGER = logging.getLogger(__name__)


def _method_signature_helper(
    positional: List[str], keyword_only: Optional[List[str]], kwarg_params: List[str]
):
    keyword_only = keyword_only or []
    return positional + keyword_only + kwarg_params

def _sort(params):
    return sorted(
        params, key=lambda x: not x.default_value and x.required, reverse=True
    )


class _ParameterListBase(MutableSequence, Generic[ParameterType]):  # pylint: disable=too-many-public-methods
    def __init__(
        self,
        code_model: "CodeModel",
        parameters: List[ParameterType],
        body_parameter: Optional[Union[BodyParameter, OverloadBodyParameter]] = None,
    ) -> None:
        self.code_model = code_model
        self.parameters = parameters or []
        self.body_parameter = body_parameter

    # MutableSequence

    def __getitem__(self, index):
        if isinstance(index, str):
            raise TypeError(f"{index} is invalid type")
        return self.parameters[index]

    def __len__(self) -> int:
        return len(self.parameters)

    def __setitem__(self, index, parameter):
        self.parameters[index] = parameter

    def __delitem__(self, index):
        del self.parameters[index]

    def insert(self, index: int, value: Parameter) -> None:
        self.parameters.insert(index, value)

    # Parameter helpers

    @property
    def path(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location == "path"]

    @property
    def query(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location == "query"]

    @property
    def headers(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location == "header"]

    @property
    def grouped(self) -> List[ParameterType]:
        raise NotImplementedError("No parameter grouping")

    @property
    def groupers(self) -> List[ParameterType]:
        raise NotImplementedError("No parameter grouping")

    @property
    def positional(self) -> List[ParameterType]:
        return _sort([p for p in self.parameters if p.method_location == ParameterMethodLocation.POSITIONAL])

    @property
    def keyword_only(self) -> List[ParameterType]:
        return _sort([p for p in self.parameters if p.method_location == ParameterMethodLocation.KEYWORD_ONLY])

    @property
    def kwarg(self) -> List[ParameterType]:
        return _sort([p for p in self.parameters if p.method_location == ParameterMethodLocation.KWARG])

    @property
    def method(self) -> List[ParameterType]:
        return self.positional + self.keyword_only + self.kwarg

    def method_signature(self, is_python3_file: bool) -> List[str]:
        return _method_signature_helper(
            positional=self.method_signature_positional(is_python3_file),
            keyword_only=self.method_signature_keyword_only(is_python3_file),
            kwarg_params=self.method_signature_kwargs(is_python3_file),
        )

    def method_signature_positional(self, is_python3_file: bool) -> List[str]:
        return [
            parameter.method_signature(is_python3_file) for parameter in self.positional
        ]

    def method_signature_keyword_only(self, is_python3_file: bool) -> List[str]:
        if not (self.keyword_only and is_python3_file):
            return []
        return ["*,"] + [
            parameter.method_signature(is_python3_file)
            for parameter in self.keyword_only
        ]

    @staticmethod
    def method_signature_kwargs(is_python3_file: bool) -> List[str]:
        return ["**kwargs: Any"] if is_python3_file else ["**kwargs  # type: Any"]

    def kwargs_to_pop(self, is_python3_file: bool) -> List[ParameterType]:
        kwargs_to_pop = [p for p in self.parameters if p.method_location == ParameterMethodLocation.KWARG]
        if not is_python3_file:
            kwargs_to_pop += [p for p in self.parameters if p.method_location == ParameterMethodLocation.KEYWORD_ONLY]
        return kwargs_to_pop

    @property
    def call(self) -> List[str]:
        retval = [p.serialized_name for p in self.parameters if p.method_location == ParameterMethodLocation.POSITIONAL]
        retval.extend(
            [f"{p.serialized_name}={p.serialized_name}" for p in self.parameters if p.method_location == ParameterMethodLocation.KEYWORD_ONLY]
        )
        retval.append("**kwargs")
        return retval

class ParameterList(_ParameterListBase[Parameter]):
    ...

class OverloadBaseParameterList(ParameterList):

    def method_signature(self) -> str:
        return "*args, **kwargs"

class RequestBuilderParameterList(_ParameterListBase[RequestBuilderParameter]):

    def method(self):
        ...

class ClientGlobalParameterList(ParameterList):
    ...

class ConfigGlobalParameterList(ParameterList):
    ...
