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

from msrest.serialization import Model


class CustomParameterGroup(Model):
    """Additional parameters for
    get_multiple_pages_fragment_with_grouping_next_link operation.

    :param api_version: Sets the api version to use.
    :type api_version: str
    :param tenant: Sets the tenant to use.
    :type tenant: str
    """

    _validation = {
        'api_version': {'required': True},
        'tenant': {'required': True},
    }

    def __init__(self, api_version, tenant):
        super(Model, self).__init__()
        self.api_version = api_version
        self.tenant = tenant
