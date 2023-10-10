# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Union

from azure.core.pipeline import policies

from . import models as _models
from ._version import VERSION


class ClientWithEnumConfiguration:  # pylint: disable=too-many-instance-attributes
    """Configuration for ClientWithEnum.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param x_ms_enum: Enum client parameter. "single" Required.
    :type x_ms_enum: str or ~clientenumversiontolerant.models.Enum0
    """

    def __init__(self, x_ms_enum: Union[str, _models.Enum0], **kwargs: Any) -> None:
        if x_ms_enum is None:
            raise ValueError("Parameter 'x_ms_enum' must not be None.")

        self.x_ms_enum = x_ms_enum
        kwargs.setdefault("sdk_moniker", "clientwithenum/{}".format(VERSION))
        self._configure(**kwargs)

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
