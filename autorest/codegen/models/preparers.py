# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List
from .base_model import BaseModel
from .request import Request
from .imports import FileImport

class Preparers(BaseModel):
    """Everything that goes into the preparers
    """
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        requests: List[Request]
    ):
        super(Preparers, self). __init__(yaml_data=yaml_data)
        self.requests = requests

    def imports(self) -> FileImport:
        file_import = FileImport()
        for request in self.requests:
            file_import.merge(request.imports())
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], *, code_model) -> "Preparers":
        requests = [
            Request.from_yaml(operation_yaml, code_model=code_model)
            for og_group in yaml_data["operationGroups"]
            for operation_yaml in og_group["operations"]
        ]

        return cls(
            yaml_data=yaml_data,
            requests=requests
        )
