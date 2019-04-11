# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.configuration import Configuration, ConnectionConfiguration
from azure.core.pipeline import policies, Pipeline
from azure.core.pipeline.transport import RequestsTransport

from .version import VERSION


class AutoRestParameterFlatteningConfiguration(Configuration):
    """Configuration for AutoRestParameterFlattening
    Note that all parameters used to create this instance are saved as instance
    attributes.

    """

    def __init__(self, **kwargs):


        super(AutoRestParameterFlatteningConfiguration, self).__init__(**kwargs)
        self.credentials = None
        self._configure(**kwargs)

        self.user_agent_policy.add_user_agent('autorestparameterflattening/{}'.format(VERSION))

    def _configure(self, **kwargs):
        self.connection = ConnectionConfiguration(**kwargs)
        self.user_agent_policy = policies.UserAgentPolicy(**kwargs)
        self.headers_policy = policies.HeadersPolicy(**kwargs)
        self.proxy_policy = policies.ProxyPolicy(**kwargs)
        self.logging_policy = policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = policies.RetryPolicy(**kwargs)
        self.redirect_policy = policies.RedirectPolicy(**kwargs)
        self.transport = kwargs.get('transport', RequestsTransport)

    def build_pipeline(self):
        transport = self.get_transport()
        pipeline_policies = [
            self.user_agent_policy,
            self.headers_policy,
            self.credentials,
            policies.ContentDecodePolicy(),
            self.redirect_policy,
            self.retry_policy,
            self.logging_policy,
        ]
        return Pipeline(transport, policies=pipeline_policies)
