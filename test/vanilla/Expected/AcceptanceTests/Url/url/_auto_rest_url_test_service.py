# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AutoRestUrlTestServiceConfiguration
from .operations import PathsOperations
from .operations import QueriesOperations
from .operations import PathItemsOperations
from . import models


class AutoRestUrlTestService(object):
    """Test Infrastructure for AutoRest

    :ivar paths: PathsOperations operations
    :vartype paths: url.operations.PathsOperations
    :ivar queries: QueriesOperations operations
    :vartype queries: url.operations.QueriesOperations
    :ivar path_items: PathItemsOperations operations
    :vartype path_items: url.operations.PathItemsOperations
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
    :type global_string_path: str
    :param global_string_query: should contain value null.
    :type global_string_query: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestUrlTestServiceConfiguration(global_string_path, global_string_query, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.queries = QueriesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.path_items = PathItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestUrlTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
