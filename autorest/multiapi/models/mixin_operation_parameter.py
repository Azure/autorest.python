# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, TypeVar

T = TypeVar('T')
OrderedSet = Dict[T, None]

class MixinOperationParameter:
    def __init__(self, name: str):
        self.name = name
        self._available_apis: OrderedSet = {}

    @property
    def api_version_added(self):
        return list(self._available_apis)[0]

    def append_available_api(self, api_version: str) -> None:
        self._available_apis[api_version] = None

    def __eq__(self, other):
        return self.name == other.name
