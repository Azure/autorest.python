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


class DictionaryOperations(object):
    """DictionaryOperations operations.

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

    def get_valid(
            self, custom_headers=None, raw=False, **operation_config):
        """Get complex types with dictionary property.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DictionaryWrapper or ClientRawResponse if raw=true
        :rtype: ~fixtures.acceptancetestsbodycomplex.models.DictionaryWrapper
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/dictionary/typed/valid'

        # Construct parameters
        query_parameters = {}

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

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DictionaryWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def put_valid(
            self, default_program=None, custom_headers=None, raw=False, **operation_config):
        """Put complex types with dictionary property.

        :param default_program:
        :type default_program: dict[str, str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        complex_body = models.DictionaryWrapper(default_program=default_program)

        # Construct URL
        url = '/complex/dictionary/typed/valid'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'DictionaryWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get_empty(
            self, custom_headers=None, raw=False, **operation_config):
        """Get complex types with dictionary property which is empty.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DictionaryWrapper or ClientRawResponse if raw=true
        :rtype: ~fixtures.acceptancetestsbodycomplex.models.DictionaryWrapper
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/dictionary/typed/empty'

        # Construct parameters
        query_parameters = {}

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

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DictionaryWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def put_empty(
            self, default_program=None, custom_headers=None, raw=False, **operation_config):
        """Put complex types with dictionary property which is empty.

        :param default_program:
        :type default_program: dict[str, str]
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        complex_body = models.DictionaryWrapper(default_program=default_program)

        # Construct URL
        url = '/complex/dictionary/typed/empty'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'DictionaryWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get_null(
            self, custom_headers=None, raw=False, **operation_config):
        """Get complex types with dictionary property which is null.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DictionaryWrapper or ClientRawResponse if raw=true
        :rtype: ~fixtures.acceptancetestsbodycomplex.models.DictionaryWrapper
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/dictionary/typed/null'

        # Construct parameters
        query_parameters = {}

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

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DictionaryWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_not_provided(
            self, custom_headers=None, raw=False, **operation_config):
        """Get complex types with dictionary property while server doesn't provide
        a response payload.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DictionaryWrapper or ClientRawResponse if raw=true
        :rtype: ~fixtures.acceptancetestsbodycomplex.models.DictionaryWrapper
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/dictionary/typed/notprovided'

        # Construct parameters
        query_parameters = {}

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

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('DictionaryWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
