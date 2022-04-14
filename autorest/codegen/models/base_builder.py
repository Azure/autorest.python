# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, Tuple, cast, TypeVar, Union, TYPE_CHECKING, NamedTuple, Generic
from .base_model import BaseModel
from .parameter import (
    Parameter, BodyParameter, OverloadBodyParameter
)
from .parameter_list import ParameterList, OverloadBaseParameterList, RequestBuilderParameterList, BodyParameterType
from .request_builder_parameter import RequestBuilderBodyParameter, RequestBuilderOverloadBodyParameter, RequestBuilderParameter

ParameterListType = TypeVar("ParameterListType", bound=Union[ParameterList, RequestBuilderParameterList])
OverloadBodyParameterType = TypeVar(
    "OverloadBodyParameterType", bound=Union[OverloadBodyParameter, RequestBuilderOverloadBodyParameter], contravariant=True
)


if TYPE_CHECKING:
    from .code_model import CodeModel

class BaseBuilder(BaseModel, Generic[ParameterListType]):
    """Base class for Operations and Request Builders"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        parameters: ParameterListType,
        overloads,
        *,
        abstract: bool = False,
        want_tracing: bool = True,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name = name
        self._description = yaml_data.get("description", "")
        self.parameters = parameters
        self.overloads = overloads
        self._summary = yaml_data.get("summary", "")
        # for operations where we don't know what to do, we mark them as abstract so users implement
        # in patch.py
        self.abstract = abstract
        self.want_tracing = want_tracing
        self.group_name = yaml_data["groupName"]

    @staticmethod
    def create_parameters_and_overloads(
        yaml_data: Dict[str, Any], code_model: "CodeModel", is_operation: bool
    ) -> Tuple[ParameterListType, List[OverloadBodyParameterType]]:
        parameter_creator = Parameter if is_operation else RequestBuilderParameter
        parameters = [parameter_creator.from_yaml(p, code_model) for p in yaml_data["parameters"]]
        body_parameter_creator = BodyParameter if is_operation else RequestBuilderBodyParameter
        body_parameter = body_parameter_creator.from_yaml(yaml_data["bodyParameter"], code_model) if yaml_data.get("bodyParameter") else None
        overload_body_parameters: List[OverloadBodyParameterType] = []
        if body_parameter and len(body_parameter.types) > 1:
            # we have overloads now, one for each type
            parameter_list_creator = OverloadBaseParameterList if is_operation else ParameterList
            parameter_list = parameter_list_creator(code_model, parameters, body_parameter=body_parameter)
            for type in body_parameter.types:
                overload_body_parameter_creator = OverloadBodyParameter if is_operation else RequestBuilderOverloadBodyParameter
                overload_body_parameters.append(cast(OverloadBodyParameterType, overload_body_parameter_creator(
                    body_parameter.yaml_data,
                    body_parameter.code_model,
                    type=type,
                    content_types=body_parameter.type_to_content_types(id(type.yaml_data))
                )))
        else:
            parameter_list = ParameterList(code_model, parameters, body_parameter=body_parameter)
        return parameter_list, overload_body_parameters

    @property
    def summary(self) -> Optional[str]:
        if self.abstract:
            return None
        return self._summary

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
