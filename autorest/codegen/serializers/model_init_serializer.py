# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from ..models import CodeModel

class ModelInitSerializer:
    def __init__(self, code_model: CodeModel, env: Environment):
        self.code_model = code_model
        self.env = env
        self._model_init_file: str = ""

    def serialize(self) -> None:
        schemas = sorted(self.code_model.sorted_schemas, key=lambda x: x.name)
        enums = [e.enum_type for e in self.code_model.enums.values()] if self.code_model.enums else None

        if enums:
            enums.sort()

        template = self.env.get_template("model_init.py.jinja2")
        self._model_init_file = template.render(
            code_model=self.code_model,
            schemas=schemas,
            enums=enums
        )

    @property
    def model_init_file(self) -> str:
        return self._model_init_file
