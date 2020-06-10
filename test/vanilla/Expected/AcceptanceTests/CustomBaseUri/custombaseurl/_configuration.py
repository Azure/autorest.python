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


class AutoRestParameterizedHostTestClientConfiguration(Configuration):
    """Configuration for AutoRestParameterizedHostTestClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param host: A string value that is used as a global part of the parameterized host.
    :type host: str
    """

    def __init__(
        self,
        host="host",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if host is None:
            raise ValueError("Parameter 'host' must not be None.")
        super(AutoRestParameterizedHostTestClientConfiguration, self).__init__(**kwargs)

        self.host = host
        kwargs.setdefault('sdk_moniker', 'autorestparameterizedhosttestclient/{}'.format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        kwargs.pop('sdk_moniker')
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
