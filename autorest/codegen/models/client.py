# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .imports import FileImport, ImportType, IsTypingImport


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
        file_import.add_from_import("typing", "Any", ImportType.STDLIB, IsTypingImport.PYTHON2)

        # if code_model.options["credential"]:
        #     file_import.add_from_import("azure.core.credentials", "TokenCredential", ImportType.AZURECORE)
        any_optional_gp = any(not gp.required for gp in code_model.global_parameters)

        if any_optional_gp or code_model.base_url:
            file_import.add_from_import("typing", "Optional", ImportType.STDLIB, IsTypingImport.PYTHON2)

        if code_model.options["azure_arm"]:
            file_import.add_from_import(
                "azure.mgmt.core", Client.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_from_import(
                "azure.core", Client.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )
        return file_import
