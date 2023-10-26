# coding=utf-8


from typing import Any, TYPE_CHECKING, Union

from corehttp.credentials import ServiceKeyCredential
from corehttp.runtime import policies

from .._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.credentials import AsyncTokenCredential


class UnionClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for UnionClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Is either a
     ServiceKeyCredential type or a TokenCredential type. Required.
    :type credential: ~corehttp.credentials.ServiceKeyCredential or
     ~corehttp.credentials.AsyncTokenCredential
    """

    def __init__(self, credential: Union[ServiceKeyCredential, "AsyncTokenCredential"], **kwargs: Any) -> None:
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.credential = credential
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://security.microsoft.com/.default"])
        kwargs.setdefault("sdk_moniker", "authentication-union/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _infer_policy(self, **kwargs):
        if isinstance(self.credential, ServiceKeyCredential):
            return policies.ServiceKeyCredentialPolicy(self.credential, "x-ms-api-key", **kwargs)
        if hasattr(self.credential, "get_token"):
            return policies.AsyncBearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
        raise TypeError(f"Unsupported credential: {self.credential}")

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = self._infer_policy(**kwargs)
