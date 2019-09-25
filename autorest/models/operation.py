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
from typing import Dict, Any

from .imports import FileImport, ImportType

class Operation:
    """Represent an operation.
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str
    ) -> None:
        self.yaml_data = yaml_data
        self.name = name
        self.description = description


    def imports(self):
        file_import = FileImport()

        # Exceptions
        file_import.add_from_import("azure.core.exceptions", "map_error", ImportType.AZURECORE)
        if True: # Replace with "this operation has default exception"
            file_import.add_from_import("azure.core.exceptions", "HttpResponseError", ImportType.AZURECORE)

        # Tracings
        if True: # Replace with "--tracing was passed to autorest"
            file_import.add_from_import("azure.core.tracing.decorator", "distributed_trace", ImportType.AZURECORE)

        # Deprecation
        if True: # Replace with "the YAML contains deprecated:true"
            file_import.add_import("warnings", ImportType.STDLIB)

        # Models
        if True: # Replace by "this operation has a return type or a body parameter"
            file_import.add_from_import("..", "models", ImportType.LOCAL)

        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "Operation":
        return cls(
            yaml_data=yaml_data,
            name=yaml_data['language']['default']['name'],
            description=yaml_data['language']['default']['description'],
        )
