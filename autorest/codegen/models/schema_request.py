# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, List, Any, Optional

from .base_model import BaseModel
from .parameter import Parameter, get_parameter
from .parameter_list import ParameterList

class SchemaRequest(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        parameters: ParameterList,
    ) -> None:
        super().__init__(yaml_data)
        self.content_types: List[str] = []
        self.parameters = parameters

    @property
    def is_stream_request(self) -> bool:
        """Is the request expected to be streamable, like a download."""
        if self.yaml_data['protocol']['http'].get('knownMediaType'):
            return self.yaml_data['protocol']['http']['knownMediaType'] == 'binary' # FIXME: this might be an m4 issue
        return self.yaml_data["protocol"]["http"].get("binary", False)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], *, code_model) -> "SchemaRequest":
        parameter_creator = get_parameter(code_model).from_yaml
        parameters: Optional[List[Parameter]] = [
            parameter_creator(yaml, code_model=code_model)
            for yaml in yaml_data.get("parameters", [])
        ]

        return cls(
            yaml_data=yaml_data,
            parameters=ParameterList(code_model, parameters)
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.content_types}>"
