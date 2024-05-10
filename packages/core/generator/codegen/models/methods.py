# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from __future__ import annotations
from typing import TypeVar, Generic
from .sdk_package import SdkPackage
from .base import PythonYaml
from .property_types import MethodParameter
from .responses import MethodResponse


from ... import types

TYamlServiceMethod = TypeVar("TYamlServiceMethod", bound=types.YamlServiceMethod)

class _ServiceMethodBase(PythonYaml[TYamlServiceMethod]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: TYamlServiceMethod) -> None:
        super().__init__(sdk_package, yaml_data)
        self.name = yaml_data["name"]
        self.description = yaml_data["description"]
        self.parameters = [MethodParameter(sdk_package, p) for p in yaml_data["parameters"]]
        self.operation = HttpOperation.from_yaml(sdk_package, yaml_data["operation"])
        self.response = MethodResponse(sdk_package, yaml_data["response"])
        yaml_exception = yaml_data.get("exception")
        self.exception = MethodResponse(sdk_package, yaml_exception) if yaml_exception else None
        self.cross_language_definition_id = yaml_data.get("crossLanguageDefinitionId")

class BasicServiceMethod(_ServiceMethodBase[types.YamlBasicServiceMethod]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlBasicServiceMethod) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]

class PagingServiceMethod(_ServiceMethodBase[types.YamlPagingServiceMethod]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlPagingServiceMethod) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]
        yaml_next_operation = yaml_data.get("nextOperation")
        self.next_operation = HttpOperation.from_yaml(sdk_package, yaml_next_operation) if yaml_next_operation else None
        self.next_link_path = yaml_data["nextLinkPath"]

class LroServiceMethod(_ServiceMethodBase[types.YamlLroServiceMethod]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlLroServiceMethod) -> None:
        super().__init__(sdk_package, yaml_data)
        self.kind = yaml_data["kind"]

class HttpOperation(PythonYaml[types.YamlHttpOperation]):
    def __init__(self, sdk_package: SdkPackage, yaml_data: types.YamlHttpOperation) -> None:
        super().__init__(sdk_package, yaml_data)
        self.verb = yaml_data["verb"]
        self.path = yaml_data["path"]

