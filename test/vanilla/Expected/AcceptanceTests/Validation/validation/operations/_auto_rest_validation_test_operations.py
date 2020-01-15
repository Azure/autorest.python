# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional
import warnings

from azure.core.exceptions import HttpResponseError, map_error
from azure.core.tracing.decorator import distributed_trace
from msrest.serialization import Model

from .. import models


class AutoRestValidationTestOperationsMixin(object):
    @distributed_trace
    def validation_of_method_parameters(self, resource_group_name, id, cls=None, **kwargs):
        # type: (str, int, Optional[Any], **Any) -> "Product"
        """Validates input parameters on the method. See swagger for details..

        FIXME: add operation.summary


        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~validation.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.0.0"

        # Construct URL
        url = self.validation_of_method_parameters.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern='[a-zA-Z0-9]+'),
            'id': self._serialize.url("id", id, 'int', maximum=1000, minimum=100, multiple=10),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['apiVersion'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Product', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    validation_of_method_parameters.metadata = {'url': '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'}

    @distributed_trace
    def validation_of_body(self, resource_group_name, id, body=None, cls=None, **kwargs):
        # type: (str, int, Optional["Product"], Optional[Any], **Any) -> "Product"
        """Validates body parameters on the method. See swagger for details..

        FIXME: add operation.summary


        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param body: 
        :type body: ~validation.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~validation.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.0.0"

        # Construct URL
        url = self.validation_of_body.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern='[a-zA-Z0-9]+'),
            'id': self._serialize.url("id", id, 'int', maximum=1000, minimum=100, multiple=10),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['apiVersion'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Product', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    validation_of_body.metadata = {'url': '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'}

    @distributed_trace
    def get_with_constant_in_path(self, cls=None, **kwargs):
        # type: (Optional[Any], **Any) -> None
        """MISSING·OPERATION-DESCRIPTION.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})
        constant_param = "constant"

        # Construct URL
        url = self.get_with_constant_in_path.metadata['url']
        path_format_arguments = {
            'constantParam': self._serialize.url("constant_param", constant_param, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
          return cls(response, None, {})

    get_with_constant_in_path.metadata = {'url': '/validation/constantsInPath/{constantParam}/value'}

    @distributed_trace
    def post_with_constant_in_body(self, body=None, cls=None, **kwargs):
        # type: (Optional["Product"], Optional[Any], **Any) -> "Product"
        """MISSING·OPERATION-DESCRIPTION.

        FIXME: add operation.summary


        :param body: 
        :type body: ~validation.models.Product
        :param callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})
        constant_param = "constant"

        # Construct URL
        url = self.post_with_constant_in_body.metadata['url']
        path_format_arguments = {
            'constantParam': self._serialize.url("constant_param", constant_param, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('Product', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    post_with_constant_in_body.metadata = {'url': '/validation/constantsInPath/{constantParam}/value'}

