# coding=utf-8

from typing import Any, TYPE_CHECKING, Union

from corehttp.credentials import ServiceKeyCredential
from corehttp.runtime import policies

from .._version import VERSION

if TYPE_CHECKING:
    from corehttp.credentials import AsyncTokenCredential


class UnionClientConfiguration:
    """Configuration for UnionClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential used to authenticate requests to the service. Is either a key
     credential type or a token credential type. Required.
    :type credential: ~corehttp.credentials.ServiceKeyCredential or
     ~corehttp.credentials.AsyncTokenCredential
    :param endpoint: Service host. Default value is "http://localhost:3000".
    :type endpoint: str
    """

    def __init__(
        self,
        credential: Union[ServiceKeyCredential, "AsyncTokenCredential"],
        endpoint: str = "http://localhost:3000",
        **kwargs: Any,
    ) -> None:
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.credential = credential
        self.endpoint = endpoint
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://security.microsoft.com/.default"])
        kwargs.setdefault("sdk_moniker", "authentication-union/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _infer_policy(self, **kwargs):
        if isinstance(self.credential, ServiceKeyCredential):
            return policies.ServiceKeyCredentialPolicy(self.credential, "x-ms-api-key", **kwargs)
        if hasattr(self.credential, "get_token"):
            return policies.AsyncBearerTokenCredentialPolicy(
                self.credential,
                *self.credential_scopes,
                auth_flows=[
                    {
                        "authorizationUrl": "https://login.microsoftonline.com/common/oauth2/authorize",
                        "scopes": [{"value": "https://security.microsoft.com/.default"}],
                        "type": "implicit",
                    }
                ],
                **kwargs,
            )
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
