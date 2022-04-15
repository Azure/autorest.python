# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from copy import copy
from typing import List, Optional, Tuple, TypeVar, Dict, TYPE_CHECKING
from .request_builder_parameter import RequestBuilderParameter
from .parameter_list import ParameterList
from .parameter import (
    ParameterLocation,
    Parameter,
    ParameterMethodLocation,
    ParameterStyle,
)
from .primitive_schemas import AnySchema
from .dictionary_schema import DictionarySchema
from .base_schema import BaseSchema
from .list_schema import ListSchema
from .object_schema import ObjectSchema
from .schema_request import SchemaRequest
from .utils import JSON_REGEXP

if TYPE_CHECKING:
    from .code_model import CodeModel

T = TypeVar("T")
OrderedSet = Dict[T, None]


def _update_content_types(content_types_to_assign: List[str], param: Parameter):
    return [c for c in content_types_to_assign if c not in param.content_types]


def _kwarg_not_added(body_method_params, serialized_name: str) -> bool:
    return not any(
        b for b in body_method_params if b.serialized_name == serialized_name
    )


class RequestBuilderParameterList(ParameterList):
    def __init__(
        self,
        code_model: "CodeModel",
        parameters: Optional[List[RequestBuilderParameter]] = None,
        schema_requests: Optional[List[SchemaRequest]] = None,
    ) -> None:
        super().__init__(code_model, parameters, schema_requests)  # type: ignore
        self.body_kwarg_names: OrderedSet[str] = {}
        self.parameters: List[RequestBuilderParameter] = parameters or []  # type: ignore

    def _change_body_param_name(self, parameter: Parameter, name: str) -> None:
        self.body_kwarg_names[name] = None
        parameter.serialized_name = name
        parameter.is_body_kwarg = True

    def _is_json(self, body_method_param: Parameter) -> bool:
        if "json" in body_method_param.serialization_formats:
            return True
        if not any(
            flag
            for flag in ["version_tolerant", "low_level_client"]
            if self.code_model.options.get(flag)
        ):
            if body_method_param.style == ParameterStyle.binary:
                return False
        if any(
            sr
            for sr in self.schema_requests
            if sr.yaml_data.get("protocol", {}).get("http", {}).get("knownMediaType")
            == "json"
        ):
            return True
        return any(c for c in self.content_types if JSON_REGEXP.match(c))

    @property
    def body_kwargs_to_get(self) -> List[Parameter]:
        if not self.body_kwarg_names:
            return []
        return [b for b in self.body if b.content_types]

    def _update_constant_params(self):
        # we don't currently have a fully constant data or files input
        # so we don't need to modify the body kwarg
        constant_bodies = [
            p
            for p in self.parameters
            if p.location == ParameterLocation.Body and p.constant
        ]
        for constant_body in constant_bodies:
            if self._is_json(constant_body):
                constant_body.serialized_name = "json"
            else:
                constant_body.serialized_name = "content"

    def _add_json_kwarg(
        self, content_types_to_assign, body_method_param
    ) -> Tuple[List[str], RequestBuilderParameter]:
        json_kwarg = copy(body_method_param)
        self._change_body_param_name(json_kwarg, "json")
        json_kwarg.description = (
            "Pass in a JSON-serializable object (usually a dictionary). "
            "See the template in our example to find the input shape. "
            + json_kwarg.description
        )
        if not isinstance(
            body_method_param.schema, (ObjectSchema, DictionarySchema, ListSchema)
        ):
            json_kwarg.schema = AnySchema(yaml_data={}, code_model=self.code_model)
        json_kwarg.content_types = [
            c for c in content_types_to_assign if JSON_REGEXP.match(c)
        ]
        content_types_to_assign = _update_content_types(
            content_types_to_assign, json_kwarg
        )
        return content_types_to_assign, json_kwarg

    def _add_content_kwarg(
        self, content_types_to_assign, body_method_param
    ) -> RequestBuilderParameter:
        content_kwarg = copy(body_method_param)
        self._change_body_param_name(content_kwarg, "content")
        content_kwarg.schema = AnySchema(yaml_data={}, code_model=self.code_model)
        content_kwarg.description = (
            "Pass in binary content you want in the body of the request (typically bytes, "
            "a byte iterator, or stream input). " + content_kwarg.description
        )
        content_kwarg.content_types = content_types_to_assign
        return content_kwarg

    def add_body_kwargs(self) -> None:
        self._update_constant_params()
        body_kwargs_added: List[RequestBuilderParameter] = []
        body_method_params = [
            p
            for p in self.parameters
            if p.location == ParameterLocation.Body
            and not (p.constant or p.is_multipart or p.is_data_input)
        ]
        if not body_method_params:
            return
        content_types_to_assign = copy(self.content_types)
        for body_method_param in body_method_params:
            if self._is_json(body_method_param) and _kwarg_not_added(
                body_kwargs_added, "json"
            ):
                content_types_to_assign, json_kwarg = self._add_json_kwarg(
                    content_types_to_assign, body_method_param
                )
                body_kwargs_added.append(json_kwarg)

        first_body_param = body_method_params[0]
        if _kwarg_not_added(body_kwargs_added, "content"):
            # we always add a content kwarg so users can pass in input by stream
            content_kwarg = self._add_content_kwarg(
                content_types_to_assign, first_body_param
            )
            body_kwargs_added.append(content_kwarg)
        if len(body_kwargs_added) == 1:
            body_kwargs_added[0].required = first_body_param.required
        else:
            for kwarg in body_kwargs_added:
                kwarg.required = False
        first_body_param.need_import = False
        self.parameters = body_kwargs_added + self.parameters

    @property
    def json_body(self) -> BaseSchema:
        if not self._json_body:
            try:
                json_param = next(
                    b for b in self.body if not b.is_body_kwarg and b.is_json_parameter
                )
                self._json_body = json_param.schema
                return self._json_body
            except StopIteration:
                raise ValueError("There is no JSON body in these parameters")
        return self._json_body

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Parameter]:
        # we don't want to pop the body kwargs in py2.7. We send them straight to HttpRequest
        kwargs_to_pop = self.kwargs
        if not is_python3_file:
            kwargs_to_pop += [
                k for k in self.keyword_only if not (k.is_body and not k.constant)
            ]
        return kwargs_to_pop

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature. Includes both positional and kwargs"""
        signature_parameters_no_default_value = []
        signature_parameters_default_value = []

        # Want all method parameters.
        # Also allow client parameters if they're going to be used in the request body.
        # i.e., path parameter, query parameter, header.
        parameters = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation
            or parameter.in_method_code
        )
        seen_content_type = False

        for parameter in parameters:
            if parameter.location == ParameterLocation.Body and (
                parameter.is_multipart or parameter.is_data_input
            ):
                # don't want any multipart for formdata params in our signature
                continue
            if (
                parameter.location == ParameterLocation.Body
                and not parameter.is_body_kwarg
                and not parameter.constant
            ):
                # we keep the original body param from the swagger for documentation purposes
                # we don't want it in the method signature
                continue
            if any(
                [g for g in self.groupers if id(g.yaml_data) == id(parameter.yaml_data)]
            ):
                # we don't allow a grouped parameter for the body param
                continue
            if seen_content_type and parameter.serialized_name == "content_type":
                # we ony want one content type
                # there can be multiple content types in the case of multiple media types
                continue
            if parameter.serialized_name == "content_type":
                seen_content_type = True
            if parameter.in_method_signature:
                if not parameter.default_value and parameter.required:
                    signature_parameters_no_default_value.append(parameter)
                else:
                    signature_parameters_default_value.append(parameter)

        signature_parameters = (
            signature_parameters_no_default_value + signature_parameters_default_value
        )
        signature_parameters.sort(
            key=lambda item: item.method_location
            == ParameterMethodLocation.KEYWORD_ONLY
        )
        signature_parameters = self._filter_out_multiple_content_type(
            signature_parameters
        )
        return signature_parameters

    @staticmethod
    def _wanted_path_parameter(parameter):
        return parameter.location == ParameterLocation.Path
