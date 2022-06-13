# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import AutoRestParameterizedCustomHostTestClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import PathsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class AutoRestParameterizedCustomHostTestClient:  # pylint: disable=client-accepts-api-version-keyword
    """Test Infrastructure for AutoRest.

    :ivar paths: PathsOperations operations
    :vartype paths: custombaseurlmoreoptionsversiontolerant.operations.PathsOperations
    :param subscription_id: The subscription id with value 'test12'. Required.
    :type subscription_id: str
    :param dns_suffix: A string value that is used as a global part of the parameterized host.
     Default value 'host'. Default value is "host".
    :type dns_suffix: str
    """

    def __init__(self, subscription_id: str, dns_suffix: str = "host", **kwargs: Any) -> None:
        _endpoint = "{vault}{secret}{dnsSuffix}"
        self._config = AutoRestParameterizedCustomHostTestClientConfiguration(
            subscription_id=subscription_id, dns_suffix=dns_suffix, **kwargs
        )
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.paths = PathsOperations(self._client, self._config, self._serialize, self._deserialize)

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
        path_format_arguments = {
            "dnsSuffix": self._serialize.url(
                "self._config.dns_suffix", self._config.dns_suffix, "str", skip_quote=True
            ),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

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
