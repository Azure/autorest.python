# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict
from abc import abstractmethod
from collections.abc import MutableSequence
from enum import Enum
import logging
from typing import List, Optional, TYPE_CHECKING, Union, Generic, TypeVar, Type
from .combined_type import CombinedType
from .imports import FileImport, ImportType
from .request_builder_parameter import RequestBuilderBodyParameter, RequestBuilderParameter
from .parameter import ParameterLocation, BodyParameter, Parameter, ParameterMethodLocation, ClientParameter, ConfigParameter

ParameterType = TypeVar("ParameterType", bound=Union[Parameter, RequestBuilderParameter])
BodyParameterType = TypeVar("BodyParameterType", bound=Union[BodyParameter, RequestBuilderBodyParameter])


if TYPE_CHECKING:
    from .code_model import CodeModel

class ParameterImplementation(Enum):
    METHOD = "method"
    CLIENT = "client"

_LOGGER = logging.getLogger(__name__)


def method_signature_helper(
    positional: List[str], keyword_only: Optional[List[str]], kwarg_params: List[str]
):
    keyword_only = keyword_only or []
    return positional + keyword_only + kwarg_params

def _sort(params):
    return sorted(
        params, key=lambda x: not (x.client_default_value or x.optional), reverse=True
    )


class _ParameterListBase(MutableSequence, Generic[ParameterType, BodyParameterType]):  # pylint: disable=too-many-public-methods
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        parameters: List[ParameterType],
        body_parameter: Optional[BodyParameterType] = None,
    ) -> None:
        self.yaml_data = yaml_data
        self.code_model = code_model
        self.parameters = parameters or []
        self._body_parameter = body_parameter

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

    def insert(self, index: int, value: ParameterType) -> None:
        self.parameters.insert(index, value)

    # Parameter helpers


    @staticmethod
    @abstractmethod
    def parameter_creator() -> Type[ParameterType]:
        ...

    @staticmethod
    @abstractmethod
    def body_parameter_creator() -> Type[BodyParameterType]:
        ...

    @property
    def has_body(self) -> bool:
        return bool(self._body_parameter)

    @property
    def path(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location in (ParameterLocation.PATH, ParameterLocation.ENDPOINT_PATH)]

    @property
    def query(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location == ParameterLocation.QUERY]

    @property
    def headers(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.location == ParameterLocation.HEADER]

    @property
    def grouped(self) -> List[ParameterType]:
        raise NotImplementedError("No parameter grouping")

    @property
    def groupers(self) -> List[ParameterType]:
        raise NotImplementedError("No parameter grouping")

    @property
    def constant(self) -> List[ParameterType]:
        return [p for p in self.parameters if p.constant]

    @property
    def positional(self) -> List[Union[ParameterType, BodyParameterType]]:
        return _sort([
            p for p in self.unsorted_method_params if p.method_location == ParameterMethodLocation.POSITIONAL
        ])

    @property
    def keyword_only(self) -> List[Union[ParameterType, BodyParameterType]]:
        return _sort([
            p for p in self.unsorted_method_params if p.method_location == ParameterMethodLocation.KEYWORD_ONLY
        ])

    @property
    def kwarg(self) -> List[Union[ParameterType, BodyParameterType]]:
        return _sort([
            p for p in self.unsorted_method_params if p.method_location == ParameterMethodLocation.KWARG
        ])

    @property
    @abstractmethod
    def implementation(self) -> str:
        ...

    @property
    def unsorted_method_params(self) -> List[Union[ParameterType, BodyParameterType]]:
        method_params: List[Union[ParameterType, BodyParameterType]] = [p for p in self.parameters if p.in_method_signature and p.implementation == self.implementation]
        if self._body_parameter:
            method_params.append(self._body_parameter)
        return method_params

    @property
    def method(self) -> List[Union[ParameterType, BodyParameterType]]:
        return self.positional + self.keyword_only + self.kwarg

    def method_signature(self, is_python3_file: bool) -> List[str]:
        return method_signature_helper(
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

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Union[ParameterType, BodyParameterType]]:
        kwargs_to_pop = [p for p in self.method if p.method_location == ParameterMethodLocation.KWARG]
        if not is_python3_file:
            kwargs_to_pop += [p for p in self.method if p.method_location == ParameterMethodLocation.KEYWORD_ONLY]
        return kwargs_to_pop

    @property
    def call(self) -> List[str]:
        retval = [p.client_name for p in self.method if p.method_location == ParameterMethodLocation.POSITIONAL]
        retval.extend(
            [f"{p.client_name}={p.client_name}" for p in self.method if p.method_location == ParameterMethodLocation.KEYWORD_ONLY]
        )
        retval.append("**kwargs")
        return retval

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel"):
        parameters = [
            cls.parameter_creator().from_yaml(parameter, code_model)
            for parameter in yaml_data["parameters"]
        ]
        body_parameter = None
        if yaml_data.get("bodyParameter"):
            body_parameter = cls.body_parameter_creator().from_yaml(yaml_data["bodyParameter"], code_model)
        return cls(
            yaml_data,
            code_model,
            parameters=parameters,
            body_parameter=body_parameter,
        )


class _ParameterList(_ParameterListBase[Parameter, BodyParameter]):

    @staticmethod
    def parameter_creator() -> Type[Parameter]:
        return Parameter

    @staticmethod
    def body_parameter_creator() -> Type[BodyParameter]:
        return BodyParameter

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def path(self) -> List[Parameter]:
        return [k for k in super().path if k.location == ParameterLocation.ENDPOINT_PATH]

    @property
    def body_parameter(self) -> BodyParameter:
        if not self._body_parameter:
            raise ValueError("There is no body parameter")
        return self._body_parameter

class ParameterList(_ParameterList):
    ...

class OverloadedOperationParameterList(_ParameterList):
    """This parameter list is used if we have overloads for an operation due to multiple types of the body parameter"""

    ...

class _RequestBuilderParameterList(_ParameterListBase[RequestBuilderParameter, RequestBuilderBodyParameter]):

    @staticmethod
    def parameter_creator() -> Type[RequestBuilderParameter]:
        return RequestBuilderParameter

    @staticmethod
    def body_parameter_creator() -> Type[RequestBuilderBodyParameter]:
        return RequestBuilderBodyParameter

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def body_parameter(self) -> RequestBuilderBodyParameter:
        if not self._body_parameter:
            raise ValueError("There is no body parameter")
        return self._body_parameter

    @property
    def unsorted_method_params(self) -> List[Union[RequestBuilderParameter, RequestBuilderBodyParameter]]:
        return [k for k in super().unsorted_method_params if k.location != ParameterLocation.ENDPOINT_PATH]

    @property
    def path(self) -> List[RequestBuilderParameter]:
        return [p for p in super().path if p.location != ParameterLocation.ENDPOINT_PATH]


class RequestBuilderParameterList(_RequestBuilderParameterList):
    ...

class OverloadedRequestBuilderParameterList(_RequestBuilderParameterList):

    def method_signature(self, is_python3_file: bool) -> List[str]:
        if self.positional:
            return ["*args", "**kwargs"]
        return ["**kwargs"]

class _ClientGlobalParameterList(_ParameterListBase[ParameterType, BodyParameter]):

    @staticmethod
    def body_parameter_creator() -> Type[BodyParameter]:
        return BodyParameter

    @property
    def implementation(self) -> str:
        return "Client"

    @property
    def credential(self) -> Optional[ParameterType]:
        try:
            return next(p for p in self.parameters if p.client_name == "credential")
        except StopIteration:
            return None

class ClientGlobalParameterList(_ClientGlobalParameterList[ClientParameter]):

    @staticmethod
    def parameter_creator() -> Type[ClientParameter]:
        return ClientParameter

    @property
    def path(self) -> List[ClientParameter]:
        return [p for p in super().path if not p.is_host]

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Union[ClientParameter, BodyParameter]]:
        return [
            k for k in super().kwargs_to_pop(is_python3_file=is_python3_file)
            if k.location == ParameterLocation.ENDPOINT_PATH
        ]


class ConfigGlobalParameterList(_ClientGlobalParameterList[ConfigParameter]):

    @staticmethod
    def parameter_creator() -> Type[ConfigParameter]:
        return ConfigParameter

    @property
    def implementation(self) -> str:
        return "Client"
