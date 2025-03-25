# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core.pipeline import policies

from ._version import VERSION


class AutoRestUrlTestServiceConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for AutoRestUrlTestService.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
     Required.
    :type global_string_path: str
    :param global_string_query: should contain value null. Default value is None.
    :type global_string_query: str
    """

    def __init__(self, global_string_path: str, global_string_query: Optional[str] = None, **kwargs: Any) -> None:
        if global_string_path is None:
            raise ValueError("Parameter 'global_string_path' must not be None.")

        self.global_string_path = global_string_path
        self.global_string_query = global_string_query
        kwargs.setdefault("sdk_moniker", "autoresturltestservice/{}".format(VERSION))
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
