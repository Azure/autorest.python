# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from .import_serializer import FileImportSerializer
from ..models import FileImport, ImportType, CodeModel, CredentialSchema


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
        return template.render(code_model=self.code_model, async_mode=self.async_mode)

    def _correct_credential_parameter(self):
        credential_param = [
            gp for gp in self.code_model.global_parameters.parameters if isinstance(gp.schema, CredentialSchema)
        ][0]
        credential_param.schema = CredentialSchema(async_mode=self.async_mode)
        # we know that if there's a credential global param, it's always the first because
        # we insert it there
        self.code_model.global_parameters[0] = credential_param

    def serialize_service_client_file(self) -> str:
        template = self.env.get_template("service_client.py.jinja2")

        global_parameters = self.code_model.global_parameters
        if self.code_model.options['credential']:
            self._correct_credential_parameter()

        return template.render(
            code_model=self.code_model,
            global_parameters=global_parameters,
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
            for gp in self.code_model.global_parameters:
                file_import.merge(gp.imports())
            return file_import

        package_name = self.code_model.options['package_name']
        if package_name and package_name.startswith("azure-"):
            package_name = package_name[len("azure-"):]
        sdk_moniker = package_name if package_name else self.code_model.class_name.lower()

        if self.code_model.options['credential']:
            self._correct_credential_parameter()

        template = self.env.get_template("config.py.jinja2")
        return template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(_config_imports(self.async_mode)),
            sdk_moniker=sdk_moniker
        )

    def serialize_version_file(self) -> str:
        template = self.env.get_template("version.py.jinja2")
        return template.render(code_model=self.code_model)

    def serialize_setup_file(self) -> str:
        template = self.env.get_template("setup.py.jinja2")
        return template.render(code_model=self.code_model)
