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


class Datetimerfc1123Operations(object):
    """Datetimerfc1123Operations operations.

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

    def get_null(
            self, custom_headers=None, raw=False, **operation_config):
        """Get null datetime value.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: datetime or ClientRawResponse if raw=true
        :rtype: datetime or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/null'

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
            deserialized = self._deserialize('rfc-1123', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_invalid(
            self, custom_headers=None, raw=False, **operation_config):
        """Get invalid datetime value.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: datetime or ClientRawResponse if raw=true
        :rtype: datetime or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/invalid'

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
            deserialized = self._deserialize('rfc-1123', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_overflow(
            self, custom_headers=None, raw=False, **operation_config):
        """Get overflow datetime value.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: datetime or ClientRawResponse if raw=true
        :rtype: datetime or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/overflow'

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
            deserialized = self._deserialize('rfc-1123', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_underflow(
            self, custom_headers=None, raw=False, **operation_config):
        """Get underflow datetime value.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: datetime or ClientRawResponse if raw=true
        :rtype: datetime or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/underflow'

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
            deserialized = self._deserialize('rfc-1123', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def put_utc_max_date_time(
            self, datetime_body, custom_headers=None, raw=False, **operation_config):
        """Put max datetime value Fri, 31 Dec 9999 23:59:59 GMT.

        :param datetime_body:
        :type datetime_body: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/max'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(datetime_body, 'rfc-1123')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get_utc_lowercase_max_date_time(
            self, custom_headers=None, raw=False, **operation_config):
        """Get max datetime value fri, 31 dec 9999 23:59:59 gmt.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: datetime or ClientRawResponse if raw=true
        :rtype: datetime or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/max/lowercase'

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
            deserialized = self._deserialize('rfc-1123', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def get_utc_uppercase_max_date_time(
            self, custom_headers=None, raw=False, **operation_config):
        """Get max datetime value FRI, 31 DEC 9999 23:59:59 GMT.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: datetime or ClientRawResponse if raw=true
        :rtype: datetime or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/max/uppercase'

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
            deserialized = self._deserialize('rfc-1123', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def put_utc_min_date_time(
            self, datetime_body, custom_headers=None, raw=False, **operation_config):
        """Put min datetime value Mon, 1 Jan 0001 00:00:00 GMT.

        :param datetime_body:
        :type datetime_body: datetime
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/min'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(datetime_body, 'rfc-1123')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def get_utc_min_date_time(
            self, custom_headers=None, raw=False, **operation_config):
        """Get min datetime value Mon, 1 Jan 0001 00:00:00 GMT.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: datetime or ClientRawResponse if raw=true
        :rtype: datetime or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodydatetimerfc1123.models.ErrorException>`
        """
        # Construct URL
        url = '/datetimerfc1123/min'

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
            deserialized = self._deserialize('rfc-1123', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
