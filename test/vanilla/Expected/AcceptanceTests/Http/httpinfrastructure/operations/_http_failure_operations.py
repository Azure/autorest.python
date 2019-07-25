# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.tracing.decorator import distributed_trace
from azure.core.exceptions import HttpResponseError, map_error

from .. import models


class HttpFailureOperations(object):
    """HttpFailureOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

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
    def get_empty_error(self, cls=None, **kwargs):
        """Get empty error form server.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_empty_error.metadata['url']

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

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_empty_error.metadata = {'url': '/http/failure/emptybody/error'}

    @distributed_trace
    def get_no_model_error(self, cls=None, **kwargs):
        """Get empty error form server.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`HttpResponseError<azure.core.HttpResponseError>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_no_model_error.metadata['url']

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
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_no_model_error.metadata = {'url': '/http/failure/nomodel/error'}

    @distributed_trace
    def get_no_model_empty(self, cls=None, **kwargs):
        """Get empty response from server.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`HttpResponseError<azure.core.HttpResponseError>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_no_model_empty.metadata['url']

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
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_no_model_empty.metadata = {'url': '/http/failure/nomodel/empty'}
