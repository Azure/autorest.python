# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SubscriptionInCredentialsOperations(object):
    """SubscriptionInCredentialsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

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
    def post_method_global_valid(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
        '1234-5678-9012-3456' to succeed.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.post_method_global_valid.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_method_global_valid.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/global/1234-5678-9012-3456/{subscriptionId}'}  # type: ignore

    @distributed_trace
    def post_method_global_null(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
        null, and client-side validation should prevent you from making this call.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.post_method_global_null.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_method_global_null.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/global/null/{subscriptionId}'}  # type: ignore

    @distributed_trace
    def post_method_global_not_provided_valid(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
        '1234-5678-9012-3456' to succeed.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2015-07-01-preview"
        accept = "application/json"

        # Construct URL
        url = self.post_method_global_not_provided_valid.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_method_global_not_provided_valid.metadata = {'url': '/azurespecials/subscriptionId/method/string/none/path/globalNotProvided/1234-5678-9012-3456/{subscriptionId}'}  # type: ignore

    @distributed_trace
    def post_path_global_valid(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
        '1234-5678-9012-3456' to succeed.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.post_path_global_valid.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_path_global_valid.metadata = {'url': '/azurespecials/subscriptionId/path/string/none/path/global/1234-5678-9012-3456/{subscriptionId}'}  # type: ignore

    @distributed_trace
    def post_swagger_global_valid(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """POST method with subscriptionId modeled in credentials.  Set the credential subscriptionId to
        '1234-5678-9012-3456' to succeed.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.post_swagger_global_valid.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    post_swagger_global_valid.metadata = {'url': '/azurespecials/subscriptionId/swagger/string/none/path/global/1234-5678-9012-3456/{subscriptionId}'}  # type: ignore
