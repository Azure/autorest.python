# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import XMsClientRequestIdOperations
from ._operations import SubscriptionInCredentialsOperations
from ._operations import SubscriptionInMethodOperations
from ._operations import ApiVersionDefaultOperations
from ._operations import ApiVersionLocalOperations
from ._operations import SkipUrlEncodingOperations
from ._operations import OdataOperations
from ._operations import HeaderOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "XMsClientRequestIdOperations",
    "SubscriptionInCredentialsOperations",
    "SubscriptionInMethodOperations",
    "ApiVersionDefaultOperations",
    "ApiVersionLocalOperations",
    "SkipUrlEncodingOperations",
    "OdataOperations",
    "HeaderOperations",
]
__all__.extend(_patch_all)
_patch_sdk()
