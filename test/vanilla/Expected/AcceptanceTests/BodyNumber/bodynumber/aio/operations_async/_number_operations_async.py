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


class NumberOperations:
    """NumberOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodynumber.models
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
        """Get null Number value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/number/null'}

    @distributed_trace_async
    async def get_invalid_float(self, cls=None, **kwargs):
        """Get invalid float Number value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_invalid_float.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_invalid_float.metadata = {'url': '/number/invalidfloat'}

    @distributed_trace_async
    async def get_invalid_double(self, cls=None, **kwargs):
        """Get invalid double Number value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_invalid_double.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_invalid_double.metadata = {'url': '/number/invaliddouble'}

    @distributed_trace_async
    async def get_invalid_decimal(self, cls=None, **kwargs):
        """Get invalid decimal Number value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_invalid_decimal.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_invalid_decimal.metadata = {'url': '/number/invaliddecimal'}

    @distributed_trace_async
    async def put_big_float(self, number_body, cls=None, **kwargs):
        """Put big float value 3.402823e+20.

        FIXME: add operation.summary

        :param number_body: 
        :type number_body: float
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_big_float.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_big_float.metadata = {'url': '/number/big/float/3.402823e+20'}

    @distributed_trace_async
    async def get_big_float(self, cls=None, **kwargs):
        """Get big float value 3.402823e+20.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_big_float.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_big_float.metadata = {'url': '/number/big/float/3.402823e+20'}

    @distributed_trace_async
    async def put_big_double(self, number_body, cls=None, **kwargs):
        """Put big double value 2.5976931e+101.

        FIXME: add operation.summary

        :param number_body: 
        :type number_body: float
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_big_double.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_big_double.metadata = {'url': '/number/big/double/2.5976931e+101'}

    @distributed_trace_async
    async def get_big_double(self, cls=None, **kwargs):
        """Get big double value 2.5976931e+101.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_big_double.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_big_double.metadata = {'url': '/number/big/double/2.5976931e+101'}

    @distributed_trace_async
    async def put_big_double_positive_decimal(self, cls=None, **kwargs):
        """Put big double value 99999999.99.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        number_body = 99999999.99

        # Construct URL
        url = self.put_big_double_positive_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_big_double_positive_decimal.metadata = {'url': '/number/big/double/99999999.99'}

    @distributed_trace_async
    async def get_big_double_positive_decimal(self, cls=None, **kwargs):
        """Get big double value 99999999.99.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_big_double_positive_decimal.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_big_double_positive_decimal.metadata = {'url': '/number/big/double/99999999.99'}

    @distributed_trace_async
    async def put_big_double_negative_decimal(self, cls=None, **kwargs):
        """Put big double value -99999999.99.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        number_body = -99999999.99

        # Construct URL
        url = self.put_big_double_negative_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_big_double_negative_decimal.metadata = {'url': '/number/big/double/-99999999.99'}

    @distributed_trace_async
    async def get_big_double_negative_decimal(self, cls=None, **kwargs):
        """Get big double value -99999999.99.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_big_double_negative_decimal.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_big_double_negative_decimal.metadata = {'url': '/number/big/double/-99999999.99'}

    @distributed_trace_async
    async def put_big_decimal(self, number_body, cls=None, **kwargs):
        """Put big decimal value 2.5976931e+101.

        FIXME: add operation.summary

        :param number_body: 
        :type number_body: float
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_big_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_big_decimal.metadata = {'url': '/number/big/decimal/2.5976931e+101'}

    @distributed_trace_async
    async def get_big_decimal(self, cls=None, **kwargs):
        """Get big decimal value 2.5976931e+101.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_big_decimal.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_big_decimal.metadata = {'url': '/number/big/decimal/2.5976931e+101'}

    @distributed_trace_async
    async def put_big_decimal_positive_decimal(self, cls=None, **kwargs):
        """Put big decimal value 99999999.99.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        number_body = 99999999.99

        # Construct URL
        url = self.put_big_decimal_positive_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_big_decimal_positive_decimal.metadata = {'url': '/number/big/decimal/99999999.99'}

    @distributed_trace_async
    async def get_big_decimal_positive_decimal(self, cls=None, **kwargs):
        """Get big decimal value 99999999.99.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_big_decimal_positive_decimal.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_big_decimal_positive_decimal.metadata = {'url': '/number/big/decimal/99999999.99'}

    @distributed_trace_async
    async def put_big_decimal_negative_decimal(self, cls=None, **kwargs):
        """Put big decimal value -99999999.99.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        number_body = -99999999.99

        # Construct URL
        url = self.put_big_decimal_negative_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_big_decimal_negative_decimal.metadata = {'url': '/number/big/decimal/-99999999.99'}

    @distributed_trace_async
    async def get_big_decimal_negative_decimal(self, cls=None, **kwargs):
        """Get big decimal value -99999999.99.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_big_decimal_negative_decimal.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_big_decimal_negative_decimal.metadata = {'url': '/number/big/decimal/-99999999.99'}

    @distributed_trace_async
    async def put_small_float(self, number_body, cls=None, **kwargs):
        """Put small float value 3.402823e-20.

        FIXME: add operation.summary

        :param number_body: 
        :type number_body: float
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_small_float.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_small_float.metadata = {'url': '/number/small/float/3.402823e-20'}

    @distributed_trace_async
    async def get_small_float(self, cls=None, **kwargs):
        """Get big double value 3.402823e-20.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_small_float.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_small_float.metadata = {'url': '/number/small/float/3.402823e-20'}

    @distributed_trace_async
    async def put_small_double(self, number_body, cls=None, **kwargs):
        """Put small double value 2.5976931e-101.

        FIXME: add operation.summary

        :param number_body: 
        :type number_body: float
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_small_double.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_small_double.metadata = {'url': '/number/small/double/2.5976931e-101'}

    @distributed_trace_async
    async def get_small_double(self, cls=None, **kwargs):
        """Get big double value 2.5976931e-101.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_small_double.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_small_double.metadata = {'url': '/number/small/double/2.5976931e-101'}

    @distributed_trace_async
    async def put_small_decimal(self, number_body, cls=None, **kwargs):
        """Put small decimal value 2.5976931e-101.

        FIXME: add operation.summary

        :param number_body: 
        :type number_body: float
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_small_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_small_decimal.metadata = {'url': '/number/small/decimal/2.5976931e-101'}

    @distributed_trace_async
    async def get_small_decimal(self, cls=None, **kwargs):
        """Get small decimal value 2.5976931e-101.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: float or the result of cls(response)
        :rtype: float
        :raises: ~bodynumber.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_small_decimal.metadata['url']

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

        deserialized = self._deserialize('float', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_small_decimal.metadata = {'url': '/number/small/decimal/2.5976931e-101'}
