# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AutoRestHeadTestServiceConfiguration
from .operations import HttpSuccessOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline import PipelineResponse
    from azure.core.pipeline.transport import HttpRequest


class AutoRestHeadTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar http_success: HttpSuccessOperations operations
    :vartype http_success: azure.mgmt.sample.operations.HttpSuccessOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestHeadTestServiceConfiguration(credential, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {}  # type: Dict[str, Any]
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.http_success = HttpSuccessOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def invoke(self, request, **kwargs):
        # type: (HttpRequest, Any) -> PipelineResponse
        return self._client._pipeline.run(request, stream=False, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestHeadTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
