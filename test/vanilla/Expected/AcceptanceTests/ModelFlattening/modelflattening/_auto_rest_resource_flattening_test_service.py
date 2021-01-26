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
from ._configuration import AutoRestResourceFlatteningTestServiceConfiguration
from .operations import AutoRestResourceFlatteningTestServiceOperationsMixin

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.pipeline import PipelineResponse
    from azure.core.pipeline.transport import HttpRequest


class AutoRestResourceFlatteningTestService(AutoRestResourceFlatteningTestServiceOperationsMixin):
    """Resource Flattening for AutoRest.

    :param str base_url: Service URL
    """

    def __init__(
        self,
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestResourceFlatteningTestServiceConfiguration(**kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

    def invoke(self, request, **kwargs):
        # type: (HttpRequest, Any) -> PipelineResponse
        return self._client._pipeline.run(request, stream=False, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestResourceFlatteningTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
