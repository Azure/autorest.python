# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from copy import copy
from typing import List, Optional, Tuple, TypeVar, Dict
from .request_builder_parameter import RequestBuilderParameter
from .parameter_list import ParameterList
from .parameter import ParameterLocation, Parameter, ParameterStyle
from .primitive_schemas import AnySchema, JSONSchema
from .dictionary_schema import DictionarySchema
from .base_schema import BaseSchema
from .schema_request import SchemaRequest
from .utils import JSON_REGEXP
from .base_builder import BodyKwargNames

T = TypeVar('T')
OrderedSet = Dict[T, None]


def _kwarg_not_added(body_method_params, serialized_name: str) -> bool:
    return not any(b for b in body_method_params if b.serialized_name == serialized_name)

class RequestBuilderParameterList(ParameterList):
    def __init__(
        self,
        code_model,
        parameters: Optional[List[RequestBuilderParameter]] = None,
    ) -> None:
        super(RequestBuilderParameterList, self).__init__(
            code_model, parameters, # type: ignore
        )
        self.body_kwarg_names: OrderedSet[str] = {}
        self.parameters: List[RequestBuilderParameter] = parameters or []  # type: ignore

    def _change_body_param_name(self, parameter: Parameter, name: str) -> None:
        self.body_kwarg_names[name] = None
        parameter.serialized_name = name
        parameter.is_keyword_only = True
        parameter.flattened = False

    def _add_files_kwarg(
        self, body_param_base
    ) -> RequestBuilderParameter:
        file_kwarg = copy(body_param_base)
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
        return file_kwarg

    def _add_data_kwarg(
        self, body_param_base
    ) -> RequestBuilderParameter:
        data_kwarg = copy(body_param_base)
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
        return data_kwarg

    def _add_json_kwarg(
        self, body_param_base
    ) -> RequestBuilderParameter:
        json_kwarg = copy(body_param_base)
        self._change_body_param_name(json_kwarg, "json")
        json_kwarg.description = (
            "Pass in a JSON-serializable object (usually a dictionary). "
            "See the template in our example to find the input shape. " +
            json_kwarg.description
        )
        json_kwarg.schema = JSONSchema(namespace="", yaml_data={})
        return json_kwarg

    def _add_content_kwarg(
        self, body_method_param
    ) -> RequestBuilderParameter:
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
        return content_kwarg

    def add_body_kwargs(
        self, content_type_to_schema_request: Dict[str, SchemaRequest], body_kwarg_name_to_content_types: Dict[BodyKwargNames, List[str]]
    ) -> None:
        body_kwargs_added: List[RequestBuilderParameter] = []
        body_method_params = [
            p for p in self.parameters
            if p.location == ParameterLocation.Body and not p.constant
        ]
        if not body_method_params:
            return
        for content_type, schema_request in content_type_to_schema_request.items():
            body_param = schema_request.parameters.body[0]
            if body_param.is_multipart and _kwarg_not_added(body_kwargs_added, "files"):
                file_kwarg = self._add_files_kwarg(body_param)
                body_kwargs_added.append(file_kwarg)
            elif body_param.is_data_input and _kwarg_not_added(body_kwargs_added, "data"):
                data_kwarg = self._add_data_kwarg(body_param)
                body_kwargs_added.append(data_kwarg)
            elif content_type in body_kwarg_name_to_content_types.get(BodyKwargNames.JSON, {}) and _kwarg_not_added(body_kwargs_added, "json"):
                json_kwarg = self._add_json_kwarg(body_param)
                body_kwargs_added.append(json_kwarg)
            elif _kwarg_not_added(body_kwargs_added, "content"):
                content_kwarg = self._add_content_kwarg(body_param)
                body_kwargs_added.append(content_kwarg)
        first_body_param = body_method_params[0]
        if _kwarg_not_added(body_kwargs_added, "content"):
            # we always add a content kwarg so users can pass in input by stream
            content_kwarg = self._add_content_kwarg(first_body_param)
            body_kwargs_added.append(content_kwarg)
        if len(body_kwargs_added) == 1:
            body_kwargs_added[0].required = first_body_param.required
        else:
            for kwarg in body_kwargs_added:
                kwarg.required = False
        first_body_param.need_import = False
        self.parameters = body_kwargs_added + self.parameters

    def kwargs_to_pop(self, is_python3_file: bool) -> List[Parameter]:
        # we don't want to pop the body kwargs in py2.7. We send them straight to HttpRequest
        kwargs_to_pop = self.kwargs
        if not is_python3_file:
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
                (parameter.is_data_input or parameter.is_multipart) and
                not parameter.is_keyword_only
            ):
                # if i am a part of files or data, and i'm not the files or
                # data kwarg, ignore me
                continue
            if (
                parameter.location == ParameterLocation.Body and
                not parameter.is_keyword_only and
                not parameter.constant
            ):
                # we keep the original body param from the swagger for documentation purposes
                # we don't want it in the method signature
                continue
            if (
                parameter.location == ParameterLocation.Body and
                parameter.serialized_name not in [k.value for k in BodyKwargNames]
            ):
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
        return signature_parameters

    @staticmethod
    def _wanted_path_parameter(parameter):
        return parameter.location == ParameterLocation.Path
