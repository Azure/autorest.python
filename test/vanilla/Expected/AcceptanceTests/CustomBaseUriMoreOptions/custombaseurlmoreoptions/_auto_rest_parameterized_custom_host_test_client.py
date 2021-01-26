# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

from . import models
from ._configuration import AutoRestParameterizedCustomHostTestClientConfiguration
from .operations import PathsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

    from azure.core.pipeline import PipelineResponse
    from azure.core.pipeline.transport import HttpRequest

from ._configuration import AutoRestParameterizedCustomHostTestClientConfiguration
from .operations import PathsOperations
from . import models


class AutoRestParameterizedCustomHostTestClient(object):
    """Test Infrastructure for AutoRest.

    :ivar paths: PathsOperations operations
    :vartype paths: custombaseurlmoreoptions.operations.PathsOperations
    :param subscription_id: The subscription id with value 'test12'.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the parameterized host. Default value 'host'.
    :type dns_suffix: str
    """

    def __init__(
        self,
        subscription_id,  # type: str
        dns_suffix="host",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = "{vault}{secret}{dnsSuffix}"
        self._config = AutoRestParameterizedCustomHostTestClientConfiguration(subscription_id, dns_suffix, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(self._client, self._config, self._serialize, self._deserialize)

    def invoke(self, request, **kwargs):
        # type: (HttpRequest, Any) -> PipelineResponse
        path_format_arguments = {
            "subscriptionId": self._serialize.url("self._config.subscription_id", self._config.subscription_id, "str"),
            "dnsSuffix": self._serialize.url(
                "self._config.dns_suffix", self._config.dns_suffix, "str", skip_quote=True
            ),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)
        return self._client._pipeline.run(request, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestParameterizedCustomHostTestClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
