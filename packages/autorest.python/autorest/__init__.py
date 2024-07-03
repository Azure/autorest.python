# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from pathlib import Path
from abc import abstractmethod
from typing import Any, Dict, Union, List

import yaml

from pygen import ReaderAndWriter, Plugin, YamlUpdatePlugin
from .jsonrpc import AutorestAPI


_LOGGER = logging.getLogger(__name__)


class ReaderAndWriterAutorest(ReaderAndWriter):
    def __init__(self, *, output_folder: Union[str, Path], autorestapi: AutorestAPI) -> None:
        super().__init__(output_folder=output_folder)
        self._autorestapi = autorestapi

    def read_file(self, path: Union[str, Path]) -> str:
        return self._autorestapi.read_file(path)

    def write_file(self, filename: Union[str, Path], file_content: str) -> None:
        return self._autorestapi.write_file(filename, file_content)

    def list_file(self) -> List[str]:
        return self._autorestapi.list_inputs()


class PluginAutorest(Plugin, ReaderAndWriterAutorest):
    """For our Autorest plugins, we want to take autorest api as input as options, then pass it to the Plugin"""

    def __init__(self, autorestapi: AutorestAPI, *, output_folder: Union[str, Path]) -> None:
        super().__init__(autorestapi=autorestapi, output_folder=output_folder)
        self.options = self.get_options()

    @abstractmethod
    def get_options(self) -> Dict[str, Any]:
        """Get the options bag using the AutorestAPI that we send to the parent plugin"""


class YamlUpdatePluginAutorest(YamlUpdatePlugin, PluginAutorest):  # pylint: disable=abstract-method
    def get_yaml(self) -> Dict[str, Any]:
        return yaml.safe_load(self.read_file("code-model-v4-no-tags.yaml"))

    def write_yaml(self, yaml_string: str) -> None:
        self.write_file("code-model-v4-no-tags.yaml", yaml_string)

    def get_options(self) -> Dict[str, Any]:
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")
        return {}
