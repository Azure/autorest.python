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


class EnumOperations:
    """EnumOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

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

        self.config = config

    async def get_not_expandable(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get enum value 'red color' from enumeration of 'red color',
        'green-color', 'blue_color'.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Colors or ClientRawResponse if raw=true
        :rtype: ~bodystring.models.Colors or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.get_not_expandable.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Colors', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_not_expandable.metadata = {'url': '/string/enum/notExpandable'}

    async def put_not_expandable(
            self, string_body, *, custom_headers=None, raw=False, **operation_config):
        """Sends value 'red color' from enumeration of 'red color', 'green-color',
        'blue_color'.

        :param string_body: Possible values include: 'red color',
         'green-color', 'blue_color'
        :type string_body: str or ~bodystring.models.Colors
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.put_not_expandable.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(string_body, 'Colors')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_not_expandable.metadata = {'url': '/string/enum/notExpandable'}

    async def get_referenced(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get enum value 'red color' from enumeration of 'red color',
        'green-color', 'blue_color'.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Colors or ClientRawResponse if raw=true
        :rtype: ~bodystring.models.Colors or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.get_referenced.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Colors', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_referenced.metadata = {'url': '/string/enum/Referenced'}

    async def put_referenced(
            self, enum_string_body, *, custom_headers=None, raw=False, **operation_config):
        """Sends value 'red color' from enumeration of 'red color', 'green-color',
        'blue_color'.

        :param enum_string_body: Possible values include: 'red color',
         'green-color', 'blue_color'
        :type enum_string_body: str or ~bodystring.models.Colors
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.put_referenced.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(enum_string_body, 'Colors')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_referenced.metadata = {'url': '/string/enum/Referenced'}

    async def get_referenced_constant(
            self, *, custom_headers=None, raw=False, **operation_config):
        """Get value 'green-color' from the constant.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: RefColorConstant or ClientRawResponse if raw=true
        :rtype: ~bodystring.models.RefColorConstant or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        # Construct URL
        url = self.get_referenced_constant.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('RefColorConstant', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_referenced_constant.metadata = {'url': '/string/enum/ReferencedConstant'}

    async def put_referenced_constant(
            self, field1=None, *, custom_headers=None, raw=False, **operation_config):
        """Sends value 'green-color' from a constant.

        :param field1: Sample string.
        :type field1: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodystring.models.ErrorException>`
        """
        enum_string_body = models.RefColorConstant(field1=field1)

        # Construct URL
        url = self.put_referenced_constant.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(enum_string_body, 'RefColorConstant')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = await self._client.async_send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_referenced_constant.metadata = {'url': '/string/enum/ReferencedConstant'}
