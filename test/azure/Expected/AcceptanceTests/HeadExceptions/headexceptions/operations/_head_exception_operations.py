# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMError


class HeadExceptionOperations(object):
    """HeadExceptionOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def head200(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 200 status code if successful.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.head200.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        if cls:
          return cls(response, None, {})

        return 200 <= response.status_code <= 299
    head200.metadata = {'url': '/http/success/200'}

    @distributed_trace
    def head204(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 204 status code if successful.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.head204.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        if cls:
          return cls(response, None, {})

        return 200 <= response.status_code <= 299
    head204.metadata = {'url': '/http/success/204'}

    @distributed_trace
    def head404(
        self,
        cls=None,  # type: Optional[Callable[[HttpResponse, None, Dict[str, Any]], Any]]
        **kwargs  # type: **Any
    ):
        # type: (...) -> None
        """Return 404 status code if successful.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.mgmt.core.ARMError
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.head404.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        if cls:
          return cls(response, None, {})

        return 200 <= response.status_code <= 299
    head404.metadata = {'url': '/http/success/404'}
