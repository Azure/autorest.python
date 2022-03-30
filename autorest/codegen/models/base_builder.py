# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, Union
from enum import Enum
from .base_model import BaseModel
from .schema_response import SchemaResponse
from .schema_request import SchemaRequest
from .parameter import Parameter, ParameterLocation
from .object_schema import ObjectSchema
from .utils import JSON_REGEXP

_M4_HEADER_PARAMETERS = ["content_type", "accept"]


class BodyKwargNames(str, Enum):
    JSON = "json"
    CONTENT = "content"
    FILES = "files"
    DATA = "data"

def _get_chosen_parameter(overloaded_parameters: List[Parameter]) -> Parameter:
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
        return overloaded_parameters[0]

def _unify_overloaded_parameters(overloaded_parameters: List[Parameter]) -> Parameter:
    """Unify the overloaded parameters into one parameter for the main method

    When parameters are overloaded, we need to create one unified
    parameter on the actual function.
    """
    type_annot = ", ".join([
        param.schema.type_annotation(is_operation_file=True)
        for param in overloaded_parameters
    ])
    docstring_type = " or ".join([
        param.schema.docstring_type for param in overloaded_parameters
    ])
    chosen_parameter = _get_chosen_parameter(overloaded_parameters)

    chosen_parameter.set_type_annotation(f"Union[{type_annot}]")
    chosen_parameter.docstring_type = docstring_type
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
            parameters.append(_unify_overloaded_parameters(overloaded_parameters))

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
    def body_kwarg_name_to_content_types(self) -> Dict[BodyKwargNames, List[str]]:
        # Group the different content types into content type groups based off of request kwarg name
        retval: Dict[BodyKwargNames, List[str]] = {}
        for content_type in self.content_type_to_schema_request.keys():
            if "multipart" in content_type:
                retval.setdefault(BodyKwargNames.FILES, []).append(content_type)
            elif "application/x-www-form-urlencoded" == content_type:
                retval.setdefault(BodyKwargNames.DATA, []).append(content_type)
            elif JSON_REGEXP.match(content_type):
                retval.setdefault(BodyKwargNames.JSON, []).append(content_type)
            else:
                retval.setdefault(BodyKwargNames.CONTENT, []).append(content_type)
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
