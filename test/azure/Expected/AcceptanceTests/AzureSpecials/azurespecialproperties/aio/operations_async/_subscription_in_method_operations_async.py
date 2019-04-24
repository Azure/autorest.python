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


class SubscriptionInMethodOperations:
    """SubscriptionInMethodOperations async operations.

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

    async def post_method_local_valid(
            self,  **kwargs):
        """POST method with subscriptionId modeled in the method.  pass in
        subscription id = '1234-5678-9012-3456' to succeed.

        :param subscription_id: This should appear as a method parameter, use
         value '1234-5678-9012-3456'
        :type subscription_id: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.post_method_local_valid.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

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
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_method_local_valid.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}

    async def post_method_local_null(
            self,  **kwargs):
        """POST method with subscriptionId modeled in the method.  pass in
        subscription id = null, client-side validation should prevent you from
        making this call.

        :param subscription_id: This should appear as a method parameter, use
         value null, client-side validation should prvenet the call
        :type subscription_id: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.post_method_local_null.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

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
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_method_local_null.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/local/null/{subscriptionId}'}

    async def post_path_local_valid(
            self,  **kwargs):
        """POST method with subscriptionId modeled in the method.  pass in
        subscription id = '1234-5678-9012-3456' to succeed.

        :param subscription_id: Should appear as a method parameter -use value
         '1234-5678-9012-3456'
        :type subscription_id: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.post_path_local_valid.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

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
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_path_local_valid.metadata = {'url': '/azurespecials/subscriptionId/path/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}

    async def post_swagger_local_valid(
            self,  **kwargs):
        """POST method with subscriptionId modeled in the method.  pass in
        subscription id = '1234-5678-9012-3456' to succeed.

        :param subscription_id: The subscriptionId, which appears in the path,
         the value is always '1234-5678-9012-3456'
        :type subscription_id: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        # Construct URL
        url = self.post_swagger_local_valid.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

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
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    post_swagger_local_valid.metadata = {'url': '/azurespecials/subscriptionId/swagger/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}
