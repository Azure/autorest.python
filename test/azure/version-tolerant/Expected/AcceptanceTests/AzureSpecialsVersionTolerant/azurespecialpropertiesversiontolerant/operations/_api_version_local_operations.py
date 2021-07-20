# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from ..rest import api_version_local as rest_api_version_local

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class ApiVersionLocalOperations(object):
    """ApiVersionLocalOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_method_local_valid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_api_version_local.build_get_method_local_valid_request(
            template_url=self.get_method_local_valid.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_method_local_valid.metadata = {"url": "/azurespecials/apiVersion/method/string/none/query/local/2.0"}  # type: ignore

    @distributed_trace
    def get_method_local_null(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with api-version modeled in the method.  pass in api-version = null to succeed.

        :keyword api_version: This should appear as a method parameter, use value null, this should
         result in no serialized parameter.
        :paramtype api_version: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        api_version = kwargs.pop("api_version", None)  # type: Optional[str]

        request = rest_api_version_local.build_get_method_local_null_request(
            api_version=api_version,
            template_url=self.get_method_local_null.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_method_local_null.metadata = {"url": "/azurespecials/apiVersion/method/string/none/query/local/null"}  # type: ignore

    @distributed_trace
    def get_path_local_valid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_api_version_local.build_get_path_local_valid_request(
            template_url=self.get_path_local_valid.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_path_local_valid.metadata = {"url": "/azurespecials/apiVersion/path/string/none/query/local/2.0"}  # type: ignore

    @distributed_trace
    def get_swagger_local_valid(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = rest_api_version_local.build_get_swagger_local_valid_request(
            template_url=self.get_swagger_local_valid.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_swagger_local_valid.metadata = {"url": "/azurespecials/apiVersion/swagger/string/none/query/local/2.0"}  # type: ignore
