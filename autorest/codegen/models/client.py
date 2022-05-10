# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Optional, TYPE_CHECKING
from .parameter_list import GlobalParameterList
from .imports import FileImport, ImportType, TypingSection, MsrestImportType

if TYPE_CHECKING:
    from .code_model import CodeModel


class Client:
    """A service client."""

    def __init__(self, code_model: "CodeModel", parameters: GlobalParameterList):
        self.code_model = code_model
        self.parameters = parameters
        self.parameterized_host_template: Optional[str] = None
        self._config_parameters = parameters

    @property
    def has_parameterized_host(self) -> bool:
        return bool(self.parameterized_host_template)

    def pipeline_class(self, async_mode: bool) -> str:
        if self.code_model.options["azure_arm"]:
            if async_mode:
                return "AsyncARMPipelineClient"
            return "ARMPipelineClient"
        if async_mode:
            return "AsyncPipelineClient"
        return "PipelineClient"

    def _imports_shared(self, async_mode: bool) -> FileImport:
        file_import = FileImport()

        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )

        any_optional_gp = any(not gp.required for gp in self.parameters)

        legacy = not any(
            g
            for g in ["low_level_client", "version_tolerant"]
            if g in self.code_model.options
        )
        if any_optional_gp or (
            legacy and self.code_model.service_client.parameters.host
        ):
            file_import.add_submodule_import(
                "typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL
            )

        file_import.add_msrest_import(
            self.code_model,
            ".." if async_mode else ".",
            MsrestImportType.SerializerDeserializer,
            TypingSection.REGULAR,
        )

        if self.code_model.options["azure_arm"]:
            file_import.add_submodule_import(
                "azure.mgmt.core", self.pipeline_class(async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_submodule_import(
                "azure.core", self.pipeline_class(async_mode), ImportType.AZURECORE
            )

        for gp in self.code_model.global_parameters:
            file_import.merge(gp.imports())
        file_import.add_submodule_import(
            "._configuration",
            f"{self.code_model.class_name}Configuration",
            ImportType.LOCAL,
        )

        return file_import

    def imports(self, async_mode: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)
        if async_mode:
            file_import.add_submodule_import("typing", "Awaitable", ImportType.STDLIB)
            file_import.add_submodule_import(
                "azure.core.rest",
                "AsyncHttpResponse",
                ImportType.AZURECORE,
                TypingSection.CONDITIONAL,
            )
        else:
            file_import.add_submodule_import(
                "azure.core.rest",
                "HttpResponse",
                ImportType.AZURECORE,
                TypingSection.CONDITIONAL,
            )
        file_import.add_submodule_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
            TypingSection.CONDITIONAL,
        )
        for og in self.code_model.operation_groups:
            file_import.add_submodule_import(
                f".{self.code_model.operations_folder_name}",
                og.class_name,
                ImportType.LOCAL,
            )

        if self.code_model.sorted_schemas:
            path_to_models = ".." if async_mode else "."
            file_import.add_submodule_import(path_to_models, "models", ImportType.LOCAL)
        else:
            # in this case, we have client_models = {} in the service client, which needs a type annotation
            # this import will always be commented, so will always add it to the typing section
            file_import.add_submodule_import(
                "typing", "Dict", ImportType.STDLIB, TypingSection.TYPING
            )
        file_import.add_submodule_import("copy", "deepcopy", ImportType.STDLIB)
        return file_import

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)
        try:
            mixin_operation = next(
                og
                for og in self.code_model.operation_groups
                if og.is_empty_operation_group
            )
            file_import.add_submodule_import(
                "._operations_mixin", mixin_operation.class_name, ImportType.LOCAL
            )
        except StopIteration:
            pass
        return file_import

    def send_request_signature(self, is_python3_file: bool) -> List[str]:
        request_signature = [
            "request: HttpRequest,"
            if is_python3_file
            else "request,  # type: HttpRequest"
        ]
        return request_signature + self.parameters.method_signature_kwargs(
            is_python3_file
        )

    @property
    def filename(self) -> str:
        if not self.code_model.is_legacy:
            return "_client"
        return f"_{self.code_model.module_name}"
