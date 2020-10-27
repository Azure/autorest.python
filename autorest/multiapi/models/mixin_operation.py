# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, TypeVar
from ..utils import _sync_or_async

T = TypeVar('T')
OrderedSet = Dict[T, None]

class MixinOperation:
    def __init__(self, name: str, mod_to_api_version: Dict[str, str]):
        self.name = name
        self._mod_to_api_version = mod_to_api_version
        self._api_version_to_mixin_operation_metadata: Dict[str, Dict[str, Any]] = {}
        self.param_to_api_versions: Dict[str, List[str]] = {}
        self._available_apis: OrderedSet[str] = {}
        self.call_to_api_versions: Dict[str, List[str]] = {}

    def signature(self, async_mode: bool) -> str:
        return self.mixin_operation_metadata()[_sync_or_async(async_mode)]["signature"]

    def _get_version_added_description(self, description: str) -> str:
        # remove trailing """ from docstring to insert version added information for params
        # will add back after adding version added information
        description = description.rsplit('"""', 1)[0] + "\n"

        version_added_to_params: Dict[str, List[str]] = {}

        for param in self.param_to_api_versions:
            if param in self.params_added_later:
                api_version_added = self.param_to_api_versions[param][0]
                version_added_to_params.setdefault(api_version_added, [])
                version_added_to_params[api_version_added].append(param)

        for api, params in version_added_to_params.items():
            parameter_string = "parameter" if len(params) == 1 else "parameters"
            param_names = [f"*{param}*" for param in params]

            description += f"**New in API version {api}**\n    The {parameter_string} "

            if len(params) == 1:
                description += f"{param_names[0]}"
            elif len(params) == 2:
                description += "{}".format(" and ".join(param_names))
            else:
                description += "{}, and {}".format(param_names[:-1], param_names[-1])

            description += '\n'

        return description + '"""'


    def description(self, async_mode: bool) -> str:
        description = self.mixin_operation_metadata()[_sync_or_async(async_mode)]["doc"]
        if not self.has_different_calls_across_api_versions:
            return description
        return self._get_version_added_description(description)

    def coroutine(self, async_mode: bool) -> bool:
        if not async_mode:
            return False
        return self.mixin_operation_metadata()["async"]["coroutine"]

    def mixin_operation_metadata(self, api_version=None):
        if not api_version:
            last_api_version = list(self._available_apis.keys())[-1]
            api_version = last_api_version
        return self._api_version_to_mixin_operation_metadata[api_version]

    @property
    def call(self) -> str:
        if self.has_different_calls_across_api_versions:
            raise ValueError(
                "This property should only be called if your call is the same across all API versions. "
                "Get the call from self.call_to_api_versions instead."
            )
        return self.mixin_operation_metadata()["call"]

    @property
    def available_apis(self) -> List[str]:
        return list(self._available_apis.keys())

    @property
    def has_different_calls_across_api_versions(self) -> bool:
        return len(self.call_to_api_versions) != 1

    @property
    def params_added_later(self) -> List[str]:
        return [
            param for param in self.param_to_api_versions
            if len(self.param_to_api_versions[param]) < len(self.available_apis)
        ]

    def append_available_api(self, api_version: str, mixin_operation_metadata: Dict[str, Any]) -> None:
        self._available_apis[api_version] = None

        call = mixin_operation_metadata["call"]
        self.call_to_api_versions.setdefault(call, [])
        self.call_to_api_versions[call].append(self._mod_to_api_version[api_version])

        for param in call.split(", "):
            self.param_to_api_versions.setdefault(param, [])
            self.param_to_api_versions[param].append(self._mod_to_api_version[api_version])

        self._api_version_to_mixin_operation_metadata[api_version] = mixin_operation_metadata
