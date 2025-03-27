# coding=utf-8

from typing import Any

from azure.core.pipeline import policies

from .._version import VERSION


class FlattenPropertyClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for FlattenPropertyClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Service host. Default value is "http://localhost:3000".
    :type endpoint: str
    """

    def __init__(self, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:

        self.endpoint = endpoint
        kwargs.setdefault("sdk_moniker", "specs-azure-clientgenerator-core-flattenproperty/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.AsyncRedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
