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
import logging
from typing import Dict, List, Any, Optional

from .operation import Operation
from .parameter import Parameter
from .schema_response import SchemaResponse
from .imports import ImportType

_LOGGER = logging.getLogger(__name__)


class PagingOperation(Operation):

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        url: str,
        method: str,
        parameters: List[Parameter] = None,
        responses: List[SchemaResponse] = None,
        exceptions: List[SchemaResponse] = None,
        media_types: List[str] = None,
    ) -> None:
        super(PagingOperation, self).__init__(
            yaml_data,
            name,
            description,
            url,
            method,
            parameters,
            responses,
            exceptions,
            media_types
        )
        self._item_name = yaml_data['extensions']['x-ms-pageable'].get("itemName")
        self._next_link_name = yaml_data['extensions']['x-ms-pageable'].get("nextLinkName")
        self.operation_name = yaml_data['extensions']['x-ms-pageable'].get("operationName")

    def _find_python_name(self, rest_api_name, log_name):
        response = self.responses[0]
        for prop in response.schema.properties:
            if prop.original_swagger_name == rest_api_name:
                return prop.name
        raise ValueError(f"Was unable to find {log_name}:{rest_api_name} in model {response.schema.name}")

    @property
    def item_name(self):
        return self._find_python_name(self._item_name, "itemName")

    @property
    def next_link_name(self):
        return self._find_python_name(self._next_link_name, "nextLinkName")

    def imports(self, code_model, async_mode):
        file_import = super(PagingOperation, self).imports(code_model, async_mode)

        if async_mode:
            file_import.add_from_import(
                "azure.core.async_paging", "AsyncItemPaged", ImportType.AZURECORE
            )
            file_import.add_from_import(
                "azure.core.async_paging", "AsyncList", ImportType.AZURECORE
            )
        else:
            file_import.add_from_import(
                "azure.core.paging", "ItemPaged", ImportType.AZURECORE
            )
        return file_import
