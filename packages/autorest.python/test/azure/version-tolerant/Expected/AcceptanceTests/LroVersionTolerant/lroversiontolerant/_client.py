# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from ._configuration import AutoRestLongRunningOperationTestServiceConfiguration
from ._serialization import Deserializer, Serializer
from .operations import LRORetrysOperations, LROSADsOperations, LROsCustomHeaderOperations, LROsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class AutoRestLongRunningOperationTestService:  # pylint: disable=client-accepts-api-version-keyword
    """Long-running Operation for AutoRest.

    :ivar lros: LROsOperations operations
    :vartype lros: lroversiontolerant.operations.LROsOperations
    :ivar lro_retrys: LRORetrysOperations operations
    :vartype lro_retrys: lroversiontolerant.operations.LRORetrysOperations
    :ivar lrosads: LROSADsOperations operations
    :vartype lrosads: lroversiontolerant.operations.LROSADsOperations
    :ivar lr_os_custom_header: LROsCustomHeaderOperations operations
    :vartype lr_os_custom_header: lroversiontolerant.operations.LROsCustomHeaderOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :keyword endpoint: Service URL. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self, credential: "TokenCredential", *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = AutoRestLongRunningOperationTestServiceConfiguration(credential=credential, **kwargs)
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.lros = LROsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.lro_retrys = LRORetrysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.lrosads = LROSADsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.lr_os_custom_header = LROsCustomHeaderOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "AutoRestLongRunningOperationTestService":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
