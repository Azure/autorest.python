# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from .import_serializer import FileImportSerializer
from ..models import FileImport, ImportType, CodeModel


class GeneralSerializer:
    def __init__(self, code_model: CodeModel, env: Environment, async_mode: bool) -> None:
        self.code_model = code_model
        self.env = env
        self.async_mode = async_mode

    def serialize_pkgutil_init_file(self) -> str:
        template = self.env.get_template("pkgutil_init.py.jinja2")
        return template.render()

    def serialize_init_file(self) -> str:
        template = self.env.get_template("init.py.jinja2")
        return template.render(code_model=self.code_model, async_mode=self.async_mode,)

    def serialize_service_client_file(self) -> str:
        template = self.env.get_template("service_client.py.jinja2")
        return template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(self.code_model.service_client.imports(self.code_model, self.async_mode)),
        )

    def serialize_config_file(self) -> str:
        def _config_imports(async_mode: bool) -> FileImport:
            file_import = FileImport()
            file_import.add_from_import("azure.core.configuration", "Configuration", ImportType.AZURECORE)
            file_import.add_from_import("azure.core.pipeline", "policies", ImportType.AZURECORE)
            file_import.add_from_import("typing", "Any", ImportType.STDLIB)
            if self.code_model.options["package_version"]:
                file_import.add_from_import(".._version" if async_mode else "._version", "VERSION", ImportType.LOCAL)
            if any(not gp.required for gp in self.code_model.global_parameters):
                file_import.add_from_import("typing", "Optional", ImportType.STDLIB)
            # if self.code_model.options['credential']:
            #     file_import.add_from_import("azure.core.credentials", "TokenCredential", ImportType.AZURECORE)
            return file_import

        template = self.env.get_template("config.py.jinja2")
        return template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(_config_imports(self.async_mode)),
        )

    def serialize_version_file(self) -> str:
        template = self.env.get_template("version.py.jinja2")
        return template.render(code_model=self.code_model)

    def serialize_setup_file(self) -> str:
        template = self.env.get_template("setup.py.jinja2")
        return template.render(code_model=self.code_model)
