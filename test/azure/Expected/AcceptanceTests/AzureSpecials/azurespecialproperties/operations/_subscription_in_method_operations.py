# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SubscriptionInMethodOperations(object):
    """SubscriptionInMethodOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azurespecialproperties.models
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

    @distributed_trace
    def post_method_local_valid(
        self,
        subscription_id,  # type: str
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id = '1234-5678-9012-3456' to succeed.

        :param subscription_id: This should appear as a method parameter, use value
         '1234-5678-9012-3456'.
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


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    post_method_local_valid.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}

    @distributed_trace
    def post_method_local_null(
        self,
        subscription_id,  # type: str
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id = null, client-side validation should prevent you from making this call.

        :param subscription_id: This should appear as a method parameter, use value
         '1234-5678-9012-3456'.
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


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    post_method_local_null.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/local/null/{subscriptionId}'}

    @distributed_trace
    def post_path_local_valid(
        self,
        subscription_id,  # type: str
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id = '1234-5678-9012-3456' to succeed.

        :param subscription_id: This should appear as a method parameter, use value
         '1234-5678-9012-3456'.
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


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    post_path_local_valid.metadata = {'url': '/azurespecials/subscriptionId/path/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}

    @distributed_trace
    def post_swagger_local_valid(
        self,
        subscription_id,  # type: str
        cls=None,  # type: ClsType[None]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in the method.  pass in subscription id = '1234-5678-9012-3456' to succeed.

        :param subscription_id: This should appear as a method parameter, use value
         '1234-5678-9012-3456'.
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


        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    post_swagger_local_valid.metadata = {'url': '/azurespecials/subscriptionId/swagger/string/none/path/local/1234-5678-9012-3456/{subscriptionId}'}
