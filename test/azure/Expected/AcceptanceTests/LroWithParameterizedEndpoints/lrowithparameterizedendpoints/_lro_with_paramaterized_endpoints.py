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

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any

from ._configuration import LROWithParamaterizedEndpointsConfiguration
from .operations import LROWithParamaterizedEndpointsOperationsMixin
from . import models


class LROWithParamaterizedEndpoints(LROWithParamaterizedEndpointsOperationsMixin):
    """Test Infrastructure for AutoRest.

    :param host: A string value that is used as a global part of the parameterized host. Pass in 'host:3000' to pass test.
    :type host: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        host="host",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = "http://{accountName}{host}"
        self._config = LROWithParamaterizedEndpointsConfiguration(host, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> LROWithParamaterizedEndpoints
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
