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

from msrest.pipeline import ClientRawResponse

from .. import models


class FilesOperations(object):
    """FilesOperations operations.

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

        self.config = config

    def get_file(
            self, custom_headers=None, raw=False, callback=None, **operation_config):
        """Get file.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyfile.models.ErrorException>`
        """
        # Construct URL
        url = self.get_file.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        body_content = None
        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=True, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_file.metadata = {'url': '/files/stream/nonempty'}

    def get_file_large(
            self, custom_headers=None, raw=False, callback=None, **operation_config):
        """Get a large file.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyfile.models.ErrorException>`
        """
        # Construct URL
        url = self.get_file_large.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        body_content = None
        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=True, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_file_large.metadata = {'url': '/files/stream/verylarge'}

    def get_empty_file(
            self, custom_headers=None, raw=False, callback=None, **operation_config):
        """Get empty file.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param callback: When specified, will be called with each chunk of
         data that is streamed. The callback should take two arguments, the
         bytes of the current chunk of data and the response object. If the
         data is uploading, response will be None.
        :type callback: Callable[Bytes, response=None]
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: Generator or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodyfile.models.ErrorException>`
        """
        # Construct URL
        url = self.get_empty_file.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        body_content = None
        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=True, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = self._client.stream_download(response, callback)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_empty_file.metadata = {'url': '/files/stream/empty'}
