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


class QueriesOperations(object):
    """QueriesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def array_string_multi_null(
            self, array_query=None, custom_headers=None, raw=False, **operation_config):
        """Get a null array of string using the multi-array format.

        :param array_query: a null array of string using the multi-array
         format
        :type array_query: list of str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsurlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = '/queries/array/multi/string/null'

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def array_string_multi_empty(
            self, array_query=None, custom_headers=None, raw=False, **operation_config):
        """Get an empty array [] of string using the multi-array format.

        :param array_query: an empty array [] of string using the multi-array
         format
        :type array_query: list of str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsurlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = '/queries/array/multi/string/empty'

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def array_string_multi_valid(
            self, array_query=None, custom_headers=None, raw=False, **operation_config):
        """Get an array of string ['ArrayQuery1', 'begin!*'();:@ &=+$,/?#[]end' ,
        null, ''] using the mult-array format.

        :param array_query: an array of string ['ArrayQuery1', 'begin!*'();:@
         &=+$,/?#[]end' , null, ''] using the mult-array format
        :type array_query: list of str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>` if
         raw=true
        :rtype: None or
         :class:`ClientRawResponse<msrest.pipeline.ClientRawResponse>`
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsurlmulticollectionformat.models.ErrorException>`
        """
        # Construct URL
        url = '/queries/array/multi/string/valid'

        # Construct parameters
        query_parameters = {}
        if array_query is not None:
            query_parameters['arrayQuery'] = self._serialize.query("array_query", array_query, '[str]', div=',')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
