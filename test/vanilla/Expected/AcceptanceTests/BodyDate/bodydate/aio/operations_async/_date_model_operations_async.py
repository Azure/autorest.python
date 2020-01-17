# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class DateOperations:
    """DateOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodydate.models
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
    async def get_null(self, *, cls=None, **kwargs) -> datetime.date:

        """Get null date value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~bodydate.models.ErrorException:
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

        deserialized = self._deserialize('date', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/date/null'}

    @distributed_trace_async
    async def get_invalid_date(self, *, cls=None, **kwargs) -> datetime.date:

        """Get invalid date value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~bodydate.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_invalid_date.metadata['url']

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

        deserialized = self._deserialize('date', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_invalid_date.metadata = {'url': '/date/invaliddate'}

    @distributed_trace_async
    async def get_overflow_date(self, *, cls=None, **kwargs) -> datetime.date:

        """Get overflow date value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~bodydate.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_overflow_date.metadata['url']

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

        deserialized = self._deserialize('date', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_overflow_date.metadata = {'url': '/date/overflowdate'}

    @distributed_trace_async
    async def get_underflow_date(self, *, cls=None, **kwargs) -> datetime.date:

        """Get underflow date value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~bodydate.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_underflow_date.metadata['url']

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

        deserialized = self._deserialize('date', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_underflow_date.metadata = {'url': '/date/underflowdate'}

    @distributed_trace_async
    async def put_max_date(self, date_body: datetime.date, *, cls=None, **kwargs) -> None:

        """Put max date value 9999-12-31.

        FIXME: add operation.summary

        :param date_body: 
        :type date_body: ~datetime.date
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodydate.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_max_date.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(date_body, 'date')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_max_date.metadata = {'url': '/date/max'}

    @distributed_trace_async
    async def get_max_date(self, *, cls=None, **kwargs) -> datetime.date:

        """Get max date value 9999-12-31.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~bodydate.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_max_date.metadata['url']

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

        deserialized = self._deserialize('date', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_max_date.metadata = {'url': '/date/max'}

    @distributed_trace_async
    async def put_min_date(self, date_body: datetime.date, *, cls=None, **kwargs) -> None:

        """Put min date value 0000-01-01.

        FIXME: add operation.summary

        :param date_body: 
        :type date_body: ~datetime.date
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodydate.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_min_date.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(date_body, 'date')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_min_date.metadata = {'url': '/date/min'}

    @distributed_trace_async
    async def get_min_date(self, *, cls=None, **kwargs) -> datetime.date:

        """Get min date value 0000-01-01.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: ~datetime.date
        :raises: ~bodydate.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_min_date.metadata['url']

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

        deserialized = self._deserialize('date', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_min_date.metadata = {'url': '/date/min'}
