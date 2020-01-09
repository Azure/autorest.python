# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import List
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator import distributed_trace
from msrest.serialization import Model

from .. import models


class ExplicitOperations(object):
    """ExplicitOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~requiredoptional.models
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
    def post_required_integer_parameter(self, body_parameter, cls=None, **kwargs):
        """Test explicitly required integer. Please put null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param body_parameter: 
        :type body_parameter: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_required_integer_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body_parameter, 'int')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_integer_parameter.metadata = {'url': '/reqopt/requied/integer/parameter'}

    @distributed_trace
    def post_optional_integer_parameter(self, body_parameter=None, cls=None, **kwargs):
        """Test explicitly optional integer. Please put null..

        FIXME: add operation.summary


        :param body_parameter: 
        :type body_parameter: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_optional_integer_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'int')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_integer_parameter.metadata = {'url': '/reqopt/optional/integer/parameter'}

    @distributed_trace
    def post_required_integer_property(self, value, cls=None, **kwargs):
        """Test explicitly required integer. Please put a valid int-wrapper with 'value' = null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param value: 
        :type value: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        body_parameter = models.IntWrapper(value=value)

        # Construct URL
        url = self.post_required_integer_property.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body_parameter, 'IntWrapper')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_integer_property.metadata = {'url': '/reqopt/requied/integer/property'}

    @distributed_trace
    def post_optional_integer_property(self, value=None, cls=None, **kwargs):
        """Test explicitly optional integer. Please put a valid int-wrapper with 'value' = null..

        FIXME: add operation.summary


        :param value: 
        :type value: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        body_parameter = models.IntOptionalWrapper(value=value)

        # Construct URL
        url = self.post_optional_integer_property.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'IntOptionalWrapper')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_integer_property.metadata = {'url': '/reqopt/optional/integer/property'}

    @distributed_trace
    def post_required_integer_header(self, header_parameter, cls=None, **kwargs):
        """Test explicitly required integer. Please put a header 'headerParameter' => null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param header_parameter: MISSING·PARAMETER-DESCRIPTION
        :type header_parameter: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_required_integer_header.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, 'int')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_integer_header.metadata = {'url': '/reqopt/requied/integer/header'}

    @distributed_trace
    def post_optional_integer_header(self, header_parameter=None, cls=None, **kwargs):
        """Test explicitly optional integer. Please put a header 'headerParameter' => null..

        FIXME: add operation.summary


        :param header_parameter: MISSING·PARAMETER-DESCRIPTION
        :type header_parameter: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_optional_integer_header.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        if header_parameter is not None:
            header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, 'int')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_integer_header.metadata = {'url': '/reqopt/optional/integer/header'}

    @distributed_trace
    def post_required_string_parameter(self, body_parameter, cls=None, **kwargs):
        """Test explicitly required string. Please put null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param body_parameter: 
        :type body_parameter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_required_string_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body_parameter, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_string_parameter.metadata = {'url': '/reqopt/requied/string/parameter'}

    @distributed_trace
    def post_optional_string_parameter(self, body_parameter=None, cls=None, **kwargs):
        """Test explicitly optional string. Please put null..

        FIXME: add operation.summary


        :param body_parameter: 
        :type body_parameter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_optional_string_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'str')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_string_parameter.metadata = {'url': '/reqopt/optional/string/parameter'}

    @distributed_trace
    def post_required_string_property(self, value, cls=None, **kwargs):
        """Test explicitly required string. Please put a valid string-wrapper with 'value' = null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param value: 
        :type value: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        body_parameter = models.StringWrapper(value=value)

        # Construct URL
        url = self.post_required_string_property.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body_parameter, 'StringWrapper')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_string_property.metadata = {'url': '/reqopt/requied/string/property'}

    @distributed_trace
    def post_optional_string_property(self, value=None, cls=None, **kwargs):
        """Test explicitly optional integer. Please put a valid string-wrapper with 'value' = null..

        FIXME: add operation.summary


        :param value: 
        :type value: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        body_parameter = models.StringOptionalWrapper(value=value)

        # Construct URL
        url = self.post_optional_string_property.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'StringOptionalWrapper')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_string_property.metadata = {'url': '/reqopt/optional/string/property'}

    @distributed_trace
    def post_required_string_header(self, header_parameter, cls=None, **kwargs):
        """Test explicitly required string. Please put a header 'headerParameter' => null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param header_parameter: MISSING·PARAMETER-DESCRIPTION
        :type header_parameter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_required_string_header.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, 'str')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_string_header.metadata = {'url': '/reqopt/requied/string/header'}

    @distributed_trace
    def post_optional_string_header(self, body_parameter=None, cls=None, **kwargs):
        """Test explicitly optional string. Please put a header 'headerParameter' => null..

        FIXME: add operation.summary


        :param body_parameter: MISSING·PARAMETER-DESCRIPTION
        :type body_parameter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_optional_string_header.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        if body_parameter is not None:
            header_parameters['bodyParameter'] = self._serialize.header("body_parameter", body_parameter, 'str')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_string_header.metadata = {'url': '/reqopt/optional/string/header'}

    @distributed_trace
    def post_required_class_parameter(self, body_parameter, cls=None, **kwargs):
        """Test explicitly required complex object. Please put null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param body_parameter: 
        :type body_parameter: ~requiredoptional.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_required_class_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body_parameter, 'Product')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_class_parameter.metadata = {'url': '/reqopt/requied/class/parameter'}

    @distributed_trace
    def post_optional_class_parameter(self, body_parameter=None, cls=None, **kwargs):
        """Test explicitly optional complex object. Please put null..

        FIXME: add operation.summary


        :param body_parameter: 
        :type body_parameter: ~requiredoptional.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_optional_class_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_class_parameter.metadata = {'url': '/reqopt/optional/class/parameter'}

    @distributed_trace
    def post_required_class_property(self, value, cls=None, **kwargs):
        """Test explicitly required complex object. Please put a valid class-wrapper with 'value' = null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param value: 
        :type value: ~requiredoptional.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        body_parameter = models.ClassWrapper(value=value)

        # Construct URL
        url = self.post_required_class_property.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body_parameter, 'ClassWrapper')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_class_property.metadata = {'url': '/reqopt/requied/class/property'}

    @distributed_trace
    def post_optional_class_property(self, value=None, cls=None, **kwargs):
        """Test explicitly optional complex object. Please put a valid class-wrapper with 'value' = null..

        FIXME: add operation.summary


        :param value: 
        :type value: ~requiredoptional.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        body_parameter = models.ClassOptionalWrapper(value=value)

        # Construct URL
        url = self.post_optional_class_property.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'ClassOptionalWrapper')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_class_property.metadata = {'url': '/reqopt/optional/class/property'}

    @distributed_trace
    def post_required_array_parameter(self, body_parameter, cls=None, **kwargs):
        """Test explicitly required array. Please put null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param body_parameter: 
        :type body_parameter: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_required_array_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body_parameter, '[str]')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_array_parameter.metadata = {'url': '/reqopt/requied/array/parameter'}

    @distributed_trace
    def post_optional_array_parameter(self, body_parameter=None, cls=None, **kwargs):
        """Test explicitly optional array. Please put null..

        FIXME: add operation.summary


        :param body_parameter: 
        :type body_parameter: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_optional_array_parameter.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, '[str]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_array_parameter.metadata = {'url': '/reqopt/optional/array/parameter'}

    @distributed_trace
    def post_required_array_property(self, value, cls=None, **kwargs):
        """Test explicitly required array. Please put a valid array-wrapper with 'value' = null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param value: 
        :type value: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        body_parameter = models.ArrayWrapper(value=value)

        # Construct URL
        url = self.post_required_array_property.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(body_parameter, 'ArrayWrapper')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_array_property.metadata = {'url': '/reqopt/requied/array/property'}

    @distributed_trace
    def post_optional_array_property(self, value=None, cls=None, **kwargs):
        """Test explicitly optional array. Please put a valid array-wrapper with 'value' = null..

        FIXME: add operation.summary


        :param value: 
        :type value: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        body_parameter = models.ArrayOptionalWrapper(value=value)

        # Construct URL
        url = self.post_optional_array_property.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body_parameter is not None:
            body_content = self._serialize.body(body_parameter, 'ArrayOptionalWrapper')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_array_property.metadata = {'url': '/reqopt/optional/array/property'}

    @distributed_trace
    def post_required_array_header(self, header_parameter, cls=None, **kwargs):
        """Test explicitly required array. Please put a header 'headerParameter' => null and the client library should throw before the request is sent..

        FIXME: add operation.summary


        :param header_parameter: MISSING·PARAMETER-DESCRIPTION
        :type header_parameter: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_required_array_header.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, '[str]', div=',')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_required_array_header.metadata = {'url': '/reqopt/requied/array/header'}

    @distributed_trace
    def post_optional_array_header(self, header_parameter=None, cls=None, **kwargs):
        """Test explicitly optional integer. Please put a header 'headerParameter' => null..

        FIXME: add operation.summary


        :param header_parameter: MISSING·PARAMETER-DESCRIPTION
        :type header_parameter: list[str]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~requiredoptional.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_optional_array_header.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        if header_parameter is not None:
            header_parameters['headerParameter'] = self._serialize.header("header_parameter", header_parameter, '[str]', div=',')


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_optional_array_header.metadata = {'url': '/reqopt/optional/array/header'}

