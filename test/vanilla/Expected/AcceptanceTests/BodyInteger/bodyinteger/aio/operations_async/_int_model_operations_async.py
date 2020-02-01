# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class IntOperations:
    """IntOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyinteger.models
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
    async def get_null(
        self,
        cls: ClsType[int] = None,
        **kwargs: Any
    ) -> int:
        """Get null Int value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: int or the result of cls(response)
        :rtype: int
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('int', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/int/null'}

    @distributed_trace_async
    async def get_invalid(
        self,
        cls: ClsType[int] = None,
        **kwargs: Any
    ) -> int:
        """Get invalid Int value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: int or the result of cls(response)
        :rtype: int
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_invalid.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('int', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_invalid.metadata = {'url': '/int/invalid'}

    @distributed_trace_async
    async def get_overflow_int32(
        self,
        cls: ClsType[int] = None,
        **kwargs: Any
    ) -> int:
        """Get overflow Int32 value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: int or the result of cls(response)
        :rtype: int
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_overflow_int32.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('int', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_overflow_int32.metadata = {'url': '/int/overflowint32'}

    @distributed_trace_async
    async def get_underflow_int32(
        self,
        cls: ClsType[int] = None,
        **kwargs: Any
    ) -> int:
        """Get underflow Int32 value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: int or the result of cls(response)
        :rtype: int
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_underflow_int32.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('int', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_underflow_int32.metadata = {'url': '/int/underflowint32'}

    @distributed_trace_async
    async def get_overflow_int64(
        self,
        cls: ClsType[int] = None,
        **kwargs: Any
    ) -> int:
        """Get overflow Int64 value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: long or the result of cls(response)
        :rtype: long
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_overflow_int64.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_overflow_int64.metadata = {'url': '/int/overflowint64'}

    @distributed_trace_async
    async def get_underflow_int64(
        self,
        cls: ClsType[int] = None,
        **kwargs: Any
    ) -> int:
        """Get underflow Int64 value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: long or the result of cls(response)
        :rtype: long
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_underflow_int64.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('long', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_underflow_int64.metadata = {'url': '/int/underflowint64'}

    @distributed_trace_async
    async def put_max32(
        self,
        int_body: int,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Put max int32 value.

        :param int_body:
        :type int_body: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.put_max32.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(int_body, 'int')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_max32.metadata = {'url': '/int/max/32'}

    @distributed_trace_async
    async def put_max64(
        self,
        int_body: int,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Put max int64 value.

        :param int_body:
        :type int_body: long
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.put_max64.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(int_body, 'long')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_max64.metadata = {'url': '/int/max/64'}

    @distributed_trace_async
    async def put_min32(
        self,
        int_body: int,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Put min int32 value.

        :param int_body:
        :type int_body: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.put_min32.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(int_body, 'int')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_min32.metadata = {'url': '/int/min/32'}

    @distributed_trace_async
    async def put_min64(
        self,
        int_body: int,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Put min int64 value.

        :param int_body:
        :type int_body: long
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.put_min64.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(int_body, 'long')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_min64.metadata = {'url': '/int/min/64'}

    @distributed_trace_async
    async def get_unix_time(
        self,
        cls: ClsType[datetime.datetime] = None,
        **kwargs: Any
    ) -> datetime.datetime:
        """Get datetime encoded as Unix time value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_unix_time.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('unix-time', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_unix_time.metadata = {'url': '/int/unixtime'}

    @distributed_trace_async
    async def put_unix_time_date(
        self,
        int_body: datetime.datetime,
        *,
        cls: ClsType[None] = None,
        **kwargs: Any
    ) -> None:
        """Put datetime encoded as Unix time.

        :param int_body:
        :type int_body: ~datetime.datetime
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.put_unix_time_date.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(int_body, 'unix-time')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    put_unix_time_date.metadata = {'url': '/int/unixtime'}

    @distributed_trace_async
    async def get_invalid_unix_time(
        self,
        cls: ClsType[datetime.datetime] = None,
        **kwargs: Any
    ) -> datetime.datetime:
        """Get invalid Unix time value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_invalid_unix_time.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('unix-time', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_invalid_unix_time.metadata = {'url': '/int/invalidunixtime'}

    @distributed_trace_async
    async def get_null_unix_time(
        self,
        cls: ClsType[datetime.datetime] = None,
        **kwargs: Any
    ) -> datetime.datetime:
        """Get null Unix time value.

        :param callable cls: A custom type or function that will be passed the direct response
        :return: datetime or the result of cls(response)
        :rtype: ~datetime.datetime
        :raises: ~bodyinteger.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})


        # Construct URL
        url = self.get_null_unix_time.metadata['url']

        # Construct parameters
        query_parameters: Dict[str, Any] = {}

        # Construct headers
        header_parameters: Dict[str, Any] = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('unix-time', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_null_unix_time.metadata = {'url': '/int/nullunixtime'}
