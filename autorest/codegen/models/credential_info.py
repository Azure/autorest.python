# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum

class CredentialInfo(str, Enum):
    AAD_TOKEN = "AADToken"
    AZURE_KEY = "AzureKey"
    SCOPES = "credential_scopes"
    KEY_HEADER_NAME = "key_header_name"
    POLICY_TYPE = "policy_type"
