# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import Dict, List

from ...types import Options, YamlData
from . import PythonSdkType
from .model_type import ModelType
from .client import Client
from .utils import sort_model_types
from .backcompat import SdkPackageBackcompatMixin
from .union_type import UnionType

class SdkPackage(SdkPackageBackcompatMixin):
    def __init__(self, yaml_data: YamlData, options: Options) -> None:
        self.yaml_data = yaml_data
        self.options = options
        self.namespace = self.yaml_data["namespace"]
        self.types_map: Dict[int, PythonSdkType] = {}  # map yaml id to schema
        self.model_types: List[ModelType] = []
        from . import get_type

        for type_yaml in self.yaml_data["types"]:
            get_type(sdk_package=self, yaml_data=type_yaml)
        self.clients: List[Client] = [
            Client.from_yaml(self, client_yaml) for client_yaml in self.yaml_data["clients"]
        ]
        self.subnamespace_to_clients: Dict[str, List[Client]] = {
            subnamespace: [Client.from_yaml(self, client_yaml) for client_yaml in client_yamls]
            for subnamespace, client_yamls in yaml_data["subnamespaceToClients"].items()
        }
        if self.options["modelsMode"] and self.model_types:
            sort_model_types(self.model_types)
        self.named_unions: List[UnionType] = [
            t for t in self.types_map.values() if t.kind == "union" and t.name
        ]
        self.cross_language_package_id = self.yaml_data["crossLanguagePackageId"]

    @property
    def models_filename(self) -> str:
        return self.get_models_filename()
    
    @property
    def enums_filename(self) -> str:
        return self.get_enums_filename(self.clients[0].filename)

