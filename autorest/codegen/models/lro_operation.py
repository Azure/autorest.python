# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, List, Any, Optional, Set, cast
from .imports import FileImport
from .operation import Operation
from .parameter import Parameter
from .schema_response import SchemaResponse
from .schema_request import SchemaRequest
from .imports import ImportType, TypingSection
from .base_schema import BaseSchema

_LOGGER = logging.getLogger(__name__)


class LROOperation(Operation):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        description: str,
        url: str,
        method: str,
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
        super(LROOperation, self).__init__(
            yaml_data,
            name,
            description,
            url,
            method,
            api_versions,
            requests,
            summary,
            parameters,
            multiple_media_type_parameters,
            responses,
            exceptions,
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
        response_type = None
        if len(response_types) > 1:
            # choose the response that has a status code of 200
            response_types_with_200_status_code = [
                rt for rt in response_types if 200 in rt.status_codes
            ]
            if not response_types_with_200_status_code:
                raise ValueError(
                    f"Your swagger is invalid because you have multiple response schemas for LRO" +
                    f" method {self.python_name} and none of them have a 200 status code."
                )
            response_type = response_types_with_200_status_code[0]

            response_type_schema_name = cast(BaseSchema, response_type.schema).serialization_type
            _LOGGER.warning(
                "Multiple schema types in responses: %s. Choosing: %s", response_types, response_type_schema_name
            )
        elif response_types:
            response_type = response_types[0]
        self.lro_response = response_type

    @property
    def has_optional_return_type(self) -> bool:
        """An LROOperation will never have an optional return type, we will always return LROPoller[return type]"""
        return False

    def imports(self, code_model, async_mode: bool) -> FileImport:
        file_import = super().imports(code_model, async_mode)
        file_import.add_from_import("typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL)
        if async_mode:
            file_import.add_from_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)
            file_import.add_from_import("azure.core.polling", "AsyncLROPoller", ImportType.AZURECORE)
            file_import.add_from_import("azure.core.polling", "AsyncNoPolling", ImportType.AZURECORE)
            file_import.add_from_import("azure.core.polling", "AsyncPollingMethod", ImportType.AZURECORE)
            if code_model.options['azure_arm']:
                file_import.add_from_import(
                    "azure.mgmt.core.polling.async_arm_polling", "AsyncARMPolling", ImportType.AZURECORE
                )
            else:
                file_import.add_from_import(
                    "azure.core.polling.async_base_polling", "AsyncLROBasePolling", ImportType.AZURECORE
                )
        else:
            file_import.add_from_import("azure.core.polling", "LROPoller", ImportType.AZURECORE)
            file_import.add_from_import("azure.core.polling", "NoPolling", ImportType.AZURECORE)
            file_import.add_from_import("azure.core.polling", "PollingMethod", ImportType.AZURECORE)
            if code_model.options['azure_arm']:
                file_import.add_from_import("azure.mgmt.core.polling.arm_polling", "ARMPolling", ImportType.AZURECORE)
            else:
                file_import.add_from_import("azure.core.polling.base_polling", "LROBasePolling", ImportType.AZURECORE)
        return file_import
