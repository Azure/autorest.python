# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._auto_rest_complex_test_service import AutoRestComplexTestService
from ._version import VERSION

__version__ = VERSION

from ._patch import __all__ as _patch_all
from ._patch import *

__all__ = ["AutoRestComplexTestService"]
__all__.extend(_patch_all)

# `._patch.py` is used for handwritten extensions to the generated code
# Example: https://github.com/Azure/azure-sdk-for-python/blob/main/doc/dev/customize_code/how-to-patch-sdk-code.md
from ._patch import patch_sdk

patch_sdk()
