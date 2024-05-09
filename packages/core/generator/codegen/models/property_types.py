# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
import typing

from packages.core.generator.codegen.models.sdk_package import SdkPackage
from . import get_type
from .sdk_types import PythonYaml
from ... import types

if typing.TYPE_CHECKING:
    from .sdk_package import SdkPackage

TPropertyYaml = typing.TypeVar('TPropertyYaml', bound=types.YamlPropertyType)

class PropertyTypeBase(PythonYaml[TPropertyYaml]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlPropertyType) -> None:
        super().__init__(sdk_package, yaml_data) # type: ignore
        self.type = get_type(sdk_package, yaml_data["type"])
        self.name = yaml_data["name"]
        self.description = yaml_data["description"]
        self.client_default_value = yaml_data["clientDefaultValue"]
        self.optional = yaml_data["optional"]
        self.on_client = yaml_data["onClient"]

class EndpointParameter(PropertyTypeBase[types.YamlEndpointParameter]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlEndpointParameter) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]

class CredentialParameter(PropertyTypeBase[types.YamlCredentialParameter]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlCredentialParameter) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]

class MethodParameter(PropertyTypeBase[types.YamlMethodParameter]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlBodyModelPropertyType | types.YamlEndpointParameter | types.YamlCredentialParameter | types.YamlHeaderParameter | types.YamlPathParameter | types.YamlQueryParameter | types.YamlBodyParameter | types.YamlMethodParameter) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]

class HeaderParameter(PropertyTypeBase[types.YamlHeaderParameter]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlHeaderParameter) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.collection_format = yaml_data["collectionFormat"]
        self.serializedName = yaml_data["serializedName"]

class QueryParameter(PropertyTypeBase[types.YamlQueryParameter]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlQueryParameter) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.collection_format = yaml_data["collectionFormat"]
        self.serializedName = yaml_data["serializedName"]

class PathParameter(PropertyTypeBase[types.YamlPathParameter]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlPathParameter) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.serializedName = yaml_data["serializedName"]

class BodyParameter(PropertyTypeBase[types.YamlBodyParameter]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlBodyParameter) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        self.content_types = yaml_data["contentTypes"]
        self.default_content_type = yaml_data["defaultContentType"]
