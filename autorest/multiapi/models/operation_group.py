# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, List, TypeVar

T = TypeVar('T')
OrderedSet = Dict[T, None]

class OperationGroup(object):
    def __init__(self, name: str, class_name: str):
        self.name = name
        self.class_name = class_name
        self._available_apis: OrderedSet[str] = {}

    @property
    def available_apis(self) -> List[str]:
        return list(self._available_apis.keys())

    def append_available_api(self, val: str) -> None:
        self._available_apis[val] = None
