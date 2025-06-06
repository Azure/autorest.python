# coding=utf-8

from typing import Any

from corehttp.runtime import policies

from ._version import VERSION


class MultipleClientConfiguration:
    """Configuration for MultipleClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Pass in `http://localhost:3000 <http://localhost:3000>`_ for endpoint.
     Required.
    :type endpoint: str
    :keyword api_version: Pass in v1.0 for API version. Known values are "v1.0" and None. Default
     value is "v1.0". Note that overriding this default value may result in unsupported behavior.
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
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
