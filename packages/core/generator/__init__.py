# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Protocol, Union

import yaml

from .types import YamlData, Options

class ApiProtocol(Protocol):

    def read(self, path: Union[str, Path]) -> str:
        ...

    def write(self, path: Union[str, Path], content: str) -> None:
        ...

    def get_options(self) -> Options:
        ...


class Plugin(ABC):
    """A base class for a plugin."""

    def __init__(self, api: ApiProtocol) -> None:
        self.api = api
        self.options = self.api.get_options()

    @abstractmethod
    def process(self) -> bool:
        """The plugin process.

        :rtype: bool
        :return: True if the process is successful, False otherwise.
        """
        ...

class YamlUpdatePlugin(Plugin):
    """A plugin that updates the YAML as input before being passed to the code generator."""

    def get_yaml(self) -> YamlData:
        return yaml.safe_load(self.api.read(self.options["yamlFile"]))

    def write_yaml(self, content: str) -> None:
        self.api.write(self.options["yamlFile"], content)

    def process(self) -> bool:
        yaml_data = self.get_yaml()
        self.update_yaml(yaml_data)
        content = yaml.safe_dump(yaml_data)
        self.write_yaml(content)
        return True
    
    @abstractmethod
    def update_yaml(self, yaml_data: YamlData) -> None:
        """Update the YAML data.

        :param yaml_data: The YAML data.
        :type yaml_data: YamlData
        """
        ...
