# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .imports import FileImport, ImportType


class Client:
    """A service client.
    """

    def pipeline_class(self, code_model, async_mode):
        if code_model.options["azure_arm"]:
            if async_mode:
                return "AsyncARMPipelineClient"
            else:
                return "ARMPipelineClient"
        else:
            if async_mode:
                return "AsyncPipelineClient"
            else:
                return "PipelineClient"

    def imports(self, code_model, async_mode):
        file_import = FileImport()

        file_import.add_from_import(
            "msrest", "Serializer", ImportType.AZURECORE
        )
        file_import.add_from_import(
            "msrest", "Deserializer", ImportType.AZURECORE
        )

        if code_model.options["azure_arm"]:
            file_import.add_from_import(
                "azure.mgmt.core", self.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_from_import(
                "azure.core", self.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )
        return file_import
