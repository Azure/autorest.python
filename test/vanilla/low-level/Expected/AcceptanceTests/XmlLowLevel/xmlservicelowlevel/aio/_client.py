# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .._serialization import Deserializer, Serializer
from ._configuration import AutoRestSwaggerBATXMLServiceConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class AutoRestSwaggerBATXMLService:  # pylint: disable=client-accepts-api-version-keyword
    """Test Infrastructure for AutoRest Swagger BAT.

    :keyword endpoint: Service URL. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(self, *, endpoint: str = "http://localhost:3000", **kwargs: Any) -> None:
        self._config = AutoRestSwaggerBATXMLServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `xmlservicelowlevel.rest`.
        Use these helper methods to create the request you pass to this method.

        >>> from xmlservicelowlevel.rest import xml
        >>> request = xml.build_get_complex_type_ref_no_meta_request(**kwargs)
        <HttpRequest [GET], url: '/xml/complex-type-ref-no-meta'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestSwaggerBATXMLService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
