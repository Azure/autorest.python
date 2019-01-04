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

from .auto_rest_http_infrastructure_test_service import AutoRestHttpInfrastructureTestService, AutoRestHttpInfrastructureTestServiceConfiguration
__all__ = ['AutoRestHttpInfrastructureTestService', 'AutoRestHttpInfrastructureTestServiceConfiguration']

try:
    from .auto_rest_http_infrastructure_test_service_async import AutoRestHttpInfrastructureTestServiceAsync
    __all__ += ['AutoRestHttpInfrastructureTestServiceAsync']
except (SyntaxError, ImportError):  # Python 2
    pass

from .version import VERSION

__version__ = VERSION

