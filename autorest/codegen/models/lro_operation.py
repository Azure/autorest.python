# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any, Optional
from .imports import FileImport
from .operation import Operation
from .parameter import Parameter
from .schema_response import SchemaResponse
from .imports import ImportType

_LOGGER = logging.getLogger(__name__)


class LROOperation(Operation):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        url: str,
        method: str,
        summary: Optional[str] = None,
        parameters: List[Parameter] = None,
        responses: List[SchemaResponse] = None,
        exceptions: List[SchemaResponse] = None,
        media_types: List[str] = None,
        want_description_docstring: Optional[bool] = True,
        want_tracing: Optional[bool] = True,
    ) -> None:
        super(LROOperation, self).__init__(
            yaml_data,
            name,
            description,
            url,
            method,
            summary,
            parameters,
            responses,
            exceptions,
            media_types,
            want_description_docstring,
            want_tracing,
        )
        self.lro_response: Optional[SchemaResponse] = None
        self.lro_options = yaml_data.get("extensions", {}).get("x-ms-long-running-operation-options", {})

    def set_lro_response_type(self) -> None:
        if not self.responses:
            return
        responses = {response.schema: response for response in self.responses if response.has_body}
        response_types = list(responses.values())
        if len(response_types) > 1:
            _LOGGER.warning("Multiple schema types in responses: %s", response_types)
        self.lro_response = response_types.pop() if response_types else None

    def imports(self, code_model, async_mode: bool) -> FileImport:
        file_import = super().imports(code_model, async_mode)
        if async_mode:
            file_import.add_from_import("typing", "Optional", ImportType.STDLIB)
            file_import.add_from_import("azure.core.polling", "async_poller", ImportType.AZURECORE)
            file_import.add_from_import("azure.core.polling", "AsyncNoPolling", ImportType.AZURECORE)
            if code_model.options['azure_arm']:
                file_import.add_from_import(
                    "azure.mgmt.core.polling.async_arm_polling", "AsyncARMPolling", ImportType.AZURECORE
                )
        else:
            file_import.add_from_import("azure.core.polling", "LROPoller", ImportType.AZURECORE)
            file_import.add_from_import("azure.core.polling", "NoPolling", ImportType.AZURECORE)
            if code_model.options['azure_arm']:
                file_import.add_from_import("azure.mgmt.core.polling.arm_polling", "ARMPolling", ImportType.AZURECORE)
        return file_import
