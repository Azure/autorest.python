# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from .import_serializer import FileImportSerializer
from ..models import CodeModel


class GeneralSerializer:
    def __init__(self, code_model: CodeModel, env: Environment, async_mode: bool):
        self.code_model = code_model
        self.env = env
        self.async_mode = async_mode
        self._pkgutil_init_file: str = ""
        self._init_file: str = ""
        self._service_client_file: str = ""
        self._config_file: str = ""
        self._version_file: str = ""
        self._setup_file: str = ""

    def serialize(self) -> None:
        template = self.env.get_template("pkgutil_init.py.jinja2")
        self._pkgutil_init_file = template.render()

        template = self.env.get_template("init.py.jinja2")
        self._init_file = template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
        )

        template = self.env.get_template("service_client.py.jinja2")
        self._service_client_file = template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(
                self.code_model.service_client.imports(self.code_model, self.async_mode)
            ),
        )

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

    @property
    def pkgutil_init_file(self) -> str:
        return self._pkgutil_init_file

    @property
    def init_file(self) -> str:
        return self._init_file

    @property
    def service_client_file(self) -> str:
        return self._service_client_file

    @property
    def config_file(self) -> str:
        return self._config_file

    @property
    def version_file(self) -> str:
        return self._version_file

    @property
    def setup_file(self) -> str:
        return self._setup_file
