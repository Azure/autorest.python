# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any

from azure.core.pipeline import policies

from ._version import VERSION


class MultipleClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for MultipleClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Pass in http://localhost:3000 for endpoint. Required.
    :type endpoint: str
    :keyword api_version: Pass in v1.0 for API version. Default value is "v1.0". Note that
     overriding this default value may result in unsupported behavior.
    :paramtype api_version: str or ~server.path.multiple.models.Versions
    """

    def __init__(self, endpoint: str, **kwargs: Any) -> None:
        api_version: str = kwargs.pop("api_version", "v1.0")

        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")

        self.endpoint = endpoint
        self.api_version = api_version
        kwargs.setdefault("sdk_moniker", "server-path-multiple/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
