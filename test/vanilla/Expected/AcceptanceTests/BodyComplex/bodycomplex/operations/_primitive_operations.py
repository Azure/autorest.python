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

from azure.core.exceptions import HttpResponseError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PrimitiveOperations(object):
    """PrimitiveOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplex.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_int(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.IntWrapper"
        """Get complex types with integer properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IntWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.IntWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.IntWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_int.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('IntWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_int.metadata = {'url': '/complex/primitive/integer'}

    @distributed_trace
    def put_int(
        self,
        complex_body,  # type: "models.IntWrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with integer properties.

        :param complex_body: Please put -1 and 2.
        :type complex_body: ~bodycomplex.models.IntWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_int.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'IntWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_int.metadata = {'url': '/complex/primitive/integer'}

    @distributed_trace
    def get_long(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.LongWrapper"
        """Get complex types with long properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LongWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.LongWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.LongWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_long.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('LongWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_long.metadata = {'url': '/complex/primitive/long'}

    @distributed_trace
    def put_long(
        self,
        complex_body,  # type: "models.LongWrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with long properties.

        :param complex_body: Please put 1099511627775 and -999511627788.
        :type complex_body: ~bodycomplex.models.LongWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_long.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'LongWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_long.metadata = {'url': '/complex/primitive/long'}

    @distributed_trace
    def get_float(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.FloatWrapper"
        """Get complex types with float properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FloatWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.FloatWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.FloatWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('FloatWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_float.metadata = {'url': '/complex/primitive/float'}

    @distributed_trace
    def put_float(
        self,
        complex_body,  # type: "models.FloatWrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with float properties.

        :param complex_body: Please put 1.05 and -0.003.
        :type complex_body: ~bodycomplex.models.FloatWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'FloatWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_float.metadata = {'url': '/complex/primitive/float'}

    @distributed_trace
    def get_double(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DoubleWrapper"
        """Get complex types with double properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DoubleWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DoubleWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.DoubleWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DoubleWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_double.metadata = {'url': '/complex/primitive/double'}

    @distributed_trace
    def put_double(
        self,
        complex_body,  # type: "models.DoubleWrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with double properties.

        :param complex_body: Please put 3e-100 and
         -0.000000000000000000000000000000000000000000000000000000005.
        :type complex_body: ~bodycomplex.models.DoubleWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'DoubleWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_double.metadata = {'url': '/complex/primitive/double'}

    @distributed_trace
    def get_bool(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.BooleanWrapper"
        """Get complex types with bool properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BooleanWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.BooleanWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.BooleanWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_bool.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('BooleanWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_bool.metadata = {'url': '/complex/primitive/bool'}

    @distributed_trace
    def put_bool(
        self,
        complex_body,  # type: "models.BooleanWrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with bool properties.

        :param complex_body: Please put true and false.
        :type complex_body: ~bodycomplex.models.BooleanWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_bool.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'BooleanWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_bool.metadata = {'url': '/complex/primitive/bool'}

    @distributed_trace
    def get_string(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.StringWrapper"
        """Get complex types with string properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: StringWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.StringWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.StringWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('StringWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_string.metadata = {'url': '/complex/primitive/string'}

    @distributed_trace
    def put_string(
        self,
        complex_body,  # type: "models.StringWrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with string properties.

        :param complex_body: Please put 'goodrequest', '', and null.
        :type complex_body: ~bodycomplex.models.StringWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'StringWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_string.metadata = {'url': '/complex/primitive/string'}

    @distributed_trace
    def get_date(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DateWrapper"
        """Get complex types with date properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DateWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DateWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.DateWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DateWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_date.metadata = {'url': '/complex/primitive/date'}

    @distributed_trace
    def put_date(
        self,
        complex_body,  # type: "models.DateWrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with date properties.

        :param complex_body: Please put '0001-01-01' and '2016-02-29'.
        :type complex_body: ~bodycomplex.models.DateWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'DateWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_date.metadata = {'url': '/complex/primitive/date'}

    @distributed_trace
    def get_date_time(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DatetimeWrapper"
        """Get complex types with datetime properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DatetimeWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DatetimeWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.DatetimeWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DatetimeWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_date_time.metadata = {'url': '/complex/primitive/datetime'}

    @distributed_trace
    def put_date_time(
        self,
        complex_body,  # type: "models.DatetimeWrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with datetime properties.

        :param complex_body: Please put '0001-01-01T12:00:00-04:00' and '2015-05-18T11:38:00-08:00'.
        :type complex_body: ~bodycomplex.models.DatetimeWrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_date_time.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'DatetimeWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_date_time.metadata = {'url': '/complex/primitive/datetime'}

    @distributed_trace
    def get_date_time_rfc1123(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Datetimerfc1123Wrapper"
        """Get complex types with datetimeRfc1123 properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Datetimerfc1123Wrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.Datetimerfc1123Wrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.Datetimerfc1123Wrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_date_time_rfc1123.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('Datetimerfc1123Wrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_date_time_rfc1123.metadata = {'url': '/complex/primitive/datetimerfc1123'}

    @distributed_trace
    def put_date_time_rfc1123(
        self,
        complex_body,  # type: "models.Datetimerfc1123Wrapper"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with datetimeRfc1123 properties.

        :param complex_body: Please put 'Mon, 01 Jan 0001 12:00:00 GMT' and 'Mon, 18 May 2015 11:38:00
         GMT'.
        :type complex_body: ~bodycomplex.models.Datetimerfc1123Wrapper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_date_time_rfc1123.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Datetimerfc1123Wrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_date_time_rfc1123.metadata = {'url': '/complex/primitive/datetimerfc1123'}

    @distributed_trace
    def get_duration(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DurationWrapper"
        """Get complex types with duration properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DurationWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.DurationWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.DurationWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_duration.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('DurationWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_duration.metadata = {'url': '/complex/primitive/duration'}

    @distributed_trace
    def put_duration(
        self,
        field=None,  # type: Optional[datetime.timedelta]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with duration properties.

        :param field:
        :type field: ~datetime.timedelta
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        _complex_body = models.DurationWrapper(field=field)

        # Construct URL
        url = self.put_duration.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(_complex_body, 'DurationWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_duration.metadata = {'url': '/complex/primitive/duration'}

    @distributed_trace
    def get_byte(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ByteWrapper"
        """Get complex types with byte properties.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ByteWrapper or the result of cls(response)
        :rtype: ~bodycomplex.models.ByteWrapper
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType["models.ByteWrapper"]
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_byte.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('ByteWrapper', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_byte.metadata = {'url': '/complex/primitive/byte'}

    @distributed_trace
    def put_byte(
        self,
        field=None,  # type: Optional[bytearray]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put complex types with byte properties.

        :param field:
        :type field: bytearray
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})

        _complex_body = models.ByteWrapper(field=field)

        # Construct URL
        url = self.put_byte.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(_complex_body, 'ByteWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
          return cls(pipeline_response, None, {})

    put_byte.metadata = {'url': '/complex/primitive/byte'}
