# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import LROsOperations
from ._operations import LRORetrysOperations
from ._operations import LROSADsOperations
from ._operations import LROsCustomHeaderOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import

__all__ = [
    "LROsOperations",
    "LRORetrysOperations",
    "LROSADsOperations",
    "LROsCustomHeaderOperations",
]
__all__.extend(_patch_all)
