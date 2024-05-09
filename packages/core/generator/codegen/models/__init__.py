# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
import typing
from ... import types
from .sdk_types import PythonSdkType

if typing.TYPE_CHECKING:
    from .sdk_package import SdkPackage



def get_type(sdk_package: SdkPackage, yaml_data: types.YamlSdkType) -> PythonSdkType:
    ...


