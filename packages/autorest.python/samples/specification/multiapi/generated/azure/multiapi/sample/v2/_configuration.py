# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.mgmt.core.policies import ARMChallengeAuthenticationPolicy, ARMHttpLoggingPolicy

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

VERSION = "unknown"


class MultiapiServiceClientConfiguration:  # pylint: disable=too-many-instance-attributes,name-too-long
    """Configuration for MultiapiServiceClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword api_version: Api Version. Default value is "2.0.0". Note that overriding this default
     value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(self, credential: "TokenCredential", **kwargs: Any) -> None:
        api_version: str = kwargs.pop("api_version", "2.0.0")

        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.credential = credential
        self.api_version = api_version
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://management.azure.com/.default"])
        kwargs.setdefault("sdk_moniker", "multiapi-sample/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or ARMHttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = ARMChallengeAuthenticationPolicy(
                self.credential, *self.credential_scopes, **kwargs
            )
