# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, TYPE_CHECKING
from .base_model import BaseModel
from .request_builder import RequestBuilder
from .imports import FileImport

if TYPE_CHECKING:
    from .code_model import CodeModel

class Rest(BaseModel):
    """Everything that goes into the request_builders
    """
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        request_builders: List[RequestBuilder]
    ):
        super(). __init__(yaml_data=yaml_data, code_model=code_model)
        self.request_builders = request_builders

    def imports(self, builder_group_name: str) -> FileImport:
        file_import = FileImport()
        for request_builder in self.request_builders:
            if request_builder.builder_group_name == builder_group_name:
                file_import.merge(request_builder.imports())
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Rest":
        request_builders = []
        if yaml_data.get("operationGroups"):
            request_builders = [
                RequestBuilder.from_yaml(operation_yaml, code_model=code_model)
                for og_group in yaml_data["operationGroups"]
                for operation_yaml in og_group["operations"]
            ]

        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            request_builders=request_builders
        )
