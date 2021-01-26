# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .imports import FileImport, ImportType, TypingSection


class Client:
    """A service client.
    """

    @staticmethod
    def pipeline_class(code_model, async_mode: bool) -> str:
        if code_model.options["azure_arm"]:
            if async_mode:
                return "AsyncARMPipelineClient"
            return "ARMPipelineClient"
        if async_mode:
            return "AsyncPipelineClient"
        return "PipelineClient"

    @staticmethod
    def imports(code_model, async_mode: bool) -> FileImport:
        file_import = FileImport()

        file_import.add_from_import("msrest", "Serializer", ImportType.AZURECORE)
        file_import.add_from_import("msrest", "Deserializer", ImportType.AZURECORE)
        file_import.add_from_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
        file_import.add_from_import(
            "azure.core.pipeline", "PipelineResponse", ImportType.AZURECORE, TypingSection.CONDITIONAL
        )
        file_import.add_from_import(
            "azure.core.pipeline.transport", "HttpRequest", ImportType.AZURECORE, TypingSection.CONDITIONAL
        )
        file_import.add_from_import("._configuration", f"{code_model.class_name}Configuration", ImportType.LOCAL)
        for operation_group in code_model.operation_groups:
            file_import.add_from_import(".operations", f"{ operation_group.class_name }", ImportType.LOCAL)

        if code_model.sorted_schemas:
            path_to_models = ".." if async_mode else "."
            file_import.add_from_import(path_to_models, "models", ImportType.LOCAL)

        any_optional_gp = any(not gp.required for gp in code_model.global_parameters)

        if any_optional_gp or code_model.base_url:
            file_import.add_from_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)

        if code_model.options["azure_arm"]:
            file_import.add_from_import(
                "azure.mgmt.core", Client.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_from_import(
                "azure.core", Client.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )

        if not code_model.sorted_schemas:
            # in this case, we have client_models = {} in the service client, which needs a type annotation
            # this import will always be commented, so will always add it to the typing section
            file_import.add_from_import("typing", "Dict", ImportType.STDLIB, TypingSection.TYPING)

        return file_import
