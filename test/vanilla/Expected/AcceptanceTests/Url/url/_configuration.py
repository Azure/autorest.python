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

from msrest import Configuration

from .version import VERSION


class AutoRestUrlTestServiceConfiguration(Configuration):
    """Configuration for AutoRestUrlTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param global_string_path: A string value 'globalItemStringPath' that
     appears in the path
    :type global_string_path: str
    :param global_string_query: should contain value null
    :type global_string_query: str
    :param str base_url: Service URL
    """

    def __init__(
            self, global_string_path, global_string_query=None, base_url=None):

        if global_string_path is None:
            raise ValueError("Parameter 'global_string_path' must not be None.")
        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestUrlTestServiceConfiguration, self).__init__(base_url)

        # Starting Autorest.Python 4.0.64, make connection pool activated by default
        self.keep_alive = True

        self.add_user_agent('autoresturltestservice/{}'.format(VERSION))

        self.global_string_path = global_string_path
        self.global_string_query = global_string_query
