# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Any, Dict, Union

import yaml

from .jsonrpc import AutorestAPI
from ._version import VERSION


__version__ = VERSION
_LOGGER = logging.getLogger(__name__)


class Plugin(ABC):
    """A base class for autorest plugin.

    :param autorestapi: An autorest API instance
    """

    def __init__(self, options: Dict[str, Any]) -> None:
        self.options = options

    @abstractmethod
    def process(self) -> bool:
        """The plugin process.

        :rtype: bool
        :returns: True if everything's ok, False optherwise
        :raises Exception: Could raise any exception, stacktrace will be sent to autorest API
        """
        raise NotImplementedError()

    def read_file(self, path: Path) -> str:
        """How does one read a file in cadl?"""

    def write_file(self, filename: Union[str, Path], file_content: str) -> None:
        """How does writing work in cadl?"""


class PluginAutorest(Plugin, ABC):
    """For our Autorest plugins, we want to take autorest api as input as options, then pass it to the Plugin"""

    def __init__(self, autorestapi: AutorestAPI) -> None:
        self._autorestapi = autorestapi
        super().__init__(self.get_options())

    @abstractmethod
    def get_options(self) -> Dict[str, Any]:
        """Get the options bag using the AutorestAPI that we send to the parent plugin"""

    def read_file(self, path: Union[str, Path]) -> str:
        return self._autorestapi.read_file(path)

    def write_file(self, filename: Union[str, Path], file_content: str) -> None:
        return self._autorestapi.write_file(filename, file_content)



class YamlUpdatePlugin(Plugin):
    """A plugin that update the YAML as input."""

    def process(self) -> bool:
        # List the input file, should be only one
        file_content = self.options["inputFile"]
        yaml_data = yaml.safe_load(file_content)

        self.update_yaml(yaml_data)

        yaml_string = yaml.safe_dump(yaml_data)

        self.write_file("code-model-v4-no-tags.yaml", yaml_string)
        return True

    @abstractmethod
    def update_yaml(self, yaml_data: Dict[str, Any]) -> None:
        """The code-model-v4-no-tags yaml model tree.

        :rtype: updated yaml
        :raises Exception: Could raise any exception, stacktrace will be sent to autorest API
        """
        raise NotImplementedError()

class YamlUpdatePluginAutorest(YamlUpdatePlugin, PluginAutorest):

    def get_options(self) -> Dict[str, Any]:
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")
        return {
            "inputFile": self._autorestapi.read_file("code-model-v4-no-tags.yaml")
        }
