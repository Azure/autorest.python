# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from ._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any


class AutoRestParameterizedCustomHostTestClientConfiguration(
    Configuration
):  # pylint: disable=too-many-instance-attributes
    """Configuration for AutoRestParameterizedCustomHostTestClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: The subscription id with value 'test12'.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the parameterized host.
     Default value 'host'.
    :type dns_suffix: str
    """

    def __init__(
        self,
        subscription_id,  # type: str
        dns_suffix="host",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        super(AutoRestParameterizedCustomHostTestClientConfiguration, self).__init__(**kwargs)
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if dns_suffix is None:
            raise ValueError("Parameter 'dns_suffix' must not be None.")

        self.subscription_id = subscription_id
        self.dns_suffix = dns_suffix
        kwargs.setdefault("sdk_moniker", "autorestparameterizedcustomhosttestclient/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
