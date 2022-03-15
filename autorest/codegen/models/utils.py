# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from enum import Enum

JSON_REGEXP = re.compile(r'^(application|text)/(.+\+)?json$')

AAD_TOKEN = "AADToken"
AZURE_KEY = "AzureKey"
class Credential(Enum):
    SCOPES = "credential_scopes"
    KEY_HEADER_NAME = "key_header_name"
    POLICY_TYPE = "policy_type"
