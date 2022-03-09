# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._polling_paging_example import PollingPagingExample
from ._version import VERSION

__version__ = VERSION

try:
    from ._patch import __all__ as _patch_all
    from ._patch import *  # pylint: disable=unused-wildcard-import
except ImportError:
    _patch_all = []
from ._patch import patch_sdk as _patch_sdk
__all__ = ['PollingPagingExample']
__all__.extend([p for p in _patch_all if p not in __all__])

# `._patch.py` is used for handwritten extensions to the generated code
# Example: https://github.com/Azure/azure-sdk-for-python/blob/main/doc/dev/customize_code/how-to-patch-sdk-code.md
_patch_sdk()
