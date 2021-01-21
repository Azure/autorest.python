# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, cast, Dict, List, Optional, TypeVar

from .base_model import BaseModel
from .constant_schema import ConstantSchema
from .list_schema import ListSchema
from .parameter import Parameter, ParameterStyle
from .parameter_list import ParameterList
from .schema_request import SchemaRequest
from .imports import FileImport

_M4_HEADER_PARAMETERS = ["content_type", "accept"]

T = TypeVar('T')
OrderedSet = Dict[T, None]

def _non_binary_schema_media_types(media_types: List[str]) -> OrderedSet[str]:
    response_media_types: OrderedSet[str] = {}

    json_media_types = [media_type for media_type in media_types if "json" in media_type]
    xml_media_types = [media_type for media_type in media_types if "xml" in media_type]

    if not sorted(json_media_types + xml_media_types) == sorted(media_types):
        raise ValueError("The non-binary responses with schemas of {self.name} have incorrect json or xml mime types")
    if json_media_types:
        if "application/json" in json_media_types:
            response_media_types["application/json"] = None
        else:
            response_media_types[json_media_types[0]] = None
    if xml_media_types:
        if "application/xml" in xml_media_types:
            response_media_types["application/xml"] = None
        else:
            response_media_types[xml_media_types[0]] = None
    return response_media_types

def _remove_multiple_m4_header_parameters(parameters: List[Parameter]) -> List[Parameter]:
    m4_header_params_in_schema = {
        k: [p for p in parameters if p.serialized_name == k]
        for k in _M4_HEADER_PARAMETERS
    }
    remaining_params = [p for p in parameters if p.serialized_name not in _M4_HEADER_PARAMETERS]
    json_m4_header_params = {
        k: [p for p in m4_header_params_in_schema[k] if p.yaml_data["schema"]["type"] == "constant"]
        for k in m4_header_params_in_schema
    }
    for k, v in json_m4_header_params.items():
        if v:
            remaining_params.append(v[0])
        else:
            remaining_params.append(m4_header_params_in_schema[k][0])

    return remaining_params

class Request(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        url: str,
        method: str,
        multipart: bool,
        schema_requests: List[SchemaRequest],
        parameters: Optional[List[Parameter]] = None,
        multiple_media_type_parameters: Optional[List[Parameter]] = None,
    ):
        super(Request, self).__init__(yaml_data)
        self.name = name
        self.url = url
        self.method = method
        self.multipart = multipart
        self.schema_requests = schema_requests
        self.parameters = ParameterList(parameters)
        self.multiple_media_type_parameters = ParameterList(multiple_media_type_parameters)

    @property
    def content_type(self) -> str:
        return next(iter(
            [
                p.schema.get_declaration(cast(ConstantSchema, p.schema).value)
                for p in self.parameters.constant if p.serialized_name == "content_type"
            ]
        ))

    @property
    def is_stream(self) -> bool:
        """Is the request is a stream, like an upload."""
        return any(request.is_stream_request for request in self.schema_requests)

    @staticmethod
    def build_serialize_data_call(parameter: Parameter, function_name: str) -> str:

        optional_parameters = []

        if parameter.skip_url_encoding:
            optional_parameters.append("skip_quote=True")

        if parameter.style and not parameter.explode:
            if parameter.style in [ParameterStyle.simple, ParameterStyle.form]:
                div_char = ","
            elif parameter.style in [ParameterStyle.spaceDelimited]:
                div_char = " "
            elif parameter.style in [ParameterStyle.pipeDelimited]:
                div_char = "|"
            elif parameter.style in [ParameterStyle.tabDelimited]:
                div_char = "\t"
            else:
                raise ValueError(f"Do not support {parameter.style} yet")
            optional_parameters.append(f"div='{div_char}'")

        if parameter.explode:
            if not isinstance(parameter.schema, ListSchema):
                raise ValueError("Got a explode boolean on a non-array schema")
            serialization_schema = parameter.schema.element_type
        else:
            serialization_schema = parameter.schema

        serialization_constraints = serialization_schema.serialization_constraints
        if serialization_constraints:
            optional_parameters += serialization_constraints

        origin_name = parameter.full_serialized_name

        parameters = [
            f'"{origin_name.lstrip("_")}"',
            "q" if parameter.explode else origin_name,
            f"'{serialization_schema.serialization_type}'",
            *optional_parameters
        ]
        parameters_line = ', '.join(parameters)

        serialize_line = f'self._serialize.{function_name}({parameters_line})'

        if parameter.explode:
            return f"[{serialize_line} if q is not None else '' for q in {origin_name}]"
        return serialize_line

    @property
    def imports(self) -> FileImport:
        file_import = FileImport()
        for parameter in self.parameters:
            file_import.merge(parameter.imports())

        if self.multiple_media_type_parameters:
            for parameter in self.multiple_media_type_parameters:
                file_import.merge(parameter.imports())
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any]) -> "Request":
        operation_name = yaml_data["language"]["python"]["name"]
        name = f"_{operation_name}_request"

        first_request = yaml_data["requests"][0]

        multiple_requests = len(yaml_data["requests"]) > 1

        multiple_media_type_parameters: List[Parameter] = []
        parameters = [Parameter.from_yaml(yaml) for yaml in yaml_data.get("parameters", [])]

        for request in yaml_data["requests"]:
            for yaml in request.get("parameters", []):
                parameter = Parameter.from_yaml(yaml)
                if yaml["language"]["python"]["name"] in _M4_HEADER_PARAMETERS:
                    parameter.is_kwarg = True
                    parameters.append(parameter)
                elif multiple_requests:
                    multiple_media_type_parameters.append(parameter)
                else:
                    parameters.append(parameter)

        if multiple_requests:
            parameters = _remove_multiple_m4_header_parameters(parameters)
            chosen_parameter = multiple_media_type_parameters[0]

            # binary body parameters are required, while object
            # ones are not. We default to optional in this case.
            optional_parameters = [p for p in multiple_media_type_parameters if not p.required]
            if optional_parameters:
                chosen_parameter = optional_parameters[0]
            else:
                chosen_parameter = multiple_media_type_parameters[0]
            chosen_parameter.has_multiple_media_types = True
            parameters.append(chosen_parameter)

        if multiple_media_type_parameters:
            body_parameters_name_set = set(
                p.serialized_name for p in multiple_media_type_parameters
            )
            if len(body_parameters_name_set) > 1:
                raise ValueError(
                f"The body parameter with multiple media types has different names: {body_parameters_name_set}"
            )


        parameters_index = {id(parameter.yaml_data): parameter for parameter in parameters}

        # Need to connect the groupBy and originalParameter
        for parameter in parameters:
            parameter_grouped_by_id = id(parameter.grouped_by)
            if parameter_grouped_by_id in parameters_index:
                parameter.grouped_by = parameters_index[parameter_grouped_by_id]

            parameter_original_id = id(parameter.original_parameter)
            if parameter_original_id in parameters_index:
                parameter.original_parameter = parameters_index[parameter_original_id]

        return cls(
            yaml_data=yaml_data,
            name=name,
            url=first_request["protocol"]["http"]["path"],
            method=first_request["protocol"]["http"]["method"],
            multipart=first_request["protocol"]["http"].get("multipart", False),
            schema_requests=[SchemaRequest.from_yaml(yaml) for yaml in yaml_data["requests"]],
            parameters=parameters,
            multiple_media_type_parameters=multiple_media_type_parameters,
        )
