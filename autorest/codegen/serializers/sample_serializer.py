# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, Any, Callable
from pathlib import Path
from jinja2 import Environment
from ..serializers.import_serializer import FileImportSerializer
from ..models import CodeModel
from ..models.imports import FileImport, ImportType
from ..models.credential_types import TokenCredentialType
from ..models.credential_types import AzureKeyCredentialType
from .utils import (
    to_snake_case,
    operation_additional,
    package_root_folder,
)

_LOGGER = logging.getLogger(__name__)


class SampleSerializer:
    def __init__(
        self,
        namespace_path: Path,
        code_model: CodeModel,
        env: Environment,
        write_func: Callable[[Path, str], None],
    ) -> None:
        self.namespace_path = namespace_path
        self.code_model = code_model
        self.env = env
        self.write_func = write_func

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
        # rest_api_name: [client_name, value]
        client_params = {
            p.rest_api_name: [
                p.client_name,
                special_param.get(p.client_name, f'"{p.client_name.upper()}"'),
            ]
            for p in params_positional
        }

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

        return {
            "imports": FileImportSerializer(imports, True),
            "client_params": client_params,
        }

    def serialize_and_write(self) -> None:
        template = self.env.get_template("sample.py.jinja2")
        out_path = package_root_folder(
            self.code_model.namespace, self.namespace_path
        ) / Path("generated_samples")
        sample_params = self._prepare_sample_render_param()
        cls = lambda x: f'"{x}"' if isinstance(x, str) else str(x)
        failure_info = '"fail to find required param named {%s} in example file {%s}"'
        # pylint: disable=too-many-nested-blocks
        for op_group in self.code_model.operation_groups:
            if self.code_model.options["multiapi"]:
                api_version_folder = f"{op_group.api_versions[0]}/"
                sample_params["client_params"]["apiVersion"] = [
                    "api_version",
                    f'"{op_group.api_versions[0]}"',
                ]
            else:
                api_version_folder = ""
            sample_params["operation_group_name"] = (
                "" if op_group.is_mixin else f".{op_group.property_name}"
            )
            for operation in op_group.operations:
                samples = operation.yaml_data["samples"]
                if not samples:
                    continue
                params_positional = [
                    p
                    for p in operation.parameters.positional
                    if not p.client_default_value
                ]
                sample_params["operation_result"] = operation_additional(operation)
                sample_params["operation_name"] = f".{operation.name}"
                for key, value in samples.items():
                    # update client parameters if it is defined in example files
                    for param in sample_params["client_params"].keys():
                        p_value = value["parameters"].get(param)
                        if p_value:
                            sample_params["client_params"][param][1] = f'"{p_value}"'

                    # prepare method parameters
                    operation_params = {}
                    for param in params_positional:
                        name = param.rest_api_name
                        fake_value = param.client_name.upper()
                        param_value = value["parameters"].get(name)
                        if param_value or not param.optional:
                            if not param_value:
                                # if can't find required param, need to log it
                                _LOGGER.warning(failure_info, name, key)
                                param_value = fake_value
                            operation_params[param.client_name] = cls(param_value)

                    # serialize and output
                    try:
                        file_name = to_snake_case(key) + ".py"
                        sample_params["file_name"] = file_name
                        sample_params["origin_file"] = value.get("x-ms-original-file")
                        self.write_func(
                            out_path / f"{api_version_folder}{file_name}",
                            template.render(
                                code_model=self.code_model,
                                operation_params=operation_params,
                                **sample_params,
                            ),
                        )
                    except Exception as e:  # pylint: disable=broad-except
                        # sample generation shall not block code generation, so just log error
                        _LOGGER.error(
                            "error happens when generate sample with {%s}: {%s}", key, e
                        )
