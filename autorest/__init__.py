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


class ReaderAndWriter:
    def __init__(
        self,
        *,
        output_folder: Union[str, Path],
        **kwargs: Any  # pylint: disable=unused-argument
    ) -> None:
        self.output_folder = Path(output_folder)

    def read_file(self, path: Union[str, Path]) -> str:
        """How does one read a file in cadl?"""
        # make path relative to output folder
        with open(self.output_folder / Path(path), "r") as fd:
            return fd.read()

    def write_file(self, filename: Union[str, Path], file_content: str) -> None:
        """How does writing work in cadl?"""
        with open(self.output_folder / Path(filename), "w") as fd:
            fd.write(file_content)


class ReaderAndWriterAutorest(ReaderAndWriter):
    def __init__(
        self, *, output_folder: Union[str, Path], autorestapi: AutorestAPI
    ) -> None:
        super().__init__(output_folder=output_folder)
        self._autorestapi = autorestapi

    def read_file(self, path: Union[str, Path]) -> str:
        return self._autorestapi.read_file(path)

    def write_file(self, filename: Union[str, Path], file_content: str) -> None:
        return self._autorestapi.write_file(filename, file_content)


class Plugin(ReaderAndWriter, ABC):
    """A base class for autorest plugin.

    :param autorestapi: An autorest API instance
    """

    def __init__(self, *, output_folder: Union[str, Path], **kwargs: Any) -> None:
        super().__init__(output_folder=output_folder, **kwargs)
        self.options: Dict[str, Any] = kwargs.pop("options", {})

    @abstractmethod
    def process(self) -> bool:
        """The plugin process.

        :rtype: bool
        :returns: True if everything's ok, False optherwise
        :raises Exception: Could raise any exception, stacktrace will be sent to autorest API
        """
        raise NotImplementedError()


class PluginAutorest(Plugin, ReaderAndWriterAutorest):
    """For our Autorest plugins, we want to take autorest api as input as options, then pass it to the Plugin"""

    def __init__(
        self, autorestapi: AutorestAPI, *, output_folder: Union[str, Path]
    ) -> None:
        super().__init__(autorestapi=autorestapi, output_folder=output_folder)
        self.options = self.get_options()

    @abstractmethod
    def get_options(self) -> Dict[str, Any]:
        """Get the options bag using the AutorestAPI that we send to the parent plugin"""


class YamlUpdatePlugin(Plugin):
    """A plugin that update the YAML as input."""

    def process(self) -> bool:
        # List the input file, should be only one
        yaml_data = yaml.safe_load(self.read_file("code-model-v4-no-tags.yaml"))

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


class YamlUpdatePluginAutorest(  # pylint: disable=abstract-method
    YamlUpdatePlugin, PluginAutorest
):
    def get_options(self) -> Dict[str, Any]:
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")
        return {}
