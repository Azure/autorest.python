# coding=utf-8


from typing import Any, TYPE_CHECKING

from corehttp.runtime import policies

from .._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.credentials import AsyncTokenCredential


class OAuth2ClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for OAuth2Client.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~corehttp.credentials.AsyncTokenCredential
    """

    def __init__(self, credential: "AsyncTokenCredential", **kwargs: Any) -> None:
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.credential = credential
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://security.microsoft.com/.default"])
        kwargs.setdefault("sdk_moniker", "authentication-oauth2/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.AsyncBearerTokenCredentialPolicy(
                self.credential, *self.credential_scopes, **kwargs
            )
