# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Optional, TypeVar, Dict

from .base_schema import BaseSchema
from .request_builder_parameter import RequestBuilderParameter
from .parameter_list import ParameterList
from .parameter import ParameterLocation, Parameter
from .primitive_schemas import AnySchema, JSONSchema
from .dictionary_schema import DictionarySchema
from .schema_request import SchemaRequest
from .base_builder import BodyKwargNames, ContentTypesContainer

T = TypeVar('T')
OrderedSet = Dict[T, None]


def _kwarg_not_added(body_method_params, serialized_name: str) -> bool:
    return not any(b for b in body_method_params if b.serialized_name == serialized_name)

def _create_request_builder_parameter(
    parameter: Parameter, name: str, schema: BaseSchema, description: str
) -> RequestBuilderParameter:
    parameter.need_import = False
    retval = RequestBuilderParameter(
        code_model=parameter.code_model,
        yaml_data=parameter.yaml_data,
        schema=schema,
        rest_api_name=parameter.rest_api_name,
        serialized_name=name,
        description=description,
        implementation=parameter.implementation,
        required=parameter.required,
        location=parameter.location,
        skip_url_encoding=parameter.skip_url_encoding,
        constraints=parameter.constraints,
        target_property_name=parameter.target_property_name,
        style=parameter.style,
        explode=parameter.explode,
        flattened=False,
        grouped_by=parameter.grouped_by,
        original_parameter=parameter.original_parameter,
        client_default_value=parameter.client_default_value,
        keyword_only=True,
    )
    retval.created_body_kwarg = True
    return retval

def _add_files_kwarg(body_param_base) -> RequestBuilderParameter:
    description = (
        "Multipart input for files. See the template in our example to find the input shape."
    )
    schema = DictionarySchema(
        namespace="",
        yaml_data={},
        element_type=AnySchema(namespace="", yaml_data={}),
    )
    return _create_request_builder_parameter(
        body_param_base, name="files", schema=schema, description=description
    )

def _add_data_kwarg(body_param_base) -> RequestBuilderParameter:
    description = (
        "Pass in dictionary that contains form data to include in the body of the request."
    )
    schema = DictionarySchema(
        namespace="",
        yaml_data={},
        element_type=AnySchema(namespace="", yaml_data={}),
    )
    return _create_request_builder_parameter(
        body_param_base,
        name="data",
        schema=schema,
        description=description,
    )

def _add_json_kwarg(body_param_base) -> RequestBuilderParameter:
    description = (
        "Pass in a JSON-serializable object (usually a dictionary). "
        "See the template in our example to find the input shape. " +
        body_param_base.description
    )
    schema = JSONSchema(namespace="", yaml_data={})
    return _create_request_builder_parameter(
        body_param_base, "json", schema=schema, description=description
    )

def _add_content_kwarg(body_method_param) -> RequestBuilderParameter:
    description = (
        "Pass in binary content you want in the body of the request (typically bytes, "
        "a byte iterator, or stream input)."
    )
    content_kwarg = _create_request_builder_parameter(
        parameter=body_method_param,
        name="content",
        schema=AnySchema(namespace="", yaml_data={}),
        description=description
    )
    return content_kwarg

class RequestBuilderParameterList(ParameterList):
    def __init__(
        self,
        code_model,
        parameters: Optional[List[RequestBuilderParameter]] = None,
    ) -> None:
        super(RequestBuilderParameterList, self).__init__(
            code_model, parameters, # type: ignore
        )
        self.parameters: List[RequestBuilderParameter] = parameters or []  # type: ignore

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
            constant_body.serialized_name = "json"
            constant_body.created_body_kwarg = True

    def add_body_kwargs(
        self,
        content_type_to_schema_request: Dict[str, SchemaRequest],
        body_kwarg_name_to_content_types: Dict[BodyKwargNames, ContentTypesContainer]
    ) -> None:
        self._update_constant_params()
        body_kwargs_added: List[RequestBuilderParameter] = []
        body_method_params = [
            p for p in self.parameters
            if p.location == ParameterLocation.Body and not p.constant
        ]
        if not body_method_params:
            return
        for content_type, schema_request in content_type_to_schema_request.items():
            body_param = schema_request.parameters.body[0]
            json_entry = body_kwarg_name_to_content_types.get(BodyKwargNames.JSON)
            if body_param.is_multipart and _kwarg_not_added(body_kwargs_added, "files"):
                file_kwarg = _add_files_kwarg(body_param)
                body_kwargs_added.append(file_kwarg)
            elif body_param.is_data_input and _kwarg_not_added(body_kwargs_added, "data"):
                data_kwarg = _add_data_kwarg(body_param)
                body_kwargs_added.append(data_kwarg)
            elif (
                json_entry and
                content_type in json_entry.content_types and
                _kwarg_not_added(body_kwargs_added, "json")
            ):
                json_kwarg = _add_json_kwarg(body_param)
                body_kwargs_added.append(json_kwarg)
            elif _kwarg_not_added(body_kwargs_added, "content"):
                content_kwarg = _add_content_kwarg(body_param)
                body_kwargs_added.append(content_kwarg)
        first_body_param = body_method_params[0]
        if _kwarg_not_added(body_kwargs_added, "content") and not first_body_param.constant:
            # we always add a content kwarg so users can pass in input by stream
            content_kwarg = _add_content_kwarg(first_body_param)
            body_kwargs_added.append(content_kwarg)
        if len(body_kwargs_added) == 1:
            body_kwargs_added[0].required = first_body_param.required
        else:
            for kwarg in body_kwargs_added:
                kwarg.required = False
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
                not parameter.created_body_kwarg
            ):
                # we only want the body kwargs we created
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
