# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, Any, Union
from pathlib import Path
import yaml

from coregen.codegen import CodeGenerator
from coregen.codegen.serializers import JinjaSerializer
from coregen.codegen.models import CodeModel


from ..jsonrpc import AutorestAPI
from .. import PluginAutorest, ReaderAndWriterAutorest

_LOGGER = logging.getLogger(__name__)


class JinjaSerializerAutorest(JinjaSerializer, ReaderAndWriterAutorest):
    def __init__(
        self,
        autorestapi: AutorestAPI,
        code_model: CodeModel,
        *,
        output_folder: Union[str, Path],
    ) -> None:
        super().__init__(
            autorestapi=autorestapi, code_model=code_model, output_folder=output_folder
        )


class CodeGeneratorAutorest(CodeGenerator, PluginAutorest):
    def get_options(self) -> Dict[str, Any]:
        if self._autorestapi.get_boolean_value("python3-only") is False:
            _LOGGER.warning(
                "You have passed in --python3-only=False. We have force overriden "
                "this to True."
            )
        if self._autorestapi.get_boolean_value("add-python3-operation-files"):
            _LOGGER.warning(
                "You have passed in --add-python3-operation-files. "
                "This flag no longer has an effect bc all SDKs are now Python3 only."
            )
        if self._autorestapi.get_boolean_value("reformat-next-link"):
            _LOGGER.warning(
                "You have passed in --reformat-next-link. We have force overriden "
                "this to False because we no longer reformat initial query parameters into next "
                "calls unless explicitly defined in the service definition."
            )
        version_tolerant = self._autorestapi.get_boolean_value("version-tolerant", True)
        low_level_client = self._autorestapi.get_boolean_value(
            "low-level-client", False
        )
        models_mode_default = (
            "none" if low_level_client or version_tolerant else "msrest"
        )
        options = {
            "azure-arm": self._autorestapi.get_boolean_value("azure-arm"),
            "header-text": self._autorestapi.get_value("header-text"),
            "low-level-client": low_level_client,
            "version-tolerant": version_tolerant,
            "show-operations": self._autorestapi.get_boolean_value("show-operations"),
            "python3-only": self._autorestapi.get_boolean_value("python3-only"),
            "head-as-boolean": self._autorestapi.get_boolean_value(
                "head-as-boolean", False
            ),
            "keep-version-file": self._autorestapi.get_boolean_value(
                "keep-version-file"
            ),
            "no-async": self._autorestapi.get_boolean_value("no-async"),
            "no-namespace-folders": self._autorestapi.get_boolean_value(
                "no-namespace-folders"
            ),
            "basic-setup-py": self._autorestapi.get_boolean_value("basic-setup-py"),
            "package-name": self._autorestapi.get_value("package-name"),
            "package-version": self._autorestapi.get_value("package-version"),
            "client-side-validation": self._autorestapi.get_boolean_value(
                "client-side-validation"
            ),
            "tracing": self._autorestapi.get_boolean_value("trace"),
            "multiapi": self._autorestapi.get_boolean_value("multiapi", False),
            "polymorphic-examples": self._autorestapi.get_value("polymorphic-examples"),
            "models-mode": self._autorestapi.get_value("models-mode")
            or models_mode_default,
            "builders-visibility": self._autorestapi.get_value("builders-visibility"),
            "show-send-request": self._autorestapi.get_boolean_value(
                "show-send-request"
            ),
            "only-path-and-body-params-positional": self._autorestapi.get_boolean_value(
                "only-path-and-body-params-positional"
            ),
            "combine-operation-files": self._autorestapi.get_boolean_value(
                "combine-operation-files"
            ),
            "package-mode": self._autorestapi.get_value("package-mode"),
            "package-pprint-name": self._autorestapi.get_value("package-pprint-name"),
            "package-configuration": self._autorestapi.get_value(
                "package-configuration"
            ),
            "default-optional-constants-to-none": self._autorestapi.get_boolean_value(
                "default-optional-constants-to-none"
            ),
        }
        return {k: v for k, v in options.items() if v is not None}

    def get_yaml(self) -> Dict[str, Any]:
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

        if self._autorestapi.get_value("input-yaml"):
            input_yaml = self._autorestapi.get_value("input-yaml")
            file_content = self._autorestapi.read_file(input_yaml)
        else:
            inputs = self._autorestapi.list_inputs()
            _LOGGER.debug("Possible Inputs: %s", inputs)
            if "code-model-v4-no-tags.yaml" not in inputs:
                raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

            file_content = self._autorestapi.read_file("code-model-v4-no-tags.yaml")

        # Parse the received YAML
        return yaml.safe_load(file_content)

    def get_serializer(self, code_model: CodeModel):  # type: ignore
        return JinjaSerializerAutorest(
            self._autorestapi, code_model, output_folder=self.output_folder
        )
