# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import uuid
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class SubscriptionInMethodOperations:
    """SubscriptionInMethodOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
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
    @distributed_trace_async
    async def post_method_local_valid(self, subscription_id: str, cls=None, **kwargs):
        """POST method with subscriptionId modeled in the method.  pass in subscription id = '1234-5678-9012-3456' to succeed.

        FIXME: add operation.summary


        :param subscription_id: This should appear as a method parameter, use value '1234-5678-9012-3456'
        :type subscription_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_method_local_valid.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_method_local_valid.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}

    @distributed_trace_async
    async def post_method_local_null(self, subscription_id: str, cls=None, **kwargs):
        """POST method with subscriptionId modeled in the method.  pass in subscription id = null, client-side validation should prevent you from making this call.

        FIXME: add operation.summary


        :param subscription_id: This should appear as a method parameter, use value '1234-5678-9012-3456'
        :type subscription_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_method_local_null.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_method_local_null.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/local/null/{subscriptionId}'}

    @distributed_trace_async
    async def post_path_local_valid(self, subscription_id: str, cls=None, **kwargs):
        """POST method with subscriptionId modeled in the method.  pass in subscription id = '1234-5678-9012-3456' to succeed.

        FIXME: add operation.summary


        :param subscription_id: This should appear as a method parameter, use value '1234-5678-9012-3456'
        :type subscription_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_path_local_valid.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_path_local_valid.metadata = {'url': '/azurespecials/subscriptionId/path/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}

    @distributed_trace_async
    async def post_swagger_local_valid(self, subscription_id: str, cls=None, **kwargs):
        """POST method with subscriptionId modeled in the method.  pass in subscription id = '1234-5678-9012-3456' to succeed.

        FIXME: add operation.summary


        :param subscription_id: This should appear as a method parameter, use value '1234-5678-9012-3456'
        :type subscription_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~azurespecialproperties.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.post_swagger_local_valid.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("subscription_id", subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        kwargs.setdefault('request_id', str(uuid.uuid1()))


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    post_swagger_local_valid.metadata = {'url': '/azurespecials/subscriptionId/swagger/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}

