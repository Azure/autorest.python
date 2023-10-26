# coding=utf-8


from typing import Any

from corehttp.credentials import ServiceKeyCredential
from corehttp.runtime import policies

from ._version import VERSION


class CustomClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for CustomClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~corehttp.credentials.ServiceKeyCredential
    """

    def __init__(self, credential: ServiceKeyCredential, **kwargs: Any) -> None:
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.credential = credential
        kwargs.setdefault("sdk_moniker", "authentication-http-custom/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.ServiceKeyCredentialPolicy(
                self.credential, "Authorization", prefix="SharedAccessKey", **kwargs
            )
