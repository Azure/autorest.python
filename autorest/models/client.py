# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
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
