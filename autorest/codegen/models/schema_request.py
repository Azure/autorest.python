# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, List, Any, Optional, TYPE_CHECKING

from .base_model import BaseModel
from .parameter import Parameter
from .parameter_list import ParameterList

if TYPE_CHECKING:
    from .code_model import CodeModel


class SchemaRequest(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        content_types: List[str],
        parameters: ParameterList,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.content_types = content_types
        self.parameters = parameters

    @property
    def is_stream_request(self) -> bool:
        """Is the request expected to be streamable, like a download."""
        if self.yaml_data["protocol"]["http"].get("knownMediaType"):
            return (
                self.yaml_data["protocol"]["http"]["knownMediaType"] == "binary"
            )  # FIXME: this might be an m4 issue
        return self.yaml_data["protocol"]["http"].get("binary", False)

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "SchemaRequest":

        parameters: Optional[List[Parameter]] = [
            Parameter.from_yaml(yaml, code_model=code_model)
            for yaml in yaml_data.get("parameters", [])
        ]

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            content_types=yaml_data["protocol"]["http"].get("mediaTypes", []),
            parameters=ParameterList(code_model, parameters),
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.content_types}>"
