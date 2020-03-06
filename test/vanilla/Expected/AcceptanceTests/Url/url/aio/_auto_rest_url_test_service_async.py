# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AutoRestUrlTestServiceConfiguration
from .operations_async import PathsOperations
from .operations_async import QueriesOperations
from .operations_async import PathItemsOperations
from .. import models


class AutoRestUrlTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar paths: PathsOperations operations
    :vartype paths: url.aio.operations_async.PathsOperations
    :ivar queries: QueriesOperations operations
    :vartype queries: url.aio.operations_async.QueriesOperations
    :ivar path_items: PathItemsOperations operations
    :vartype path_items: url.aio.operations_async.PathItemsOperations
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param global_string_query: should contain value null.
    :type global_string_query: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        global_string_path,  # type: str
        global_string_query=None,  # type: Optional[str]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestUrlTestServiceConfiguration(global_string_path, global_string_query, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queries = QueriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.path_items = PathItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self):
        # type: () -> None
        await self._client.close()

    async def __aenter__(self):
        # type: () -> AutoRestUrlTestService
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details):
        # type: (Any) -> None
        await self._client.__aexit__(*exc_details)
