# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
import typing
from ... import types
from .sdk_package import SdkPackage

TPythonYaml = typing.TypeVar('TPythonYaml', bound='PythonYaml')
TYamlType = typing.TypeVar('TYamlType', bound=types.YamlType)

class PythonYaml(typing.Generic[TYamlType]):
    """Any codegen type that can be created from a yaml file."""
    def __init__(self, sdk_package: SdkPackage, yaml_data: TYamlType) -> None:
        self.sdk_package = sdk_package
        self.yaml_data = yaml_data

    @property
    def id(self) -> int:
        return id(self.yaml_data)
    
    @classmethod
    def from_yaml(cls: typing.Type[TPythonYaml], sdk_package: SdkPackage, yaml_data: types.YamlType) -> TPythonYaml:
        """Create a PythonYaml object from a yaml data object."""
        return cls(sdk_package, yaml_data)
