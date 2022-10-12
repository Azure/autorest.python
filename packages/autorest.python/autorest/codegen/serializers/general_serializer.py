# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from .import_serializer import FileImportSerializer, TypingSection
from ..models.imports import MsrestImportType
from ..models import (
    FileImport,
    ImportType,
    NamespaceModel,
    CodeModel
)
from .client_serializer import ClientSerializer, ConfigSerializer


class GeneralSerializer:
    def __init__(
        self, code_model: CodeModel, namespace_model: NamespaceModel, env: Environment, async_mode: bool
    ) -> None:
        self.code_model = code_model
        self.namespace_model = namespace_model
        self.env = env
        self.async_mode = async_mode

    def serialize_pkgutil_init_file(self) -> str:
        template = self.env.get_template("pkgutil_init.py.jinja2")
        return template.render()

    def serialize_init_file(self) -> str:
        template = self.env.get_template("init.py.jinja2")
        clients = [c for c in self.namespace_model.clients if c.request_builders]
        return template.render(namespace_model=self.namespace_model, clients=clients, async_mode=self.async_mode)

    def serialize_service_client_file(self) -> str:

        template = self.env.get_template("client.py.jinja2")

        return template.render(
            namespace_model=self.namespace_model,
            async_mode=self.async_mode,
            serializer=ClientSerializer(self.namespace_model),
            imports=FileImportSerializer(
                self.namespace_model.client.imports(self.async_mode),
            ),
        )

    def serialize_vendor_file(self) -> str:
        template = self.env.get_template("vendor.py.jinja2")

        # configure imports
        file_import = FileImport()
        if self.namespace_model.need_request_converter:
            file_import.add_submodule_import(
                "azure.core.pipeline.transport",
                "HttpRequest",
                ImportType.AZURECORE,
            )

        if self.namespace_model.need_mixin_abc:
            file_import.add_submodule_import(
                "abc",
                "ABC",
                ImportType.STDLIB,
            )
            file_import.add_submodule_import(
                "azure.core",
                f"{'Async' if self.async_mode else ''}PipelineClient",
                ImportType.AZURECORE,
                TypingSection.TYPING,
            )
            file_import.add_submodule_import(
                "._configuration",
                f"{self.namespace_model.client.name}Configuration",
                ImportType.LOCAL,
            )
            file_import.add_msrest_import(
                self.namespace_model,
                ".." if self.async_mode else ".",
                MsrestImportType.SerializerDeserializer,
                TypingSection.TYPING,
            )

        return template.render(
            namespace_model=self.namespace_model,
            imports=FileImportSerializer(
                file_import,
            ),
            async_mode=self.async_mode,
        )

    def serialize_config_file(self) -> str:

        package_name = self.namespace_model.options["package_name"]
        if package_name and package_name.startswith("azure-"):
            package_name = package_name[len("azure-") :]
        sdk_moniker = (
            package_name if package_name else self.namespace_model.client.name.lower()
        )
        template = self.env.get_template("config.py.jinja2")
        return template.render(
            namespace_model=self.namespace_model,
            async_mode=self.async_mode,
            imports=FileImportSerializer(
                self.namespace_model.config.imports(self.async_mode),
            ),
            serializer=ConfigSerializer(self.namespace_model),
            sdk_moniker=sdk_moniker,
        )

    def serialize_version_file(self) -> str:
        template = self.env.get_template("version.py.jinja2")
        return template.render(namespace_model=self.namespace_model)

    def serialize_setup_file(self) -> str:
        template = self.env.get_template("setup.py.jinja2")
        params = {}
        params.update(self.namespace_model.options)
        params.update(self.namespace_model.package_dependency)
        return template.render(namespace_model=self.namespace_model, **params)

    def serialize_serialization_file(self) -> str:
        template = self.env.get_template("serialization.py.jinja2")
        return template.render(namespace_model=self.namespace_model)

    def serialize_model_base_file(self) -> str:
        template = self.env.get_template("model_base.py.jinja2")
        return template.render(namespace_model=self.namespace_model)

    def serialize_validation_file(self) -> str:
        template = self.env.get_template("validation.py.jinja2")
        return template.render(namespace_model=self.namespace_model)
