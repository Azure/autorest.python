# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AutoRestHeadExceptionTestServiceConfiguration
from .operations import HeadExceptionOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials_async import AsyncTokenCredential


class AutoRestHeadExceptionTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar head_exception: HeadExceptionOperations operations
    :vartype head_exception: headexceptions.aio.operations.HeadExceptionOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param str base_url: Service URL
    """

    def __init__(self, credential: "AsyncTokenCredential", base_url: Optional[str] = None, **kwargs: Any) -> None:
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestHeadExceptionTestServiceConfiguration(credential, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {}  # type: Dict[str, Any]
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.head_exception = HeadExceptionOperations(self._client, self._config, self._serialize, self._deserialize)

    async def invoke(self, request: HttpRequest, **kwargs: Any) -> PipelineResponse:
        return await self._client._pipeline.run(request, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestHeadExceptionTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
