# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, Any
from jinja2 import Environment

from autorest.codegen.models.credential_types import AzureKeyCredentialType
from autorest.codegen.models.credential_types import TokenCredentialType
from autorest.codegen.models.imports import FileImport, ImportType
from autorest.codegen.models.operation import OperationBase
from autorest.codegen.models.operation_group import OperationGroup
from autorest.codegen.serializers.import_serializer import FileImportSerializer
from ..models import CodeModel
from .utils import operation_additional

_LOGGER = logging.getLogger(__name__)


class SampleSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        operation_group: OperationGroup,
        operation: OperationBase[Any],
        sample: Dict[str, Any],
        file_name: str,
        sample_origin_name: str,
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.operation = operation
        self.sample = sample
        self.file_name = file_name
        self.sample_origin_name = sample_origin_name

    def _handle_sample_value(self, rest_api_name: str) -> str:
        value = self.sample["parameters"].get(rest_api_name)
        return "" if not value else f'"{value}"'

    def _prepare_sample_render_param(self) -> Dict[str, Any]:
        # client params
        credential = ""
        credential_type = getattr(self.code_model.credential, "type", None)
        if isinstance(credential_type, TokenCredentialType):
            credential = "DefaultAzureCredential"
            third_party = "azure.identity"
        elif isinstance(credential_type, AzureKeyCredentialType):
            credential = "AzureKeyCredential"
            third_party = "azure.core.credentials"

        additional_info = (
            'key=os.getenv("AZURE_KEY")' if credential == "AzureKeyCredential" else ""
        )
        special_param = {
            "credential": f"{credential}({additional_info})",
        }
        params_positional = [
            p
            for p in self.code_model.client.parameters.positional
            if not (p.optional or p.client_default_value)
        ]
        client_params = {
            p.client_name: special_param.get(
                p.client_name,
                self._handle_sample_value(p.rest_api_name)
                or f'"{p.client_name.upper()}"',
            )
            for p in params_positional
        }
        if self.code_model.options["multiapi"]:
            client_params["api_version"] = f'"{self.operation_group.api_versions[0]}"'

        # imports
        imports = FileImport()
        namespace = (self.code_model.options["package_name"] or "").replace(
            "-", "."
        ) or self.code_model.namespace
        imports.add_submodule_import(
            namespace, self.code_model.client.name, ImportType.THIRDPARTY
        )
        if credential:
            imports.add_import("os", ImportType.STDLIB)
            imports.add_submodule_import(third_party, credential, ImportType.THIRDPARTY)

        # operation group name
        operation_group_name = (
            ""
            if self.operation_group.is_mixin
            else f".{self.operation_group.property_name}"
        )

        return {
            "file_name": self.file_name,
            "origin_file": self.sample.get("x-ms-original-file"),
            "imports": FileImportSerializer(imports, True),
            "client_params": client_params,
            "operation_group_name": operation_group_name,
            "operation_result": operation_additional(self.operation),
            "operation_name": f".{self.operation.name}",
        }

    # prepare method parameters
    def _sample_operation_params(
        self,
    ) -> Dict[str, Any]:
        params_positional = [
            p
            for p in self.operation.parameters.positional
            if not p.client_default_value
        ]
        cls = lambda x: f'"{x}"' if isinstance(x, str) else str(x)
        failure_info = '"fail to find required param named {%s} in example file {%s}"'
        operation_params = {}
        for param in params_positional:
            name = param.rest_api_name
            fake_value = param.client_name.upper()
            param_value = self.sample["parameters"].get(name)
            if param_value or not param.optional:
                if not param_value:
                    # if can't find required param, need to log it
                    _LOGGER.warning(failure_info, name, self.sample_origin_name)
                    param_value = fake_value
                operation_params[param.client_name] = cls(param_value)
        return operation_params

    def serialize(self) -> str:
        sample_params = self._prepare_sample_render_param()
        operation_params = self._sample_operation_params()
        return self.env.get_template("sample.py.jinja2").render(
            code_model=self.code_model,
            operation_params=operation_params,
            **sample_params,
        )
