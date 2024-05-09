# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
import typing

from packages.core.generator.codegen.models import get_type
from packages.core.generator.codegen.models.sdk_package import SdkPackage
from ... import types
from .property_types import PathParameter

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


class _PythonSdkTypeBase(PythonYaml[TYamlType]):
    """Represents a Python SDK type, i.e. a model, an enum, etc.."""
    def __init__(self, sdk_package: SdkPackage, yaml_data: TYamlType) -> None:
        super().__init__(sdk_package, yaml_data)

class BuiltInType(_PythonSdkTypeBase[types.YamlBuiltInType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlBuiltInType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.encode = yaml_data["encode"]

class ConstantType(_PythonSdkTypeBase[types.YamlConstantType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlConstantType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.value = yaml_data["value"]

class CredentialType(_PythonSdkTypeBase[types.YamlCredentialType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlCredentialType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.scheme = yaml_data["scheme"]

class DictionaryType(_PythonSdkTypeBase[types.YamlDictionaryType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlDictionaryType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.value_type = get_type(sdk_package, yaml_data["valueType"])

class EndpointType(_PythonSdkTypeBase[types.YamlEndpointType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlEndpointType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.server_url = yaml_data["serverUrl"]
        self.template_arguments = [PathParameter.from_yaml(sdk_package, p) for p in yaml_data["templateArguments"]]

class EnumType(_PythonSdkTypeBase[types.YamlEnumType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlEnumType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.values = [EnumValueType.from_yaml(sdk_package, v) for v in yaml_data["values"]]
        self.value_type = get_type(sdk_package, yaml_data["valueType"])
        self.cross_language_definition_id = yaml_data["crossLanguageDefinitionId"]

class EnumValueType(_PythonSdkTypeBase[types.YamlEnumValueType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlEnumValueType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.name = yaml_data["name"]
        self.value = yaml_data["value"]
        self.enum_type = get_type(sdk_package, yaml_data["enumType"])

class ListType(_PythonSdkTypeBase[types.YamlListType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlListType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.value_type = get_type(sdk_package, yaml_data["valueType"])

class ModelType(_PythonSdkTypeBase[types.YamlModelType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlModelType, *, parents: typing.List[ModelType] = []) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.parents = parents

class UnionType(_PythonSdkTypeBase[types.YamlUnionType]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlUnionType) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.name = yaml_data.get("name")


PythonSdkType = typing.Union[
    ConstantType,
    CredentialType,
    DictionaryType, 
    ModelType,
    UnionType
]
