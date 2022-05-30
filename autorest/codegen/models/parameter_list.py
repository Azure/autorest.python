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
    Optional,
    TYPE_CHECKING,
    Union,
    Generic,
    TypeVar,
    cast,
)
from abc import abstractmethod
from collections.abc import MutableSequence
from enum import Enum

from .request_builder_parameter import (
    RequestBuilderBodyParameter,
    RequestBuilderMultipartBodyParameter,
    RequestBuilderParameter,
    get_request_body_parameter,
)
from .parameter import (
    MultipartBodyParameter,
    ParameterLocation,
    BodyParameter,
    Parameter,
    ParameterMethodLocation,
    ClientParameter,
    ConfigParameter,
    get_body_parameter,
)

ParameterType = TypeVar(
    "ParameterType", bound=Union[Parameter, RequestBuilderParameter]
)
BodyParameterType = TypeVar(
    "BodyParameterType", bound=Union[BodyParameter, RequestBuilderBodyParameter]
)
RequestBuilderBodyParameterType = Union[
    RequestBuilderBodyParameter, RequestBuilderMultipartBodyParameter
]


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


class _ParameterListBase(
    MutableSequence, Generic[ParameterType, BodyParameterType]
):  # pylint: disable=too-many-public-methods
    """Base class for all of our different ParameterList classes"""

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
    def parameter_creator() -> Callable[[Dict[str, Any], "CodeModel"], ParameterType]:
        """Callable for creating parameters"""
        ...

    @staticmethod
    @abstractmethod
    def body_parameter_creator() -> Callable[
        [Dict[str, Any], "CodeModel"], BodyParameterType
    ]:
        """Callable for creating body parameters"""
        ...

    @property
    def grouped(self) -> List[Union[ParameterType, BodyParameterType]]:
        """All parameters that are inside a parameter group"""
        params: List[Union[ParameterType, BodyParameterType]] = [
            p for p in self.parameters if p.grouped_by
        ]
        if self.has_body and self.body_parameter.grouped_by:
            params.append(self.body_parameter)
        return params

    @property
    def has_body(self) -> bool:
        """Whether there is a body parameter in the parameter list"""
        return bool(self._body_parameter)

    @property
    def path(self) -> List[ParameterType]:
        """All path parameters"""
        return [
            p
            for p in self.parameters
            if p.location in (ParameterLocation.PATH, ParameterLocation.ENDPOINT_PATH)
        ]

    @property
    def query(self) -> List[ParameterType]:
        """All query parameters"""
        return [p for p in self.parameters if p.location == ParameterLocation.QUERY]

    @property
    def headers(self) -> List[ParameterType]:
        """All header parameters"""
        return [p for p in self.parameters if p.location == ParameterLocation.HEADER]

    @property
    def constant(self) -> List[Union[ParameterType, BodyParameterType]]:
        """All constant parameters"""
        return [p for p in self.parameters if p.constant]

    @property
    def positional(self) -> List[Union[ParameterType, BodyParameterType]]:
        """All positional parameters"""
        return _sort(
            [
                p
                for p in self.unsorted_method_params
                if p.method_location == ParameterMethodLocation.POSITIONAL
            ]
        )

    @property
    def keyword_only(self) -> List[Union[ParameterType, BodyParameterType]]:
        """All keyword only parameters"""
        return _sort(
            [
                p
                for p in self.unsorted_method_params
                if p.method_location == ParameterMethodLocation.KEYWORD_ONLY
            ]
        )

    @property
    def kwarg(self) -> List[Union[ParameterType, BodyParameterType]]:
        """All kwargs"""
        return _sort(
            [
                p
                for p in self.unsorted_method_params
                if p.method_location == ParameterMethodLocation.KWARG
            ]
        )

    @property
    def body_parameter(self) -> BodyParameterType:
        """The body parameter of the parameter list. Will only ever be at most one."""
        if not self._body_parameter:
            raise ValueError("There is no body parameter")
        return self._body_parameter

    @property
    @abstractmethod
    def implementation(self) -> str:
        """Whether this is a client or a method parameter"""
        ...

    @property
    def unsorted_method_params(self) -> List[Union[ParameterType, BodyParameterType]]:
        """Method params before sorting"""
        method_params: List[Union[ParameterType, BodyParameterType]] = [
            p
            for p in self.parameters
            if p.in_method_signature and p.implementation == self.implementation
        ]
        if self._body_parameter:
            if self._body_parameter.in_method_signature:
                method_params.append(self._body_parameter)
            try:
                # i am a multipart body parameter
                # Only legacy generates operations with me, so I will follow the legacy rules
                # I will splat out my entries as individual entries
                method_params.extend(self._body_parameter.entries)  # type: ignore
            except AttributeError:
                pass
        return method_params

    @property
    def method(self) -> List[Union[ParameterType, BodyParameterType]]:
        """Sorted method params. First positional, then keyword only, then kwarg"""
        return self.positional + self.keyword_only + self.kwarg

    def method_signature(self, is_python3_file: bool, async_mode: bool) -> List[str]:
        """Method signature for this parameter list."""
        return method_signature_helper(
            positional=self.method_signature_positional(is_python3_file, async_mode),
            keyword_only=self.method_signature_keyword_only(
                is_python3_file, async_mode
            ),
            kwarg_params=self.method_signature_kwargs(is_python3_file),
        )

    def method_signature_positional(
        self, is_python3_file: bool, async_mode: bool
    ) -> List[str]:
        """Signature for positional parameters"""
        return [
            parameter.method_signature(is_python3_file, async_mode)
            for parameter in self.positional
        ]

    def method_signature_keyword_only(
        self, is_python3_file: bool, async_mode: bool
    ) -> List[str]:
        """Signature for keyword only parameters"""
        if not (self.keyword_only and is_python3_file):
            return []
        return ["*,"] + [
            parameter.method_signature(is_python3_file, async_mode)
            for parameter in self.keyword_only
        ]

    @staticmethod
    def method_signature_kwargs(is_python3_file: bool) -> List[str]:
        """Signature for kwargs"""
        return ["**kwargs: Any"] if is_python3_file else ["**kwargs  # type: Any"]

    def kwargs_to_pop(
        self, is_python3_file: bool
    ) -> List[Union[ParameterType, BodyParameterType]]:
        """Method kwargs we want to pop"""
        # don't want to pop bodies unless it's a constant
        kwargs_to_pop = self.kwarg
        if not is_python3_file:
            kwargs_to_pop += self.keyword_only
        return [
            k
            for k in kwargs_to_pop
            if k.location != ParameterLocation.BODY or k.constant
        ]

    @property
    def call(self) -> List[str]:
        """How to pass in parameters to call the operation"""
        retval = [
            p.client_name
            for p in self.method
            if p.method_location == ParameterMethodLocation.POSITIONAL
        ]
        retval.extend(
            [
                f"{p.client_name}={p.client_name}"
                for p in self.method
                if p.method_location == ParameterMethodLocation.KEYWORD_ONLY
            ]
        )
        retval.append("**kwargs")
        return retval

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel"):
        parameters = [
            cls.parameter_creator()(parameter, code_model)
            for parameter in yaml_data["parameters"]
        ]
        body_parameter = None
        if yaml_data.get("bodyParameter"):
            body_parameter = cls.body_parameter_creator()(
                yaml_data["bodyParameter"], code_model
            )
        return cls(
            yaml_data,
            code_model,
            parameters=parameters,
            body_parameter=body_parameter,
        )

    def has_several_content_types(self, overloads_parameters: List) -> bool:
        content_types = set()
        all_parameters = [self, *overloads_parameters]
        for p in all_parameters:
            try:
                content_types.update(p.body_parameter.content_types)
            except ValueError:
                pass  # ignore if there is no body_parameter
        return len(content_types) > 2


class _ParameterList(
    _ParameterListBase[  # pylint: disable=unsubscriptable-object
        Parameter, Union[MultipartBodyParameter, BodyParameter]
    ]
):
    """Base Parameter class for the two operation ParameterLists"""

    @staticmethod
    def parameter_creator() -> Callable[[Dict[str, Any], "CodeModel"], Parameter]:
        return Parameter.from_yaml

    @staticmethod
    def body_parameter_creator() -> Callable[
        [Dict[str, Any], "CodeModel"], Union[MultipartBodyParameter, BodyParameter]
    ]:
        return get_body_parameter

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def path(self) -> List[Parameter]:
        return [
            k for k in super().path if k.location == ParameterLocation.ENDPOINT_PATH
        ]


class ParameterList(_ParameterList):
    """ParameterList is the parameter list for Operation classes"""

    ...


class _RequestBuilderParameterList(
    _ParameterListBase[  # pylint: disable=unsubscriptable-object
        RequestBuilderParameter, RequestBuilderBodyParameterType
    ]
):
    """_RequestBuilderParameterList is base parameter list for RequestBuilder classes"""

    @staticmethod
    def parameter_creator() -> Callable[
        [Dict[str, Any], "CodeModel"], RequestBuilderParameter
    ]:
        return RequestBuilderParameter.from_yaml

    @staticmethod
    def body_parameter_creator() -> Callable[
        [Dict[str, Any], "CodeModel"], RequestBuilderBodyParameterType
    ]:
        return get_request_body_parameter

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def unsorted_method_params(
        self,
    ) -> List[Union[RequestBuilderParameter, RequestBuilderBodyParameterType]]:
        # don't have access to client params in request builder
        retval = [
            p
            for p in super().unsorted_method_params
            if not (
                p.location == ParameterLocation.BODY
                and cast(RequestBuilderBodyParameterType, p).is_partial_body
            )
        ]
        retval.extend(
            [
                p
                for p in self.parameters
                if p.implementation == "Client" and p.in_method_signature
            ]
        )
        return retval

    @property
    def path(self) -> List[RequestBuilderParameter]:
        return [
            p for p in super().path if p.location != ParameterLocation.ENDPOINT_PATH
        ]


class RequestBuilderParameterList(_RequestBuilderParameterList):
    """Parameter list for Request Builder"""

    ...


class OverloadedRequestBuilderParameterList(_RequestBuilderParameterList):
    """Parameter list for OverloadedRequestBuilder"""

    def method_signature(self, is_python3_file: bool, async_mode: bool) -> List[str]:
        return self.method_signature_positional(
            is_python3_file, async_mode
        ) + self.method_signature_kwargs(is_python3_file)


class _ClientGlobalParameterList(
    # pylint: disable=unsubscriptable-object
    _ParameterListBase[ParameterType, BodyParameter]
):
    """Base parameter list for client and config classes"""

    @staticmethod
    def body_parameter_creator() -> Callable[
        [Dict[str, Any], "CodeModel"], BodyParameter
    ]:
        return BodyParameter.from_yaml

    @property
    def implementation(self) -> str:
        return "Client"

    @property
    def credential(self) -> Optional[ParameterType]:
        try:
            return next(p for p in self.parameters if p.client_name == "credential")
        except StopIteration:
            return None

    @property
    def path(self) -> List[ParameterType]:
        return [
            p for p in super().path if p.location == ParameterLocation.ENDPOINT_PATH
        ]


class ClientGlobalParameterList(_ClientGlobalParameterList[ClientParameter]):
    """Parameter list for Client class"""

    @staticmethod
    def parameter_creator() -> Callable[[Dict[str, Any], "CodeModel"], ClientParameter]:
        return ClientParameter.from_yaml

    @property
    def path(self) -> List[ClientParameter]:
        return [p for p in super().path if not p.is_host]

    @property
    def host(self) -> Optional[ClientParameter]:
        """Get the host parameter"""
        try:
            return next(p for p in self.parameters if p.is_host)
        except StopIteration:
            return None

    def kwargs_to_pop(
        self, is_python3_file: bool
    ) -> List[Union[ClientParameter, BodyParameter]]:
        """We only want to pass base url path parameters in the client"""
        return [
            k
            for k in super().kwargs_to_pop(is_python3_file=is_python3_file)
            if k.location == ParameterLocation.ENDPOINT_PATH
        ]


class ConfigGlobalParameterList(_ClientGlobalParameterList[ConfigParameter]):
    """Parameter list for config"""

    @staticmethod
    def parameter_creator() -> Callable[[Dict[str, Any], "CodeModel"], ConfigParameter]:
        return ConfigParameter.from_yaml

    @property
    def implementation(self) -> str:
        return "Client"
