# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
from .base import PythonYaml
from .sdk_package import SdkPackage
from ... import types
from . import get_type

class MethodResponse(PythonYaml[types.YamlMethodResponse]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlMethodResponse) -> None:
        super().__init__(sdk_package, yaml_data)
        self.result_path = yaml_data["resultPath"]
        yaml_type = yaml_data.get("type")
        self.type = get_type(sdk_package, yaml_type) if yaml_type else None
