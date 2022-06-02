# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Optional, Dict, Any
from jinja2 import Environment
from autorest.codegen.serializers.import_serializer import FileImportSerializer
from ..models import CodeModel


class SampleSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        operation_group_name: str,
        operation_name: str,
        operation_params: Dict[Any, Any],
        sample_params: Dict[Any, Any],
        operation_result: str,
        origin_file: Optional[str],
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.operation_group_name = operation_group_name
        self.operation_name = operation_name
        self.operation_params = operation_params
        self.sample_params = sample_params
        self.operation_result = operation_result
        self.origin_file = origin_file

    def serialize(self) -> str:
        template = self.env.get_template("sample.py.jinja2")
        return template.render(
            code_model=self.code_model,
            operation_group_name=self.operation_group_name,
            operation_name=self.operation_name,
            client_params=self.sample_params["client_params"],
            operation_params=self.operation_params,
            origin_file=self.origin_file,
            imports=FileImportSerializer(self.sample_params["imports"], True),
            annotation=self.sample_params["annotation"],
            operation_result=self.operation_result,
            file_name=self.sample_params["file_name"],
        )
