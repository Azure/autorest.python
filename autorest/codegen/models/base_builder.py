# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import abstractmethod
from typing import Any, Dict, List, Optional, TypeVar, Union, TYPE_CHECKING, Generic
from .base_model import BaseModel
from .parameter_list import (
    ParameterList,
    RequestBuilderParameterList,
    OverloadedOperationParameterList,
    OverloadedRequestBuilderParameterList,
)

ParameterListType = TypeVar(
    "ParameterListType",
    bound=Union[
        ParameterList,
        RequestBuilderParameterList,
        OverloadedOperationParameterList,
        OverloadedRequestBuilderParameterList,
    ],
)


if TYPE_CHECKING:
    from .code_model import CodeModel
    from .operation import Operation
    from .request_builder import RequestBuilder


class BaseBuilder(BaseModel, Generic[ParameterListType]):
    """Base class for Operations and Request Builders"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        parameters: ParameterListType,
        *,
        overloads=None,
        abstract: bool = False,
        want_tracing: bool = True,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name = name
        self._description: str = yaml_data.get("description", "")
        self.parameters = parameters
        self.overloads: Union[List["Operation"], List["RequestBuilder"]] = (
            overloads or []
        )
        self._summary: str = yaml_data.get("summary", "")
        # for operations where we don't know what to do, we mark them as abstract so users implement
        # in patch.py
        self.abstract = abstract
        self.want_tracing = want_tracing
        self.group_name: str = yaml_data["groupName"]
        self.is_overload: bool = yaml_data["isOverload"]

    @property
    def summary(self) -> Optional[str]:
        if self.abstract:
            return None
        return self._summary

    @abstractmethod
    def response_type_annotation(self, **kwargs) -> str:
        ...

    @abstractmethod
    def response_docstring_text(self, **kwargs) -> str:
        ...

    @abstractmethod
    def response_docstring_type(self, **kwargs) -> str:
        ...

    @property
    def description(self) -> str:
        if self.abstract:
            return (
                f'You need to write a custom operation for "{self.name}". Please refer to '
                "https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
            )
        return self._description or self.name

    def method_signature(self, is_python3_file: bool) -> List[str]:
        if self.abstract:
            return ["*args,", "**kwargs"]
        return self.parameters.method_signature(is_python3_file)
