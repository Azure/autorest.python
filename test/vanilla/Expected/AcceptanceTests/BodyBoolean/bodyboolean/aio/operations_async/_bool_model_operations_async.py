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


from ... import models


class BoolModelOperations:
    """BoolModelOperations async operations.

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
        self._config = config

    async def get_true(self, *, cls=None, **operation_config):
        """Get true Boolean value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        # Construct URL
        url = self.get_true.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_true.metadata = {'url': '/bool/true'}

    async def put_true(self, *, cls=None, **operation_config):
        """Set Boolean value true.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        bool_body = True

        # Construct URL
        url = self.put_true.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(bool_body, 'bool')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_true.metadata = {'url': '/bool/true'}

    async def get_false(self, *, cls=None, **operation_config):
        """Get false Boolean value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        # Construct URL
        url = self.get_false.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_false.metadata = {'url': '/bool/false'}

    async def put_false(self, *, cls=None, **operation_config):
        """Set Boolean value false.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        bool_body = False

        # Construct URL
        url = self.put_false.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(bool_body, 'bool')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_false.metadata = {'url': '/bool/false'}

    async def get_null(self, *, cls=None, **operation_config):
        """Get null Boolean value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
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
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_null.metadata = {'url': '/bool/null'}

    async def get_invalid(self, *, cls=None, **operation_config):
        """Get invalid Boolean value.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises: :class:`ErrorException<bodyboolean.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('bool', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_invalid.metadata = {'url': '/bool/invalid'}
