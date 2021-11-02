# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from copy import copy
from typing import List, Optional, TypeVar, Dict
from .request_builder_parameter import RequestBuilderParameter
from .parameter_list import ParameterList
from .parameter import ParameterLocation, Parameter, ParameterStyle
from .primitive_schemas import AnySchema
from .dictionary_schema import DictionarySchema
from .base_schema import BaseSchema
from .schema_request import SchemaRequest

T = TypeVar('T')
OrderedSet = Dict[T, None]

_REQUEST_BUILDER_BODY_NAMES = ["files", "json", "content", "data"]
_JSON_REGEXP = re.compile(r'^(application|text)/([0-9a-z+.]+\+)?json$')

def _update_content_types(content_types_to_assign: List[str], param: Parameter):
    return [
        c for c in content_types_to_assign if c not in param.content_types
    ]

class RequestBuilderParameterList(ParameterList):
    def __init__(
        self,
        code_model,
        parameters: Optional[List[RequestBuilderParameter]] = None,
        schema_requests: Optional[List[SchemaRequest]] = None,
    ) -> None:
        super(RequestBuilderParameterList, self).__init__(
            code_model, parameters, schema_requests  # type: ignore
        )
        self.body_kwarg_names: OrderedSet[str] = {}
        self.parameters: List[RequestBuilderParameter] = parameters or []  # type: ignore

    def _change_body_param_name(self, parameter: Parameter, name: str) -> None:
        self.body_kwarg_names[name] = None
        parameter.serialized_name = name

    def _is_json(self, body_method_param: Parameter) -> bool:
        if 'json' in body_method_param.serialization_formats:
            return True
        if not any(
            flag for flag in ["version_tolerant", "low_level_client"]
            if self.code_model.options.get(flag)
        ):
            if body_method_param.style == ParameterStyle.binary:
                return False
        if any(
            sr for sr in self.schema_requests
            if sr.yaml_data.get("protocol", {}).get('http', {}).get('knownMediaType') == "json"
        ):
            return True
        return any(c for c in self.content_types if _JSON_REGEXP.match(c))

    @property
    def body_kwargs_to_get(self) -> List[Parameter]:
        if not self.body_kwarg_names:
            return []
        return [b for b in self.body if b.content_types]

    def _update_constant_params(self):
        # we don't currently have a fully constant data or files input
        # so we don't need to modify the body kwarg
        constant_bodies = [
            p for p in self.parameters
            if p.location == ParameterLocation.Body
            and p.constant
            and not p.is_data_input
            and not p.is_multipart
        ]
        for constant_body in constant_bodies:
            if self._is_json(constant_body):
                constant_body.serialized_name = "json"
            else:
                constant_body.serialized_name = "content"

    def add_body_kwargs(self) -> None:
        self._update_constant_params()
        try:
            body_kwargs_added = []
            body_method_param = next(
                p for p in self.parameters
                if p.location == ParameterLocation.Body and not p.constant
            )
        except StopIteration:
            pass
        else:
            content_types_to_assign = copy(self.content_types)
            if body_method_param.is_multipart:
                file_kwarg = copy(body_method_param)
                self._change_body_param_name(file_kwarg, "files")
                file_kwarg.schema = DictionarySchema(
                    namespace="",
                    yaml_data={},
                    element_type=AnySchema(namespace="", yaml_data={}),
                )
                file_kwarg.description = (
                    "Multipart input for files. See the template in our example to find the input shape. " +
                    file_kwarg.description
                )
                file_kwarg.is_multipart = False
                file_kwarg.content_types = [
                    c for c in content_types_to_assign
                    if c == "multipart/form-data"
                ]
                content_types_to_assign = _update_content_types(content_types_to_assign, file_kwarg)
                body_kwargs_added.append(file_kwarg)
            if body_method_param.is_data_input:
                data_kwarg = copy(body_method_param)
                self._change_body_param_name(data_kwarg, "data")
                data_kwarg.schema = DictionarySchema(
                    namespace="",
                    yaml_data={},
                    element_type=AnySchema(namespace="", yaml_data={}),
                )
                data_kwarg.description = (
                    "Pass in dictionary that contains form data to include in the body of the request. " +
                    data_kwarg.description
                )
                data_kwarg.is_data_input = False
                data_kwarg.content_types = [
                    c for c in content_types_to_assign
                    if c == "application/x-www-form-urlencoded"
                ]
                content_types_to_assign = _update_content_types(content_types_to_assign, data_kwarg)
                body_kwargs_added.append(data_kwarg)
            if self._is_json(body_method_param):
                json_kwarg = copy(body_method_param)
                self._change_body_param_name(json_kwarg, "json")
                json_kwarg.description = (
                    "Pass in a JSON-serializable object (usually a dictionary). "
                    "See the template in our example to find the input shape. " +
                    json_kwarg.description
                )
                json_kwarg.schema = AnySchema(namespace="", yaml_data={})
                json_kwarg.content_types = [
                    c for c in content_types_to_assign
                    if _JSON_REGEXP.match(c)
                ]
                content_types_to_assign = _update_content_types(content_types_to_assign, json_kwarg)
                body_kwargs_added.append(json_kwarg)

            content_kwarg = copy(body_method_param)
            self._change_body_param_name(content_kwarg, "content")
            content_kwarg.schema = AnySchema(namespace="", yaml_data={})
            content_kwarg.description = (
                "Pass in binary content you want in the body of the request (typically bytes, "
                "a byte iterator, or stream input). " +
                content_kwarg.description
            )
            content_kwarg.is_data_input = False
            content_kwarg.is_multipart = False
            content_kwarg.content_types = content_types_to_assign
            body_kwargs_added.append(content_kwarg)
            if len(body_kwargs_added) == 1:
                body_kwargs_added[0].required = body_method_param.required
            else:
                for kwarg in body_kwargs_added:
                    kwarg.required = False
            self.parameters = body_kwargs_added + self.parameters

    @property
    def json_body(self) -> BaseSchema:
        if not self._json_body:
            try:
                json_param = next(
                    b for b in self.body if b.serialized_name not in _REQUEST_BUILDER_BODY_NAMES and
                    b.is_json_parameter
                )
                self._json_body = json_param.schema
                return self._json_body
            except StopIteration:
                raise ValueError("There is no JSON body in these parameters")
        return self._json_body

    def kwargs_to_pop(self, is_python_3_file: bool) -> List[Parameter]:
        # we don't want to pop the body kwargs in py2.7. We send them straight to HttpRequest
        kwargs_to_pop = self.kwargs
        if not is_python_3_file:
            kwargs_to_pop += [k for k in self.keyword_only if not (k.is_body and not k.constant)]
        return kwargs_to_pop

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature. Includes both positional and kwargs
        """
        signature_parameters_no_default_value = []
        signature_parameters_default_value = []

        # Want all method parameters.
        # Also allow client parameters if they're going to be used in the request body.
        # i.e., path parameter, query parameter, header.
        parameters = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation or parameter.in_method_code
        )
        seen_content_type = False

        for parameter in parameters:
            if (
                parameter.location == ParameterLocation.Body and
                parameter.serialized_name not in _REQUEST_BUILDER_BODY_NAMES
            ):
                # we keep the original body param from the swagger for documentation purposes
                # we don't want it in the method signature
                continue
            if any([g for g in self.groupers if id(g.yaml_data) == id(parameter.yaml_data)]):
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

        signature_parameters = signature_parameters_no_default_value + signature_parameters_default_value
        signature_parameters.sort(key=lambda item: item.is_keyword_only)
        signature_parameters = self._filter_out_multiple_content_type(signature_parameters)
        return signature_parameters

    @staticmethod
    def _wanted_path_parameter(parameter):
        return parameter.location == ParameterLocation.Path
