# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from .import_serializer import FileImportSerializer, TypingSection
from ..models import FileImport, ImportType, CodeModel, TokenCredentialSchema, ParameterList


def config_imports(code_model, global_parameters: ParameterList, async_mode: bool) -> FileImport:
    file_import = FileImport()
    file_import.add_from_import("azure.core.configuration", "Configuration", ImportType.AZURECORE)
    file_import.add_from_import("azure.core.pipeline", "policies", ImportType.AZURECORE)
    file_import.add_from_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
    if code_model.options["package_version"]:
        file_import.add_from_import(".._version" if async_mode else "._version", "VERSION", ImportType.LOCAL)
    for gp in global_parameters:
        file_import.merge(gp.imports())
    if code_model.options["azure_arm"]:
        async_policy = "ARMHttpLoggingPolicy, AsyncARMChallengeAuthenticationPolicy"
        policy = "ARMHttpLoggingPolicy, ARMChallengeAuthenticationPolicy"
        file_import.add_from_import("azure.mgmt.core.policies", async_policy if async_mode else policy,
                                    ImportType.AZURECORE)
    return file_import


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
            gp for gp in self.code_model.global_parameters.parameters if isinstance(gp.schema, TokenCredentialSchema)
        ][0]
        credential_param.schema = TokenCredentialSchema(async_mode=self.async_mode)

    def serialize_service_client_file(self) -> str:
        def _service_client_imports() -> FileImport:
            file_import = self.code_model.service_client.imports(self.code_model, self.async_mode)
            for gp in self.code_model.global_parameters:
                file_import.merge(gp.imports())
            return file_import

        template = self.env.get_template("service_client.py.jinja2")

        if (
            self.code_model.options['credential'] and
            self.code_model.options['credential_default_policy_type'] == "ARMChallengeAuthenticationPolicy"
        ):
            self._correct_credential_parameter()

        return template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(
                _service_client_imports(),
                is_python_3_file=self.async_mode
            ),
        )

    def serialize_config_file(self) -> str:

        package_name = self.code_model.options['package_name']
        if package_name and package_name.startswith("azure-"):
            package_name = package_name[len("azure-"):]
        sdk_moniker = package_name if package_name else self.code_model.class_name.lower()

        if (
            self.code_model.options['credential'] and
            self.code_model.options['credential_default_policy_type'] == "ARMChallengeAuthenticationPolicy"
        ):
            self._correct_credential_parameter()

        template = self.env.get_template("config.py.jinja2")
        return template.render(
            code_model=self.code_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(
                config_imports(
                    self.code_model, self.code_model.global_parameters, self.async_mode
                ), is_python_3_file=self.async_mode
            ),
            sdk_moniker=sdk_moniker
        )

    def serialize_version_file(self) -> str:
        template = self.env.get_template("version.py.jinja2")
        return template.render(code_model=self.code_model)

    def serialize_setup_file(self) -> str:
        template = self.env.get_template("setup.py.jinja2")
        return template.render(code_model=self.code_model)
