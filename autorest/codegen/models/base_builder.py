# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, Union, NamedTuple, cast, TYPE_CHECKING
from enum import Enum

from autorest.codegen.models.primitive_schemas import StringSchema
from .base_model import BaseModel
from .schema_response import SchemaResponse
from .schema_request import SchemaRequest
from .parameter import Parameter, ParameterLocation
from .object_schema import ObjectSchema
from .enum_schema import EnumSchema, EnumValue, get_enum_schema
from .constant_schema import ConstantSchema
from .utils import JSON_REGEXP

if TYPE_CHECKING:
    from .code_model import CodeModel

_M4_HEADER_PARAMETERS = ["content_type", "accept"]


class BodyKwargNames(str, Enum):
    JSON = "json"
    CONTENT = "content"
    FILES = "files"
    DATA = "data"

class ContentTypesContainer(NamedTuple):
    default_content_type: str
    content_types: List[str]

def _get_chosen_parameter(overloaded_parameters: List[Parameter], code_model: "CodeModel") -> Parameter:
    """Choose a parameter to elevate to the main operation depending on its location.

    Right now we only see body or header parameters here, may change in the future
    """
    if overloaded_parameters[0].location == ParameterLocation.Body:
        try:
            # get an optional param with object first. These params are the top choice
            # bc they have more info about how to serialize the body
            chosen_parameter = next(
                p for p in overloaded_parameters
                if not p.required and isinstance(p.schema, ObjectSchema)
            )
        except StopIteration:  # pylint: disable=broad-except
            # otherwise, we get the first optional param, if that exists. If not, we just grab the first one
            optional_parameters = [p for p in overloaded_parameters if not p.required]
            chosen_parameter = (
                optional_parameters[0] if optional_parameters else overloaded_parameters[0]
            )
        if not chosen_parameter:
            raise ValueError("You are trying to unify an overloaded parameter but there is no parameter to unify.")
        return chosen_parameter
    else:
        if len(overloaded_parameters) == 1 or overloaded_parameters[0].rest_api_name == "Accept":
            # Currently we don't do different Accept headers
            return overloaded_parameters[0]
        # if it's an enum schema, we default to it.
        try:
            chosen_parameter = next(p for p in overloaded_parameters if isinstance(p.schema, EnumSchema))
        except StopIteration:
            chosen_parameter = overloaded_parameters[0]
        enum_params = [p for p in overloaded_parameters if isinstance(p.schema, EnumSchema)]
        # if there are multiple enums
        if len(enum_params) > 1:
            chosen_parameter = enum_params[0]
            chosen_parameter_schema = cast(EnumSchema, chosen_parameter.schema)
            for enum_param in enum_params[1:]:
                for value in cast(EnumSchema, enum_param).values:
                    if value.name not in [v.name for v in chosen_parameter_schema.values]:
                        chosen_parameter_schema.values.append(value)
        elif enum_params:
            chosen_parameter = enum_params[0]
            chosen_parameter_schema = cast(EnumSchema, chosen_parameter.schema)
            for param in overloaded_parameters:
                if isinstance(param.schema, EnumSchema):
                    continue
                constant_schema = cast(ConstantSchema, param.schema)
                enum_name = cast(str, constant_schema.value).replace("/", "_").upper()
                enum_value = constant_schema.value
                if enum_name not in [v.name for v in chosen_parameter_schema.values]:
                    chosen_parameter_schema.values.append(EnumValue(enum_name, enum_value))
        else:
            chosen_parameter = overloaded_parameters[0]
            values = [
                EnumValue(
                    cast(str, cast(ConstantSchema, param.schema).value).replace("/", "_").upper(),
                    cast(ConstantSchema, param.schema).value,
                )
                for param in overloaded_parameters
            ]
            chosen_parameter.schema = get_enum_schema(code_model)(namespace="", yaml_data={}, description="", name="", values=values, enum_type=StringSchema("", {"type": "str"}))
        return chosen_parameter

def _unify_overloaded_parameters(overloaded_parameters: List[Parameter], code_model: "CodeModel") -> Parameter:
    """Unify the overloaded parameters into one parameter for the main method

    When parameters are overloaded, we need to create one unified
    parameter on the actual function.
    """
    chosen_parameter = _get_chosen_parameter(overloaded_parameters, code_model)
    for param in overloaded_parameters:
        # we don't want to add string if we've already seen enums
        if isinstance(chosen_parameter.schema, EnumSchema) and isinstance(param.schema, ConstantSchema):
            continue
        for type in param.possible_types:
            chosen_parameter.possible_types[type] = None
        for type in param.possible_docstring_types:
            chosen_parameter.possible_docstring_types[type] = None
    return chosen_parameter

def create_parameters(
    yaml_data: Dict[str, Any], code_model, parameter_creator: Callable
):
    multiple_requests = len(yaml_data["requests"]) > 1

    overloaded_parameters_dict: Dict[str, List[Parameter]] = {}
    parameters = [
        parameter_creator(yaml, code_model=code_model)
        for yaml in yaml_data.get("parameters", [])
    ]

    for request in yaml_data["requests"]:
        for yaml in request.get("parameters", []):
            parameter = parameter_creator(yaml, code_model=code_model)
            if multiple_requests:
                parameter.is_overloaded = True
                overloaded_parameters_dict.setdefault(
                    parameter.serialized_name, []
                ).append(parameter)
            else:
                parameters.append(parameter)

    if overloaded_parameters_dict:
        non_header_keys = [k for k in overloaded_parameters_dict.keys() if k not in _M4_HEADER_PARAMETERS]
        if len(non_header_keys) > 1:
            raise ValueError(
            f"The body parameter with multiple media types has different names: {', '.join(non_header_keys)}"
        )
        for _, overloaded_parameters in overloaded_parameters_dict.items():
            parameters.append(_unify_overloaded_parameters(overloaded_parameters, code_model))

    parameters_index = {id(parameter.yaml_data): parameter for parameter in parameters}

    # Need to connect the groupBy and originalParameter
    for parameter in parameters:
        parameter_grouped_by_id = id(parameter.grouped_by)
        if parameter_grouped_by_id in parameters_index:
            parameter.grouped_by = parameters_index[parameter_grouped_by_id]

        parameter_original_id = id(parameter.original_parameter)
        if parameter_original_id in parameters_index:
            parameter.original_parameter = parameters_index[parameter_original_id]

    return parameters

class BaseBuilder(BaseModel):
    """Base class for Operations and Request Builders"""

    def __init__(
        self,
        code_model,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        parameters,
        schema_requests: List[SchemaRequest],
        responses: Optional[List[SchemaResponse]] = None,
        summary: Optional[str] = None,
        *,
        content_type_to_schema_request: Optional[Dict[str, SchemaRequest]] = None,
    ) -> None:
        super().__init__(yaml_data=yaml_data)
        self.code_model = code_model
        self.name = name
        self.description = description
        self.parameters = parameters
        self.responses = responses or []
        self.summary = summary
        self.schema_requests = schema_requests
        self.content_type_to_schema_request = content_type_to_schema_request or {}

    @property
    def body_kwarg_name_to_content_types(self) -> Dict[BodyKwargNames, ContentTypesContainer]:
        # Group the different content types into content type groups based off of request kwarg name
        holder: Dict[BodyKwargNames, List[str]] = {}
        for content_type in self.content_type_to_schema_request.keys():
            if "multipart" in content_type:
                holder.setdefault(BodyKwargNames.FILES, []).append(content_type)
            elif "application/x-www-form-urlencoded" == content_type:
                holder.setdefault(BodyKwargNames.DATA, []).append(content_type)
            elif JSON_REGEXP.match(content_type):
                holder.setdefault(BodyKwargNames.JSON, []).append(content_type)
            else:
                holder.setdefault(BodyKwargNames.CONTENT, []).append(content_type)
        # Now we choose the default content type for each kwarg
        retval: Dict[BodyKwargNames, ContentTypesContainer] = {}
        for body_kwarg_name, content_types in holder.items():
            default_content_type = ""
            if body_kwarg_name == "json":
                json_content_types = [c for c in content_types if JSON_REGEXP.match(c)]
                if "application/json" in json_content_types:
                    default_content_type = "application/json"
                elif json_content_types:
                    default_content_type = json_content_types[0]
                else:
                    default_content_type = content_types[0]
                retval[BodyKwargNames.JSON] = ContentTypesContainer(default_content_type, content_types)
            elif body_kwarg_name == "content":
                xml_content_types = [c for c in content_types if "xml" in c]
                if xml_content_types:
                    if "application/xml" in xml_content_types:
                        default_content_type = "application/xml"
                    elif xml_content_types:
                        default_content_type = xml_content_types[0]
                elif [c for c in content_types if "text/plain" in c]:
                    default_content_type = next(c for c in content_types if "text/plain" in c)
                elif "application/octet-stream" in content_types:
                    default_content_type = "application/octet-stream"
                else:
                    default_content_type = content_types[0]
                retval[BodyKwargNames.CONTENT] = ContentTypesContainer(default_content_type, content_types)
            else:
                retval[body_kwarg_name] = ContentTypesContainer(content_types[0], content_types)
        return retval


    def get_response_from_status(self, status_code: Optional[Union[str, int]]) -> SchemaResponse:
        for response in self.responses:
            if status_code in response.status_codes:
                return response
        raise ValueError(f"Incorrect status code {status_code}, operation {self.name}")

    @property
    def success_status_code(self) -> List[Union[str, int]]:
        """The list of all successfull status code."""
        return [code for response in self.responses for code in response.status_codes if code != "default"]
