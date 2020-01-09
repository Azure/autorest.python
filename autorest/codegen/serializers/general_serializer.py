# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Optional
from .import_serializer import FileImportSerializer
from ..models import Parameter


class GeneralSerializer:
    def __init__(self, code_model, env, async_mode):
        self.code_model = code_model
        self.env = env
        self.async_mode = async_mode
        self._init_file = None
        self._service_client_file = None
        self._config_file = None
        self._version_file = None
        self._setup_file = None
        self._pkgutil_init_file = None

    def serialize(self):
        template = self.env.get_template("pkgutil_init.py.jinja2")
        self._pkgutil_init_file = template.render()

        template = self.env.get_template("init.py.jinja2")
        self._init_file = template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
        )

        self.env.globals.update(service_client_init_typing_comment=GeneralSerializer.service_client_init_typing_comment)
        template = self.env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(
                self.code_model.service_client.imports(self.code_model, self.async_mode)
            ),
        )

        self.env.globals.update(config_init_typing_comment=GeneralSerializer.config_init_typing_comment)
        template = self.env.get_template("config.py.jinja2")
        self._config_file = template.render(
            code_model=self.code_model,
            async_mode=self.async_mode
        )

        if not self.async_mode:
            template = self.env.get_template("version.py.jinja2")
            self._version_file = template.render(code_model=self.code_model)

            template = self.env.get_template("setup.py.jinja2")
            self._setup_file = template.render(code_model=self.code_model)

    @staticmethod
    def config_init_typing_comment(global_parameters: List[Parameter]) -> str:
        if not global_parameters:
            return "# type: (**Any) -> None"
        global_parameters_typing = [p.schema.get_python_type_annotation() for p in global_parameters]
        return f"# type: ({', '.join(global_parameters_typing)}, **Any) -> None"

    @staticmethod
    def service_client_init_typing_comment(global_parameters: List[Parameter], base_url: Optional[str]) -> str:
        if not global_parameters:
            return "# type: (**Any) -> None"
        global_parameters_typing = [p.schema.get_python_type_annotation() for p in global_parameters]
        if base_url:
            return f"# type: ({', '.join(global_parameters_typing)}, Optional[str], **Any) -> None"
        return f"# type: ({', '.join(global_parameters_typing)}, **Any) -> None"

    @property
    def pkgutil_init_file(self):
        return self._pkgutil_init_file

    @property
    def init_file(self):
        return self._init_file

    @property
    def service_client_file(self):
        return self._service_client_file

    @property
    def config_file(self):
        return self._config_file

    @property
    def version_file(self):
        return self._version_file

    @property
    def setup_file(self):
        return self._setup_file
