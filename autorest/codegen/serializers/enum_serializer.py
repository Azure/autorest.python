# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from jinja2 import Environment
from ..models import CodeModel

class EnumSerializer:
    def __init__(self, code_model: CodeModel, env: Environment):
        self.code_model = code_model
        self.env = env
        self._enum_file: str = ""

    def serialize(self) -> None:
        # Generate the enum file
        template = self.env.get_template("enum_container.py.jinja2")
        self._enum_file = template.render(code_model=self.code_model)

    @property
    def enum_file(self) -> str:
        return self._enum_file
