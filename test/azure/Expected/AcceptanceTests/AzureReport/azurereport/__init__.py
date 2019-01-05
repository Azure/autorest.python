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

from ._auto_rest_report_service_for_azure import AutoRestReportServiceForAzure, AutoRestReportServiceForAzureConfiguration
__all__ = ['AutoRestReportServiceForAzure', 'AutoRestReportServiceForAzureConfiguration']

try:
    from ._auto_rest_report_service_for_azure_async import AutoRestReportServiceForAzureAsync
    __all__ += ['AutoRestReportServiceForAzureAsync']
except (SyntaxError, ImportError):  # Python 2
    pass

from .version import VERSION

__version__ = VERSION

