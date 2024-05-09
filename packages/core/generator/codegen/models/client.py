# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
from typing import TYPE_CHECKING, Protocol
from .base import PythonYaml

from .backcompat import ClientBackcompatMixin
from ... import types
from .property_types import get_client_parameter

if TYPE_CHECKING:
    from .sdk_package import SdkPackage


class Client(PythonYaml[types.YamlClient], ClientBackcompatMixin):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlClient) -> None:
        super().__init__(sdk_package, yaml_data)
        self.name = yaml_data["name"]
        self.description = yaml_data["description"]
        self.parameters = [get_client_parameter(sdk_package, p) for p in yaml_data["parameters"]]
        self.sub_clients = [Client(sdk_package, c) for c in yaml_data.get("subClients", [])]
        self.public_initialization: bool = yaml_data["publicInitialization"]

    @property
    def filename(self) -> str:
        return self.get_filename(self.yaml_data["name"])

