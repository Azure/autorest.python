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


class ApiVersionLocalOperations:
    """ApiVersionLocalOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: This should appear as a method parameter, use value '2.0'. Constant value: "2.0".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2.0"

        self._config = config

    async def get_method_local_valid(
            self,  **kwargs):
        """Get method with api-version modeled in the method.  pass in api-version
        = '2.0' to succeed.

        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_method_local_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_method_local_valid.metadata = {'url': '/azurespecials/apiVersion/method/string/none/query/local/2.0'}

    async def get_method_local_null(
            self, api_version=None, **kwargs):
        """Get method with api-version modeled in the method.  pass in api-version
        = null to succeed.

        :param api_version: This should appear as a method parameter, use
         value null, this should result in no serialized parameter
        :type api_version: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_method_local_null.metadata['url']

        # Construct parameters
        query_parameters = {}
        if api_version is not None:
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_method_local_null.metadata = {'url': '/azurespecials/apiVersion/method/string/none/query/local/null'}

    async def get_path_local_valid(
            self,  **kwargs):
        """Get method with api-version modeled in the method.  pass in api-version
        = '2.0' to succeed.

        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_path_local_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_path_local_valid.metadata = {'url': '/azurespecials/apiVersion/path/string/none/query/local/2.0'}

    async def get_swagger_local_valid(
            self,  **kwargs):
        """Get method with api-version modeled in the method.  pass in api-version
        = '2.0' to succeed.

        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.get_swagger_local_valid.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        if self._config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_swagger_local_valid.metadata = {'url': '/azurespecials/apiVersion/swagger/string/none/query/local/2.0'}
