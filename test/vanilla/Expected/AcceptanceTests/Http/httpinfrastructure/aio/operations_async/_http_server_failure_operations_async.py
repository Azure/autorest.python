# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class HttpServerFailureOperations:
    """HttpServerFailureOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~httpinfrastructure.models
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
    async def head501(self, cls=None, **kwargs):
        """Return 501 status code - should be represented in the client as an error.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.head501.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    head501.metadata = {'url': '/http/failure/server/501'}

    @distributed_trace_async
    async def get501(self, cls=None, **kwargs):
        """Return 501 status code - should be represented in the client as an error.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get501.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    get501.metadata = {'url': '/http/failure/server/501'}

    @distributed_trace_async
    async def post505(self, cls=None, **kwargs):
        """Return 505 status code - should be represented in the client as an error.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.post505.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post505.metadata = {'url': '/http/failure/server/505'}

    @distributed_trace_async
    async def delete505(self, cls=None, **kwargs):
        """Return 505 status code - should be represented in the client as an error.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~httpinfrastructure.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        boolean_value = True

        # Construct URL
        url = self.delete505.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    delete505.metadata = {'url': '/http/failure/server/505'}

