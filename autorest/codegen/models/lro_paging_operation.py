# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Set, Optional
from .lro_operation import LROOperation
from .paging_operation import PagingOperation
from .imports import FileImport, ImportType
from .schema_request import SchemaRequest
from .parameter import Parameter
from .schema_response import SchemaResponse

def _get_paging_method_import(async_mode):
    file_import = FileImport()
    paging_file = "async_paging" if async_mode else "paging"
    async_prefix = "Async" if async_mode else ""
    file_import.add_from_import(
        f"azure.core.{paging_file}_method", f"{async_prefix}PagingMethodWithInitialResponse", ImportType.AZURECORE
    )
    return file_import

class LROPagingOperation(PagingOperation, LROOperation):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        url: str,
        method: str,
        multipart: bool,
        api_versions: Set[str],
        requests: List[SchemaRequest],
        summary: Optional[str] = None,
        parameters: Optional[List[Parameter]] = None,
        multiple_media_type_parameters: Optional[List[Parameter]] = None,
        responses: Optional[List[SchemaResponse]] = None,
        exceptions: Optional[List[SchemaResponse]] = None,
        want_description_docstring: bool = True,
        want_tracing: bool = True
    ) -> None:
        super(LROPagingOperation, self).__init__(
            yaml_data,
            name,
            description,
            url,
            method,
            multipart,
            api_versions,
            requests,
            summary,
            parameters,
            multiple_media_type_parameters,
            responses,
            exceptions,
            want_description_docstring,
            want_tracing,
            override_success_response_to_200=True
        )
        self.coroutine_when_async = True

    def imports(self, code_model, async_mode: bool) -> FileImport:
        lro_imports = LROOperation.imports(self, code_model, async_mode)
        paging_imports = PagingOperation.imports(self, code_model, async_mode)

        file_import = lro_imports
        file_import.merge(paging_imports)
        return file_import
