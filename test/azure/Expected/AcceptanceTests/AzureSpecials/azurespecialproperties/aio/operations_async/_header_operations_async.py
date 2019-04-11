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

import uuid

from ... import models


class HeaderOperations:
    """HeaderOperations async operations.

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

    async def custom_named_request_id(self, foo_client_request_id, *, cls=None, **operation_config):
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in
        the header of the request.

        :param foo_client_request_id: The fooRequestId
        :type foo_client_request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.custom_named_request_id.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['foo-client-request-id'] = str(uuid.uuid1())
        header_parameters['foo-client-request-id'] = self._serialize.header("foo_client_request_id", foo_client_request_id, 'str')
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'foo-request-id': self._deserialize('str', response.headers.get('foo-request-id')),
            }
            return cls(response, None, response_headers)
    custom_named_request_id.metadata = {'url': '/azurespecials/customNamedRequestId'}

    async def custom_named_request_id_param_grouping(self, header_custom_named_request_id_param_grouping_parameters, *, cls=None, **operation_config):
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in
        the header of the request, via a parameter group.

        :param header_custom_named_request_id_param_grouping_parameters:
         Additional parameters for the operation
        :type header_custom_named_request_id_param_grouping_parameters:
         ~azurespecialproperties.models.HeaderCustomNamedRequestIdParamGroupingParameters
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        foo_client_request_id = None
        if header_custom_named_request_id_param_grouping_parameters is not None:
            foo_client_request_id = header_custom_named_request_id_param_grouping_parameters.foo_client_request_id

        # Construct URL
        url = self.custom_named_request_id_param_grouping.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['foo-client-request-id'] = str(uuid.uuid1())
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        header_parameters['foo-client-request-id'] = self._serialize.header("foo_client_request_id", foo_client_request_id, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'foo-request-id': self._deserialize('str', response.headers.get('foo-request-id')),
            }
            return cls(response, None, response_headers)
    custom_named_request_id_param_grouping.metadata = {'url': '/azurespecials/customNamedRequestIdParamGrouping'}

    async def custom_named_request_id_head(self, foo_client_request_id, *, cls=None, **operation_config):
        """Send foo-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in
        the header of the request.

        :param foo_client_request_id: The fooRequestId
        :type foo_client_request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: bool or the result of cls(response)
        :rtype: bool
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.custom_named_request_id_head.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['foo-client-request-id'] = str(uuid.uuid1())
        header_parameters['foo-client-request-id'] = self._serialize.header("foo_client_request_id", foo_client_request_id, 'str')
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 404]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = (response.status_code == 200)
        if cls:
            response_headers = {
                'foo-request-id': self._deserialize('str', response.headers.get('foo-request-id')),
                }
            return cls(response, deserialized, response_headers)
        return deserialized
    custom_named_request_id_head.metadata = {'url': '/azurespecials/customNamedRequestIdHead'}
