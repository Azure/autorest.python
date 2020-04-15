# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._auto_rest_swagger_bat_file_service import AutoRestSwaggerBATFileService
from ._version import VERSION

__version__ = VERSION
__all__ = ['AutoRestSwaggerBATFileService']

try:
    from ._patch import patch_sdk
    patch_sdk()
except ImportError:
    pass
