# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
from typing import TYPE_CHECKING, Protocol

from . import  PythonYaml
from .backcompat import ClientBackcompatMixin
from ...types import YamlClient
from ...utils import to_snake_case

if TYPE_CHECKING:
    from .sdk_package import SdkPackage




class Client(PythonYaml[YamlClient], ClientBackcompatMixin):
    @property
    def filename(self) -> str:
        return self.get_filename(self.yaml_data["name"])

