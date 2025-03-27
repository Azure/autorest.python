# coding=utf-8

from typing import Any, TYPE_CHECKING, Union

from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline import policies

from ._version import VERSION

if TYPE_CHECKING:
    from azure.core.credentials import TokenCredential


class UnionClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for UnionClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential used to authenticate requests to the service. Is either a key
     credential type or a token credential type. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential or
     ~azure.core.credentials.TokenCredential
    :param endpoint: Service host. Default value is "http://localhost:3000".
    :type endpoint: str
    """

    def __init__(
        self,
        credential: Union[AzureKeyCredential, "TokenCredential"],
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
        if isinstance(self.credential, AzureKeyCredential):
            return policies.AzureKeyCredentialPolicy(self.credential, "x-ms-api-key", **kwargs)
        if hasattr(self.credential, "get_token"):
            return policies.BearerTokenCredentialPolicy(self.credential, *self.credential_scopes, **kwargs)
        raise TypeError(f"Unsupported credential: {self.credential}")

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
        if self.credential and not self.authentication_policy:
            self.authentication_policy = self._infer_policy(**kwargs)
