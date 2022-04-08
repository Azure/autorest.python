# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, Union, TYPE_CHECKING
from .base_model import BaseModel
from .schema_response import SchemaResponse
from .schema_request import SchemaRequest

if TYPE_CHECKING:
    from .code_model import CodeModel


_M4_HEADER_PARAMETERS = ["content_type", "accept"]

def create_parameters(
    yaml_data: Dict[str, Any], code_model, parameter_creator: Callable
):
    multiple_requests = len(yaml_data["requests"]) > 1

    multiple_content_type_parameters = []
    parameters = [
        parameter_creator(yaml, code_model=code_model)
        for yaml in yaml_data.get("parameters", [])
    ]

    for request in yaml_data["requests"]:
        for yaml in request.get("parameters", []):
            parameter = parameter_creator(yaml, code_model=code_model)
            name = yaml["language"]["python"]["name"]
            if name in _M4_HEADER_PARAMETERS:
                parameters.append(parameter)
            elif multiple_requests:
                parameter.has_multiple_content_types = True
                multiple_content_type_parameters.append(parameter)
            else:
                parameters.append(parameter)

    if multiple_content_type_parameters:
        body_parameters_name_set = set(
            p.serialized_name for p in multiple_content_type_parameters
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

    return parameters, multiple_content_type_parameters

class BaseBuilder(BaseModel):
    """Base class for Operations and Request Builders"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        description: str,
        parameters,
        schema_requests: List[SchemaRequest],
        responses: Optional[List[SchemaResponse]] = None,
        summary: Optional[str] = None,
        *,
        abstract: bool = False,
        want_tracing: bool = True,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name = name
        self._description = description
        self.parameters = parameters
        self.responses = responses or []
        self._summary = summary
        self.schema_requests = schema_requests
        # for operations where we don't know what to do, we mark them as abstract so users implement
        # in patch.py
        self.abstract = abstract
        self.want_tracing = want_tracing

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
        return self._description

    @property
    def default_content_type_declaration(self) -> str:
        return f'"{self.parameters.default_content_type}"'

    def get_response_from_status(self, status_code: Optional[Union[str, int]]) -> SchemaResponse:
        for response in self.responses:
            if status_code in response.status_codes:
                return response
        raise ValueError(f"Incorrect status code {status_code}, operation {self.name}")

    @property
    def success_status_code(self) -> List[Union[str, int]]:
        """The list of all successfull status code."""
        return [code for response in self.responses for code in response.status_codes if code != "default"]

    def method_signature(self, is_python3_file: bool) -> List[str]:
        if self.abstract:
            return ["*args,", "**kwargs"]
        return self.parameters.method_signature(is_python3_file)
