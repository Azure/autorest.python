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


class DateModelOperations(object):
    """DateModelOperations operations.

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

    def get_null(self, cls=None, **operation_config):
        """Get null date value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or the result of cls(response)
        :rtype: date
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_null.metadata = {'url': '/date/null'}

    def get_invalid_date(self, cls=None, **operation_config):
        """Get invalid date value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or the result of cls(response)
        :rtype: date
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_invalid_date.metadata = {'url': '/date/invaliddate'}

    def get_overflow_date(self, cls=None, **operation_config):
        """Get overflow date value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or the result of cls(response)
        :rtype: date
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_overflow_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_overflow_date.metadata = {'url': '/date/overflowdate'}

    def get_underflow_date(self, cls=None, **operation_config):
        """Get underflow date value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or the result of cls(response)
        :rtype: date
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_underflow_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_underflow_date.metadata = {'url': '/date/underflowdate'}

    def put_max_date(self, date_body, cls=None, **operation_config):
        """Put max date value 9999-12-31.

        :param date_body:
        :type date_body: date
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.put_max_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(date_body, 'date')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_max_date.metadata = {'url': '/date/max'}

    def get_max_date(self, cls=None, **operation_config):
        """Get max date value 9999-12-31.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or the result of cls(response)
        :rtype: date
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_max_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_max_date.metadata = {'url': '/date/max'}

    def put_min_date(self, date_body, cls=None, **operation_config):
        """Put min date value 0000-01-01.

        :param date_body:
        :type date_body: date
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.put_min_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(date_body, 'date')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_min_date.metadata = {'url': '/date/min'}

    def get_min_date(self, cls=None, **operation_config):
        """Get min date value 0000-01-01.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: date or the result of cls(response)
        :rtype: date
        :raises: :class:`ErrorException<bodydate.models.ErrorException>`
        """
        # Construct URL
        url = self.get_min_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('date', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_min_date.metadata = {'url': '/date/min'}
