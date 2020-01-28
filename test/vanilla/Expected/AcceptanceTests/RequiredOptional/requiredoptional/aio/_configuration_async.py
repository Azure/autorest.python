# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from .._version import VERSION


class AutoRestRequiredOptionalTestServiceConfiguration(Configuration):
    """Configuration for AutoRestRequiredOptionalTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param required_global_path: number of items to skip
    :type required_global_path: str
    :param required_global_query: number of items to skip
    :type required_global_query: str
    :param optional_global_query: number of items to skip
    :type optional_global_query: int
    """

    def __init__(
        self,
        required_global_path: str,
        required_global_query: str,
        optional_global_query: Optional[int] = None,
        **kwargs: Any
    ) -> None:
        if required_global_path is None:
            raise ValueError("Parameter 'required_global_path' must not be None.")
        if required_global_query is None:
            raise ValueError("Parameter 'required_global_query' must not be None.")
        super(AutoRestRequiredOptionalTestServiceConfiguration, self).__init__(**kwargs)

        self.required_global_path = required_global_path
        self.required_global_query = required_global_query
        self.optional_global_query = optional_global_query
        self._configure(**kwargs)
        self.user_agent_policy.add_user_agent('azsdk-python-autorestrequiredoptionaltestservice/{}'.format(VERSION))

    def _configure(
        self,
        **kwargs: Any
    ) -> None:
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
