# coding=utf-8

from typing import Any, Union

from azure.core.pipeline import policies

from .. import models as _models
from .._version import VERSION


class TypeChangedFromClientConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for TypeChangedFromClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param endpoint: Need to be set as '`http://localhost:3000 <http://localhost:3000>`_' in
     client. Required.
    :type endpoint: str
    :param version: Need to be set as 'v1' or 'v2' in client. Known values are: "v1" and "v2".
     Required.
    :type version: str or ~versioning.typechangedfrom.models.Versions
    """

    def __init__(self, endpoint: str, version: Union[str, _models.Versions], **kwargs: Any) -> None:
        if endpoint is None:
            raise ValueError("Parameter 'endpoint' must not be None.")
        if version is None:
            raise ValueError("Parameter 'version' must not be None.")

        self.endpoint = endpoint
        self.version = version
        kwargs.setdefault("sdk_moniker", "versioning-typechangedfrom/{}".format(VERSION))
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
