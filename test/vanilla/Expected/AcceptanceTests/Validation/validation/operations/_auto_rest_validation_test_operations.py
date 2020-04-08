# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models

try:
    from typing import TYPE_CHECKING
except:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    # pylint: disable=unused-import
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class AutoRestValidationTestOperationsMixin(object):

    @distributed_trace
    def validation_of_method_parameters(
        self,
        resource_group_name,  # type: str
        id,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Product"
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Product"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "1.0.0"

        # Construct URL
        url = self.validation_of_method_parameters.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'id': self._serialize.url("id", id, 'int', maximum=1000, minimum=100, multiple=10),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['apiVersion'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('Product', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    validation_of_method_parameters.metadata = {'url': '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'}

    @distributed_trace
    def validation_of_body(
        self,
        resource_group_name,  # type: str
        id,  # type: int
        body=None,  # type: Optional["models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Product"
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param body:
        :type body: ~validation.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Product"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "1.0.0"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.validation_of_body.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9]+'),
            'id': self._serialize.url("id", id, 'int', maximum=1000, minimum=100, multiple=10),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['apiVersion'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('Product', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    validation_of_body.metadata = {'url': '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'}

    @distributed_trace
    def get_with_constant_in_path(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """get_with_constant_in_path.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        constant_param = "constant"

        # Construct URL
        url = self.get_with_constant_in_path.metadata['url']
        path_format_arguments = {
            'constantParam': self._serialize.url("constant_param", constant_param, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
          return cls(pipeline_response, None, {})

    get_with_constant_in_path.metadata = {'url': '/validation/constantsInPath/{constantParam}/value'}

    @distributed_trace
    def post_with_constant_in_body(
        self,
        body=None,  # type: Optional["models.Product"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Product"
        """post_with_constant_in_body.

        :param body:
        :type body: ~validation.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Product or the result of cls(response)
        :rtype: ~validation.models.Product
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Product"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        constant_param = "constant"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.post_with_constant_in_body.metadata['url']
        path_format_arguments = {
            'constantParam': self._serialize.url("constant_param", constant_param, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        if body is not None:
            body_content = self._serialize.body(body, 'Product')
        else:
            body_content = None
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('Product', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    post_with_constant_in_body.metadata = {'url': '/validation/constantsInPath/{constantParam}/value'}
