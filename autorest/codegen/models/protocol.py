# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List
from .base_model import BaseModel
from .preparer import Preparer
from .imports import FileImport

class Protocol(BaseModel):
    """Everything that goes into the preparers
    """
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        preparers: List[Preparer]
    ):
        super(Protocol, self). __init__(yaml_data=yaml_data)
        self.preparers = preparers

    def imports(self) -> FileImport:
        file_import = FileImport()
        for preparer in self.preparers:
            file_import.merge(preparer.imports())
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], *, code_model) -> "Protocol":
        preparers = [
            Preparer.from_yaml(operation_yaml, code_model=code_model)
            for og_group in yaml_data["operationGroups"]
            for operation_yaml in og_group["operations"]
        ]

        return cls(
            yaml_data=yaml_data,
            preparers=preparers
        )
