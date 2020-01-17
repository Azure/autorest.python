# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from .._version import VERSION


class AutoRestHeadExceptionTestServiceConfiguration(Configuration):
    """Configuration for AutoRestHeadExceptionTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    """

    def __init__(self, credential: "TokenCredential", **kwargs) -> None:
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        super(AutoRestHeadExceptionTestServiceConfiguration, self).__init__(**kwargs)

        self.credential = credential
        self.credential_scopes = ['https://management.azure.com/.default']
        self._configure(**kwargs)
        self.user_agent_policy.add_user_agent('azsdk-python-autorestheadexceptiontestservice/{}'.format(VERSION))

    def _configure(self, **kwargs) -> None:
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.AsyncBearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
