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

from .. import models


class BoolOperations(object):
    """BoolOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyboolean.models
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
    def get_true(self, cls=None, **kwargs):
        """Get true Boolean value.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: bool
        :raises: ~bodyboolean.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_true.metadata['url']

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
            raise models.ErrorException(response, self._deserialize)

        deserialized = self._deserialize('bool', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_true.metadata = {'url': '/bool/true'}

    @distributed_trace
    def put_true(self, cls=None, **kwargs):
        """Set Boolean value true.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~bodyboolean.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)
        bool_body = True

        # Construct URL
        url = self.put_true.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(bool_body, 'bool')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_true.metadata = {'url': '/bool/true'}

    @distributed_trace
    def get_false(self, cls=None, **kwargs):
        """Get false Boolean value.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: bool
        :raises: ~bodyboolean.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_false.metadata['url']

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
            raise models.ErrorException(response, self._deserialize)

        deserialized = self._deserialize('bool', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_false.metadata = {'url': '/bool/false'}

    @distributed_trace
    def put_false(self, cls=None, **kwargs):
        """Set Boolean value false.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~bodyboolean.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)
        bool_body = False

        # Construct URL
        url = self.put_false.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(bool_body, 'bool')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_false.metadata = {'url': '/bool/false'}

    @distributed_trace
    def get_null(self, cls=None, **kwargs):
        """Get null Boolean value.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: bool
        :raises: ~bodyboolean.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_null.metadata['url']

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
            raise models.ErrorException(response, self._deserialize)

        deserialized = self._deserialize('bool', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/bool/null'}

    @distributed_trace
    def get_invalid(self, cls=None, **kwargs):
        """Get invalid Boolean value.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return:  or the result of cls(response)
        :rtype: bool
        :raises: ~bodyboolean.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', None)

        # Construct URL
        url = self.get_invalid.metadata['url']

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
            raise models.ErrorException(response, self._deserialize)

        deserialized = self._deserialize('bool', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_invalid.metadata = {'url': '/bool/invalid'}

