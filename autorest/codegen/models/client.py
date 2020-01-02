# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .imports import FileImport, ImportType


class Client:
    """A service client.
    """

    @staticmethod
    def pipeline_class(code_model, async_mode):
        if code_model.options["azure_arm"]:
            if async_mode:
                return "AsyncARMPipelineClient"
            return "ARMPipelineClient"
        if async_mode:
            return "AsyncPipelineClient"
        return "PipelineClient"

    @staticmethod
    def imports(code_model, async_mode):
        file_import = FileImport()

        file_import.add_from_import(
            "msrest", "Serializer", ImportType.AZURECORE
        )
        file_import.add_from_import(
            "msrest", "Deserializer", ImportType.AZURECORE
        )

        if code_model.options["azure_arm"]:
            file_import.add_from_import(
                "azure.mgmt.core", Client.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_from_import(
                "azure.core", Client.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )
        return file_import
