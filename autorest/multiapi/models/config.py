# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict

class Config:
    def __init__(self, default_version_metadata: Dict[str, Any]):
        self.credential = default_version_metadata["config"]["credential"]
        self.credential_scopes = default_version_metadata["config"]["credential_scopes"]
        self.credential_default_policy_type = default_version_metadata["config"]["credential_default_policy_type"]
        self.credential_default_policy_type_has_async_version = (
            default_version_metadata["config"]["credential_default_policy_type_has_async_version"]
        )
        self.credential_key_header_name = default_version_metadata["config"]["credential_key_header_name"]
