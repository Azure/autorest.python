# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class DurationOperations:
    """DurationOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyduration.models
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
    async def get_null(self, cls=None, **kwargs):
        """Get null duration value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: timedelta or the result of cls(response)
        :rtype: ~datetime.timedelta
        :raises: ~bodyduration.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('duration', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/duration/null'}

    @distributed_trace_async
    async def put_positive_duration(self, duration_body, cls=None, **kwargs):
        """Put a positive duration value.

        FIXME: add operation.summary

        :param duration_body: 
        :type duration_body: ~datetime.timedelta
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodyduration.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_positive_duration.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(duration_body, 'duration')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_positive_duration.metadata = {'url': '/duration/positiveduration'}

    @distributed_trace_async
    async def get_positive_duration(self, cls=None, **kwargs):
        """Get a positive duration value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: timedelta or the result of cls(response)
        :rtype: ~datetime.timedelta
        :raises: ~bodyduration.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_positive_duration.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('duration', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_positive_duration.metadata = {'url': '/duration/positiveduration'}

    @distributed_trace_async
    async def get_invalid(self, cls=None, **kwargs):
        """Get an invalid duration value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: timedelta or the result of cls(response)
        :rtype: ~datetime.timedelta
        :raises: ~bodyduration.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_invalid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('duration', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_invalid.metadata = {'url': '/duration/invalid'}
