# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from .._version import VERSION

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports


class AutoRestValidationTestConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for AutoRestValidationTest.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: Subscription ID. Required.
    :type subscription_id: str
    :keyword api_version: Api Version. Default value is "1.0.0". Note that overriding this default
     value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, subscription_id: str, **kwargs: Any) -> None:
        super(AutoRestValidationTestConfiguration, self).__init__(**kwargs)
        api_version: str = kwargs.pop("api_version", "1.0.0")

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")

        self.subscription_id = subscription_id
        self.api_version = api_version
        kwargs.setdefault("sdk_moniker", "autorestvalidationtest/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
