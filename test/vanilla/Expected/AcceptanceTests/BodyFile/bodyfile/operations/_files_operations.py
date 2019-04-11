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


from .. import models


class FilesOperations(object):
    """FilesOperations operations.

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

    def get_file(self, cls=None, **operation_config):
        """Get file.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or the result of cls(response)
        :rtype: Generator
        :raises: :class:`ErrorException<bodyfile.models.ErrorException>`
        """
        # Construct URL
        url = self.get_file.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=True, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = self._client.stream_download(response, callback)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_file.metadata = {'url': '/files/stream/nonempty'}

    def get_file_large(self, cls=None, **operation_config):
        """Get a large file.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or the result of cls(response)
        :rtype: Generator
        :raises: :class:`ErrorException<bodyfile.models.ErrorException>`
        """
        # Construct URL
        url = self.get_file_large.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=True, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = self._client.stream_download(response, callback)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_file_large.metadata = {'url': '/files/stream/verylarge'}

    def get_empty_file(self, cls=None, **operation_config):
        """Get empty file.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or the result of cls(response)
        :rtype: Generator
        :raises: :class:`ErrorException<bodyfile.models.ErrorException>`
        """
        # Construct URL
        url = self.get_empty_file.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=True, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = self._client.stream_download(response, callback)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_empty_file.metadata = {'url': '/files/stream/empty'}
