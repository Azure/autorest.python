# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from ._version import VERSION


class AutoRestDateTestServiceConfiguration(Configuration):
    """Configuration for AutoRestDateTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.
    """

    def __init__(self[], **kwargs):
        # type: (**Any) -> None
        super(AutoRestDateTestServiceConfiguration, self).__init__(**kwargs)

        self._configure(**kwargs)
        self.user_agent_policy.add_user_agent('azsdk-python-autorestdatetestservice/{}'.format(VERSION))

    def _configure(self, **kwargs):
        # type: (**Any) -> None
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
