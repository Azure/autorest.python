# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment

from .import_serializer import FileImportSerializer
from ..models import CodeModel


class ProtocolSerializer:
    def __init__(
        self, code_model: CodeModel, env: Environment
    ) -> None:
        self.code_model = code_model
        self.env = env

    def serialize_preparers(self, is_python_3_file: bool) -> str:

        template = self.env.get_template("preparers.py.jinja2")

        return template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(
                self.code_model.protocol.imports(),
                is_python_3_file=is_python_3_file
            ),
            is_python_3_file=is_python_3_file,
        )

    def serialize_init(self) -> str:
        template = self.env.get_template("protocol_init.py.jinja2")
        return template.render(code_model=self.code_model)
