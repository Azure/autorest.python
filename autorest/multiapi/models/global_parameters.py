# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional
from .global_parameter import GlobalParameter
from .constant_global_parameter import ConstantGlobalParameter

class GlobalParameters:
    def __init__(self, global_parameters_metadata: Dict[str, Any], service_client_base_url: Optional[str]):
        self.call = global_parameters_metadata["call"]
        self.global_parameters_metadata = global_parameters_metadata
        self.service_client_base_url = service_client_base_url

    @property
    def service_client_specific_global_parameters(self) -> List[GlobalParameter]:
        """Return global params specific to multiapi service client + config
        api_version, base_url (re-adding it in specific are), and profile
        """
        api_version_param = GlobalParameter(
            name="api_version",
            global_parameter_metadata_sync={
                "signature": "api_version=None, # type: Optional[str]",
                "description": "API version to use if no profile is provided, or if missing in profile.",
                "docstring_type": "str",
                "required": False
            },
            global_parameter_metadata_async={
                "signature": "api_version: Optional[str] = None,",
                "description": "API version to use if no profile is provided, or if missing in profile.",
                "docstring_type": "str",
                "required": False
            },
        )
        base_url_param = None
        if self.service_client_base_url:
            base_url_param = GlobalParameter(
                name="base_url",
                global_parameter_metadata_sync={
                    "signature": "base_url=None, # type: Optional[str]",
                    "description": "Service URL",
                    "docstring_type": "str",
                    "required": False
                },
                global_parameter_metadata_async={
                    "signature": "base_url: Optional[str] = None,",
                    "description": "Service URL",
                    "docstring_type": "str",
                    "required": False
                },
            )
        profile_param = GlobalParameter(
            name="profile",
            global_parameter_metadata_sync={
                "signature": "profile=KnownProfiles.default, # type: KnownProfiles",
                "description": "A profile definition, from KnownProfiles to dict.",
                "docstring_type": "azure.profiles.KnownProfiles",
                "required": False
            },
            global_parameter_metadata_async={
                "signature": "profile: KnownProfiles = KnownProfiles.default,",
                "description": "A profile definition, from KnownProfiles to dict.",
                "docstring_type": "azure.profiles.KnownProfiles",
                "required": False
            },
        )
        # return non-None members
        return list(filter(None.__ne__, [api_version_param, base_url_param, profile_param]))

    @property
    def parameters(self) -> List[GlobalParameter]:
        global_parameters_metadata_sync = self.global_parameters_metadata["sync"]
        global_parameters_metadata_async = self.global_parameters_metadata["async"]

        global_parameters = [
            GlobalParameter(
                name=parameter_name,
                global_parameter_metadata_sync=gp_sync,
                global_parameter_metadata_async=global_parameters_metadata_async[parameter_name]
            )
            for parameter_name, gp_sync in global_parameters_metadata_sync.items()
        ]
        return global_parameters

    @property
    def constant_parameters(self) -> List[ConstantGlobalParameter]:
        return [
            ConstantGlobalParameter(constant_name, constant_value)
            for constant_name, constant_value in self.global_parameters_metadata["constant"].items()
        ]
