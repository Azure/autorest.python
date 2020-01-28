# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class HeaderOperations:
    """HeaderOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def custom_named_request_id(
        self,
        foo_client_request_id: str,
        *,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

        FIXME: add operation.summary

        :param foo_client_request_id: The fooRequestId
        :type foo_client_request_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.custom_named_request_id.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['foo-client-request-id'] = self._serialize.header("foo_client_request_id", foo_client_request_id, 'str')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        response_headers = {}
        response_headers['foo-request-id']=self._deserialize('str', response.headers.get('foo-request-id'))

        if cls:
          return cls(response, None, response_headers)

    custom_named_request_id.metadata = {'url': '/azurespecials/customNamedRequestId'}

    @distributed_trace_async
    async def custom_named_request_id_param_grouping(
        self,
        foo_client_request_id: str,
        *,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request, via a parameter group.

        FIXME: add operation.summary

        :param foo_client_request_id: The fooRequestId
        :type foo_client_request_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.custom_named_request_id_param_grouping.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['foo-client-request-id'] = self._serialize.header("foo_client_request_id", foo_client_request_id, 'str')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        response_headers = {}
        response_headers['foo-request-id']=self._deserialize('str', response.headers.get('foo-request-id'))

        if cls:
          return cls(response, None, response_headers)

    custom_named_request_id_param_grouping.metadata = {'url': '/azurespecials/customNamedRequestIdParamGrouping'}

    @distributed_trace_async
    async def custom_named_request_id_head(
        self,
        foo_client_request_id: str,
        *,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in the header of the request.

        FIXME: add operation.summary

        :param foo_client_request_id: The fooRequestId
        :type foo_client_request_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.custom_named_request_id_head.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['foo-client-request-id'] = self._serialize.header("foo_client_request_id", foo_client_request_id, 'str')


        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 404]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        response_headers = {}
        if response.status_code == 200:
            response_headers['foo-request-id']=self._deserialize('str', response.headers.get('foo-request-id'))

        if cls:
          return cls(response, None, response_headers)

        return 200 <= response.status_code <= 299
    custom_named_request_id_head.metadata = {'url': '/azurespecials/customNamedRequestIdHead'}
