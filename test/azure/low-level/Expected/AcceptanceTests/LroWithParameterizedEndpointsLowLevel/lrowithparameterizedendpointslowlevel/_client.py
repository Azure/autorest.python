# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from msrest import Deserializer, Serializer

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import LROWithParamaterizedEndpointsConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class LROWithParamaterizedEndpoints:  # pylint: disable=client-accepts-api-version-keyword
    """Test Infrastructure for AutoRest.

    :param host: A string value that is used as a global part of the parameterized host. Pass in
     'host:3000' to pass test. Default value is "host".
    :type host: str
    """

    def __init__(self, host: str = "host", **kwargs: Any) -> None:
        _endpoint = "http://{accountName}{host}"
        self._config = LROWithParamaterizedEndpointsConfiguration(host=host, **kwargs)
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `lrowithparameterizedendpointslowlevel.rest`.
        Use these helper methods to create the request you pass to this method.

        >>> from lrowithparameterizedendpointslowlevel.rest import build_poll_with_parameterized_endpoints_request
        >>> request = build_poll_with_parameterized_endpoints_request(**kwargs)
        <HttpRequest [POST], url: '/lroParameterizedEndpoints'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "host": self._serialize.url("self._config.host", self._config.host, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

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
