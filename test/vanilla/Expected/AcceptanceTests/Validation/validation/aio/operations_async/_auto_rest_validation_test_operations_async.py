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

from azure.core import HttpRequestError
from ... import models


class AutoRestValidationTestOperationsMixin:

    async def validation_of_method_parameters(
            self,  **kwargs):
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars
         with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :return: Product
        :rtype: ~validation.models.Product
        :raises: :class:`ErrorException<validation.models.ErrorException>`
        """
        # Construct URL
        url = self.validation_of_method_parameters.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'id': self._serialize.url("id", id, 'int', maximum=1000, minimum=100, multiple=10)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['apiVersion'] = self._serialize.query("self.api_version", self.api_version, 'str', pattern=r'\d{2}-\d{2}-\d{4}')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)

        return deserialized
    validation_of_method_parameters.metadata = {'url': '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'}

    async def validation_of_body(
            self, resource_group_name, id, body=None, **kwargs):
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars
         with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param body:
        :type body: ~validation.models.Product
        :return: Product
        :rtype: ~validation.models.Product
        :raises: :class:`ErrorException<validation.models.ErrorException>`
        """
        # Construct URL
        url = self.validation_of_body.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'id': self._serialize.url("id", id, 'int', maximum=1000, minimum=100, multiple=10)
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['apiVersion'] = self._serialize.query("self.api_version", self.api_version, 'str', pattern=r'\d{2}-\d{2}-\d{4}')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)

        return deserialized
    validation_of_body.metadata = {'url': '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'}

    async def get_with_constant_in_path(
            self,  **kwargs):
        """

        :return: None
        :rtype: None
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        constant_param = "constant"

        # Construct URL
        url = self.get_with_constant_in_path.metadata['url']
        path_format_arguments = {
            'constantParam': self._serialize.url("constant_param", constant_param, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

    get_with_constant_in_path.metadata = {'url': '/validation/constantsInPath/{constantParam}/value'}

    async def post_with_constant_in_body(
            self, body=None, **kwargs):
        """

        :param body:
        :type body: ~validation.models.Product
        :return: Product
        :rtype: ~validation.models.Product
        :raises: :class:`HttpRequestError<azure.core.HttpRequestError>`
        """
        constant_param = "constant"

        # Construct URL
        url = self.post_with_constant_in_body.metadata['url']
        path_format_arguments = {
            'constantParam': self._serialize.url("constant_param", constant_param, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise HttpRequestError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Product', response)

        return deserialized
    post_with_constant_in_body.metadata = {'url': '/validation/constantsInPath/{constantParam}/value'}
