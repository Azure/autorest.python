# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Set, TypeVar
from ..utils import _sync_or_async

T = TypeVar('T')
OrderedSet = Dict[T, None]

class MixinOperation:
    def __init__(self, name: str, mod_to_api_version: Dict[str, str]):
        self.name = name
        self._mod_to_api_version = mod_to_api_version
        self._api_version_to_mixin_operation_metadata: Dict[str, Dict[str, Any]] = {}
        self._available_apis: OrderedSet[str] = {}
        self.call_to_api_versions: Dict[str, List[str]] = {}
        self._union_of_all_params: Set[str] = set()

    def signature(self, async_mode: bool) -> str:
        return self.mixin_operation_metadata()[_sync_or_async(async_mode)]["signature"]

    def description(self, async_mode: bool) -> str:
        return self.mixin_operation_metadata()[_sync_or_async(async_mode)]["doc"]

    def coroutine(self, async_mode: bool) -> bool:
        if not async_mode:
            return False
        return self.mixin_operation_metadata()["async"]["coroutine"]

    def mixin_operation_metadata(self, api_version=None):
        if not api_version:
            api_version = self._last_api_version
        return self._api_version_to_mixin_operation_metadata[api_version]

    @property
    def _last_api_version(self) -> str:
        return list(self._available_apis.keys())[-1]

    def call(self, api_version=None) -> str:
        if not api_version and self.has_different_calls_across_api_versions:
            raise ValueError(
                "This property should only be called if your call is the same across all API versions"
            )
        return self.mixin_operation_metadata(api_version)["call"]

    @property
    def available_apis(self) -> List[str]:
        return list(self._available_apis.keys())

    @property
    def has_different_calls_across_api_versions(self) -> bool:
        return len(self.call_to_api_versions) != 1

    @property
    def api_version_to_unallowed_params(self) -> Dict[str, List[str]]:
        _api_version_to_unallowed_params: Dict[str, List[str]] = {}
        if not self.has_different_calls_across_api_versions:
            raise ValueError(
                "Should only call this property if this mixin operation has different signatures per api version"
            )
        for api in self.available_apis:
            api_params = self.call(api).split(", ")
            api_unallowed_params = self._union_of_all_params.difference(api_params)
            _api_version_to_unallowed_params.setdefault(self._mod_to_api_version[api], [])
            _api_version_to_unallowed_params[self._mod_to_api_version[api]].extend(api_unallowed_params)
        return _api_version_to_unallowed_params


    def append_available_api(self, api_version: str, mixin_operation_metadata: Dict[str, Any]) -> None:
        self._available_apis[api_version] = None

        call = mixin_operation_metadata["call"]
        self.call_to_api_versions.setdefault(call, [])
        self.call_to_api_versions[call].append(self._mod_to_api_version[api_version])

        self._union_of_all_params.update(call.split(", "))

        self._api_version_to_mixin_operation_metadata[api_version] = mixin_operation_metadata
