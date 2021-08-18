# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

from ._configuration import AutoRestRequiredOptionalTestServiceConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional

    from azure.core.rest import HttpRequest, HttpResponse


class AutoRestRequiredOptionalTestService(object):
    """Test Infrastructure for AutoRest.

    :param required_global_path: number of items to skip.
    :type required_global_path: str
    :param required_global_query: number of items to skip.
    :type required_global_query: str
    :param optional_global_query: number of items to skip.
    :type optional_global_query: int
    :keyword endpoint: Service URL
    :paramtype endpoint: str
    """

    def __init__(
        self,
        required_global_path,  # type: str
        required_global_query,  # type: str
        optional_global_query=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        endpoint = kwargs.pop("endpoint", "http://localhost:3000")  # type: str

        self._config = AutoRestRequiredOptionalTestServiceConfiguration(
            required_global_path, required_global_query, optional_global_query, **kwargs
        )
        self._client = PipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False

    def send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `requiredoptionallowlevel.rest`.
        Use these helper methods to create the request you pass to this method.

        >>> from requiredoptionallowlevel.rest import implicit
        >>> request = implicit.build_get_required_path_request(path_parameter, **kwargs)
        <HttpRequest [GET], url: '/reqopt/implicit/required/path/{pathParameter}'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestRequiredOptionalTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
