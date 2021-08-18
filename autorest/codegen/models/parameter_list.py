# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from collections.abc import MutableSequence
from copy import copy
import logging
from typing import cast, List, Callable, Optional, TypeVar, Dict

from .parameter import Parameter, ParameterLocation
from .object_schema import ObjectSchema
from .constant_schema import ConstantSchema
from .base_schema import BaseSchema
from .enum_schema import EnumSchema
from .dictionary_schema import DictionarySchema
from .primitive_schemas import AnySchema, StringSchema

T = TypeVar('T')
OrderedSet = Dict[T, None]

_LOGGER = logging.getLogger(__name__)

def _method_signature_helper(positional: List[str], keyword_only: Optional[List[str]], kwarg_params: List[str]):
    keyword_only = keyword_only or []
    return positional + keyword_only + kwarg_params


class ParameterList(MutableSequence):  # pylint: disable=too-many-public-methods
    def __init__(
        self, parameters: Optional[List[Parameter]] = None
    ) -> None:
        self.parameters = parameters or []
        self._json_body: Optional[BaseSchema] = None
        self._content_types: Optional[List[str]] = None

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

    def has_any_location(self, location: ParameterLocation) -> bool:
        return bool([parameter for parameter in self.parameters if parameter.location == location])

    def get_from_predicate(self, predicate: Callable[[Parameter], bool]) -> List[Parameter]:
        return [parameter for parameter in self.parameters if predicate(parameter)]

    def get_from_location(self, location: ParameterLocation) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: parameter.location == location)

    @property
    def json_body(self) -> BaseSchema:
        if not self._json_body:
            self._json_body = self.body[0].schema
        return self._json_body

    @property
    def has_body(self) -> bool:
        return self.has_any_location(ParameterLocation.Body)

    @property
    def body(self) -> List[Parameter]:
        if not self.has_body:
            raise ValueError(f"Can't get body parameter")
        # Should we check if there is two body? Modeler role right?
        body_params = self.get_from_location(ParameterLocation.Body)
        return body_params

    @staticmethod
    def _wanted_path_parameter(parameter: Parameter):
        # TODO add 'and parameter.location == "Method"' as requirement to this check once
        # I can use send_request on operations.
        # Don't want to duplicate code from send_request.
        return parameter.location == ParameterLocation.Uri and parameter.rest_api_name != "$host"

    @property
    def implementation(self) -> str:
        return "Method"

    @property
    def path(self) -> List[Parameter]:
        return [
            parameter
            for parameter in self.parameters
            if self._wanted_path_parameter(parameter)
        ]

    @property
    def query(self) -> List[Parameter]:
        return self.get_from_location(ParameterLocation.Query)

    @property
    def headers(self) -> List[Parameter]:
        headers = self.get_from_location(ParameterLocation.Header)
        if not headers:
            return headers
        return list({
            header.serialized_name: header
            for header in headers
        }.values())

    @property
    def grouped(self) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: cast(bool, parameter.grouped_by))

    @property
    def groupers(self) -> List[Parameter]:
        groupers: List[Parameter] = []
        for parameter in self.parameters:
            if any([
                p for p in self.grouped
                if p.grouped_by and id(p.grouped_by.yaml_data) == id(parameter.yaml_data)
            ]):
                groupers.append(parameter)
        return groupers

    @property
    def constant(self) -> List[Parameter]:
        """Return the constants of this parameter list.

        This excludes the constant from flatening on purpose, since technically they are not
        constant from this set of parameters, they are constants on the models and hence they do
        not have impact on any generation at this level
        """
        return self.get_from_predicate(
            lambda parameter: parameter.constant
        )

    @property
    def constant_bodies(self) -> List[Parameter]:
        constants = self.constant
        if not constants:
            return []
        return [c for c in constants if c.location == ParameterLocation.Body]

    @property
    def multipart(self) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: parameter.is_multipart)

    @property
    def has_partial_body(self) -> bool:
        return any(self.get_from_predicate(lambda parameter: parameter.is_partial_body))

    @property
    def content_types(self) -> List[str]:
        if self._content_types is not None:
            return self._content_types
        content_type_params = self.get_from_predicate(
            lambda parameter: parameter.serialized_name == "content_type"
        )
        content_types: OrderedSet[str] = {}
        for param in content_type_params:
            if isinstance(param.schema, dict):
                if param.schema.get("value"):
                    content_types[param.schema["value"]["value"]] = None
                if param.schema.get("choices"):
                    for choice in param.schema['choices']:
                        content_types[choice['value']] = None
            elif isinstance(param.schema, ConstantSchema) and param.schema.value:
                content_types[param.schema.value] = None
            elif isinstance(param.schema, EnumSchema):
                # enums
                content_types.update({v.value: None for v in param.schema.values})
            if param.client_default_value:
                content_types.update({param.client_default_value: None})
        self._content_types = [k for k in content_types if k is not None]
        return self._content_types

    @property
    def default_content_type(self) -> str:
        json_content_types = [c for c in self.content_types if "json" in c]
        if json_content_types:
            if "application/json" in json_content_types:
                return "application/json"
            return json_content_types[0]

        xml_content_types = [c for c in self.content_types if "xml" in c]
        if xml_content_types:
            if "application/xml" in xml_content_types:
                return "application/xml"
            return xml_content_types[0]
        return self.content_types[0]

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature.
        """
        # Client level should not be on Method, etc.
        parameters_of_this_implementation = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation
        )
        positional = [p for p in parameters_of_this_implementation if p.is_positional]
        keyword_only = [p for p in parameters_of_this_implementation if p.is_keyword_only]
        kwargs = [p for p in parameters_of_this_implementation if p.is_kwarg]
        def _sort(params):
            return sorted(params, key=lambda x: not x.default_value and x.required, reverse=True)
        signature_parameters = (
            _sort(positional) + _sort(keyword_only) + _sort(kwargs)
        )
        return signature_parameters


    def method_signature(self, is_python_3_file: bool) -> List[str]:
        return _method_signature_helper(
            positional=self.method_signature_positional(is_python_3_file),
            keyword_only=self.method_signature_keyword_only(is_python_3_file),
            kwarg_params=self.method_signature_kwargs(is_python_3_file)
        )

    def method_signature_positional(self, is_python_3_file: bool) -> List[str]:
        return [parameter.method_signature(is_python_3_file) for parameter in self.positional]

    def method_signature_keyword_only(self, is_python_3_file: bool) -> List[str]:
        if not (self.keyword_only and is_python_3_file):
            return []
        return ["*,"] + [parameter.method_signature(is_python_3_file) for parameter in self.keyword_only]

    @staticmethod
    def method_signature_kwargs(is_python_3_file: bool) -> List[str]:
        return ["**kwargs: Any"] if is_python_3_file else ["**kwargs  # type: Any"]

    @property
    def positional(self) -> List[Parameter]:
        return [p for p in self.method if p.is_positional]

    @property
    def keyword_only(self) -> List[Parameter]:
        return [p for p in self.method if p.is_keyword_only]

    @property
    def kwargs(self) -> List[Parameter]:
        return [p for p in self.method if p.is_kwarg]

    def kwargs_to_pop(self, is_python_3_file: bool) -> List[Parameter]:
        kwargs_to_pop = self.kwargs
        if not is_python_3_file:
            kwargs_to_pop += self.keyword_only
        return kwargs_to_pop

    @property
    def call(self) -> List[str]:
        retval = [
            p.serialized_name for p in self.positional
        ]
        retval.extend([
            f"{p.serialized_name}={p.serialized_name}"
            for p in self.keyword_only
        ])
        retval.append("**kwargs")
        return retval

    @property
    def is_flattened(self) -> bool:
        return cast(bool, self.get_from_predicate(lambda parameter: parameter.flattened))

    def build_flattened_object(self) -> str:
        if not self.is_flattened:
            raise ValueError("This method can't be called if the operation doesn't need parameter flattening")

        parameters = self.get_from_predicate(
            lambda parameter: parameter.in_method_code
        )
        parameter_string = ", ".join(
            [f"{param.target_property_name}={param.serialized_name}"
            for param in parameters if param.target_property_name
            ]
        )
        object_schema = cast(ObjectSchema, self.body[0].schema)
        return f"{self.body[0].serialized_name} = _models.{object_schema.name}({parameter_string})"

class ParameterOnlyPathAndBodyPositionalList(ParameterList):
    # use this to change the files parameter in the method

    @property
    def method(self) -> List[Parameter]:
        method_params = super().method
        files_params = [p for p in method_params if p.is_multipart]
        if not files_params:
            return method_params
        files_param = copy(files_params[0])
        files_param.serialized_name = "files"
        files_param.schema = DictionarySchema(
            namespace="",
            yaml_data={},
            element_type=AnySchema(namespace="", yaml_data={}),
        )
        files_param.description = (
            "Multipart input for files. See the template in our example to find the input shape."
        )
        method_params = [p for p in method_params if not p.is_multipart]
        positional = [p for p in method_params if p.is_positional]
        keyword_only = [p for p in method_params if p.is_keyword_only]
        kwargs = [p for p in method_params if p.is_kwarg]
        return positional + [files_param] + keyword_only + kwargs

def get_parameter_list(code_model):
    if code_model.options["only_path_and_body_params_positional"]:
        return ParameterOnlyPathAndBodyPositionalList
    return ParameterList

class GlobalParameterList(ParameterList):

    @property
    def implementation(self) -> str:
        return "Client"

    @property
    def code_model(self):
        try:
            return self._code_model
        except AttributeError:
            raise ValueError("You need to first set the code model")

    @code_model.setter
    def code_model(self, val):
        self._code_model = val

    @property
    def endpoint_name(self) -> str:
        return (
            "endpoint" if self.code_model.options["version_tolerant"]
            or self.code_model.options["low_level_client"]
            else "base_url"
        )

    @staticmethod
    def _wanted_path_parameter(parameter: Parameter) -> bool:
        return (
            parameter.location == ParameterLocation.Uri and
            parameter.implementation == "Client" and
            parameter.rest_api_name != "$host"
        )

    def add_endpoint(self, endpoint_value: Optional[str]) -> None:
        endpoint_param = Parameter(
            yaml_data={},
            schema=StringSchema(namespace="", yaml_data={"type": "str"}),
            rest_api_name=self.endpoint_name,
            serialized_name=self.endpoint_name,
            description="Service URL",
            implementation="Client",
            required=True,
            location=ParameterLocation.Other,
            skip_url_encoding=False,
            constraints=[],
            client_default_value=endpoint_value,
            keyword_only=self.code_model.options["version_tolerant"] or self.code_model.options["low_level_client"],
        )
        self.parameters.append(endpoint_param)

    @property
    def endpoint(self) -> Optional[Parameter]:
        try:
            return next(p for p in self.parameters if p.serialized_name == self.endpoint_name)
        except StopIteration:
            return None

    @property
    def endpoint_value(self) -> Optional[str]:
        if not self.endpoint:
            return None
        return next(p for p in self.parameters if p.serialized_name == self.endpoint_name).default_value_declaration

    @property
    def client_method(self) -> List[Parameter]:
        return self.method

    @property
    def config_method(self) -> List[Parameter]:
        return [p for p in self.method if p.serialized_name != self.endpoint_name]

    def client_method_signature(self, is_python_3_file: bool) -> List[str]:
        return self.method_signature(is_python_3_file)

    def config_method_signature(self, is_python_3_file: bool) -> List[str]:
        positional = [
            p.method_signature(is_python_3_file) for p in self.positional if p.serialized_name != self.endpoint_name
        ]
        keyword_only_params = [p for p in self.keyword_only if p.serialized_name != self.endpoint_name]
        keyword_only_method_signature = (
            ["*,"] +
            [
                p.method_signature(is_python_3_file) for p in keyword_only_params
            ]
        ) if keyword_only_params else []
        return _method_signature_helper(
            positional=positional,
            keyword_only=keyword_only_method_signature,
            kwarg_params=self.method_signature_kwargs(is_python_3_file)
        )
