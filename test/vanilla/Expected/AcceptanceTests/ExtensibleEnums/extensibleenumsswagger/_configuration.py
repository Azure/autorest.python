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

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from .version import VERSION


class PetStoreIncConfiguration(Configuration):
    """Configuration for PetStoreInc
    Note that all parameters used to create this instance are saved as instance
    attributes.

    """

    def __init__(self, **kwargs):


        super(PetStoreIncConfiguration, self).__init__(**kwargs)
        self._configure(**kwargs)

        self.user_agent_policy.add_user_agent('azsdk-python-petstoreinc/{}'.format(VERSION))
        self.generate_client_request_id = True

    def _configure(self, **kwargs):
        self.user_agent_policy = kwargs.get('user_agent_policy', policies.UserAgentPolicy(**kwargs))
        self.headers_policy = kwargs.get('headers_policy', policies.HeadersPolicy(**kwargs))
        self.proxy_policy = kwargs.get('proxy_policy', policies.ProxyPolicy(**kwargs))
        self.logging_policy = kwargs.get('logging_policy', policies.NetworkTraceLoggingPolicy(**kwargs))
        self.retry_policy = kwargs.get('retry_policy', policies.AsyncRetryPolicy(**kwargs))
        self.custom_hook_policy = kwargs.get('custom_hook_policy', policies.CustomHookPolicy(**kwargs))
        self.redirect_policy = kwargs.get('redirect_policy', policies.AsyncRedirectPolicy(**kwargs))
