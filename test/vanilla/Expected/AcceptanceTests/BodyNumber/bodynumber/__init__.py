# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from ._configuration import AutoRestNumberTestServiceConfiguration
from ._auto_rest_number_test_service import AutoRestNumberTestService
__all__ = ['AutoRestNumberTestService', 'AutoRestNumberTestServiceConfiguration']

try:
    from ._auto_rest_number_test_service_async import AutoRestNumberTestServiceAsync
    __all__ += ['AutoRestNumberTestServiceAsync']
except (SyntaxError, ImportError):  # Python 2
    pass

from .version import VERSION

__version__ = VERSION

