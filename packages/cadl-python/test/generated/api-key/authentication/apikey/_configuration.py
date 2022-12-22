# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Union

from azure.core.configuration import Configuration
from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline import policies

from ._version import VERSION


class ApiKeyClientConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for ApiKeyClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Is either a Key type
     or a Key type. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential or
     ~azure.core.credentials.AzureKeyCredential
    """

    def __init__(self, credential: Union[AzureKeyCredential, AzureKeyCredential], **kwargs: Any) -> None:
        super(ApiKeyClientConfiguration, self).__init__(**kwargs)
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")

        self.credential = credential
        kwargs.setdefault("sdk_moniker", "apikeyclient/{}".format(VERSION))
        self._configure(**kwargs)

    def _infer_policy(self, **kwargs):
        if isinstance(self.credential, AzureKeyCredential):
            return policies.AzureKeyCredentialPolicy(self.credential, "x-ms-api-key", **kwargs)
        if isinstance(self.credential, AzureKeyCredential):
            return policies.AzureKeyCredentialPolicy(self.credential, "x-ms-second-api-key", **kwargs)
        else:
            raise TypeError(f"Unsupported credential: {self.credential}")

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = self._infer_policy(**kwargs)
