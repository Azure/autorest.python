# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
from io import IOBase
import json
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core import AsyncPipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._utils.model_base import SdkJSONEncoder, _deserialize, _failsafe_deserialize
from ..._utils.serialization import Deserializer, Serializer
from ...operations._operations import (
    build_error_create_for_user_defined_error_request,
    build_error_get_for_predefined_error_request,
    build_managed_identity_create_with_system_assigned_request,
    build_managed_identity_get_request,
    build_managed_identity_update_with_user_assigned_and_system_assigned_request,
)
from .._configuration import CommonPropertiesClientConfiguration

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ManagedIdentityOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.commonproperties.aio.CommonPropertiesClient`'s
        :attr:`managed_identity` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: CommonPropertiesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, managed_identity_tracked_resource_name: str, **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Get a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ManagedIdentityTrackedResource] = kwargs.pop("cls", None)

        _request = build_managed_identity_get_request(
            resource_group_name=resource_group_name,
            managed_identity_tracked_resource_name=managed_identity_tracked_resource_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ManagedIdentityTrackedResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_with_system_assigned(
        self,
        resource_group_name: str,
        managed_identity_tracked_resource_name: str,
        resource: _models.ManagedIdentityTrackedResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Create a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_with_system_assigned(
        self,
        resource_group_name: str,
        managed_identity_tracked_resource_name: str,
        resource: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Create a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_with_system_assigned(
        self,
        resource_group_name: str,
        managed_identity_tracked_resource_name: str,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Create a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_with_system_assigned(
        self,
        resource_group_name: str,
        managed_identity_tracked_resource_name: str,
        resource: Union[_models.ManagedIdentityTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Create a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :param resource: Resource create parameters. Is one of the following types:
         ManagedIdentityTrackedResource, JSON, IO[bytes] Required.
        :type resource: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
         or JSON or IO[bytes]
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ManagedIdentityTrackedResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_managed_identity_create_with_system_assigned_request(
            resource_group_name=resource_group_name,
            managed_identity_tracked_resource_name=managed_identity_tracked_resource_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ManagedIdentityTrackedResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update_with_user_assigned_and_system_assigned(  # pylint: disable=name-too-long
        self,
        resource_group_name: str,
        managed_identity_tracked_resource_name: str,
        properties: _models.ManagedIdentityTrackedResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Update a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update_with_user_assigned_and_system_assigned(  # pylint: disable=name-too-long
        self,
        resource_group_name: str,
        managed_identity_tracked_resource_name: str,
        properties: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Update a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update_with_user_assigned_and_system_assigned(  # pylint: disable=name-too-long
        self,
        resource_group_name: str,
        managed_identity_tracked_resource_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Update a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update_with_user_assigned_and_system_assigned(  # pylint: disable=name-too-long
        self,
        resource_group_name: str,
        managed_identity_tracked_resource_name: str,
        properties: Union[_models.ManagedIdentityTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.ManagedIdentityTrackedResource:
        """Update a ManagedIdentityTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param managed_identity_tracked_resource_name: arm resource name for path. Required.
        :type managed_identity_tracked_resource_name: str
        :param properties: The resource properties to be updated. Is one of the following types:
         ManagedIdentityTrackedResource, JSON, IO[bytes] Required.
        :type properties: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
         or JSON or IO[bytes]
        :return: ManagedIdentityTrackedResource. The ManagedIdentityTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ManagedIdentityTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ManagedIdentityTrackedResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_managed_identity_update_with_user_assigned_and_system_assigned_request(
            resource_group_name=resource_group_name,
            managed_identity_tracked_resource_name=managed_identity_tracked_resource_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ManagedIdentityTrackedResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore


class ErrorOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.commonproperties.aio.CommonPropertiesClient`'s
        :attr:`error` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: CommonPropertiesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_for_predefined_error(
        self, resource_group_name: str, confidential_resource_name: str, **kwargs: Any
    ) -> _models.ConfidentialResource:
        """Get a ConfidentialResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param confidential_resource_name: The name of the ConfidentialResource. Required.
        :type confidential_resource_name: str
        :return: ConfidentialResource. The ConfidentialResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ConfidentialResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.ConfidentialResource] = kwargs.pop("cls", None)

        _request = build_error_get_for_predefined_error_request(
            resource_group_name=resource_group_name,
            confidential_resource_name=confidential_resource_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ConfidentialResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_for_user_defined_error(
        self,
        resource_group_name: str,
        confidential_resource_name: str,
        resource: _models.ConfidentialResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConfidentialResource:
        """Create a ConfidentialResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param confidential_resource_name: The name of the ConfidentialResource. Required.
        :type confidential_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.resourcemanager.commonproperties.models.ConfidentialResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ConfidentialResource. The ConfidentialResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ConfidentialResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_for_user_defined_error(
        self,
        resource_group_name: str,
        confidential_resource_name: str,
        resource: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConfidentialResource:
        """Create a ConfidentialResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param confidential_resource_name: The name of the ConfidentialResource. Required.
        :type confidential_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ConfidentialResource. The ConfidentialResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ConfidentialResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_for_user_defined_error(
        self,
        resource_group_name: str,
        confidential_resource_name: str,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConfidentialResource:
        """Create a ConfidentialResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param confidential_resource_name: The name of the ConfidentialResource. Required.
        :type confidential_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ConfidentialResource. The ConfidentialResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ConfidentialResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_for_user_defined_error(
        self,
        resource_group_name: str,
        confidential_resource_name: str,
        resource: Union[_models.ConfidentialResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.ConfidentialResource:
        """Create a ConfidentialResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param confidential_resource_name: The name of the ConfidentialResource. Required.
        :type confidential_resource_name: str
        :param resource: Resource create parameters. Is one of the following types:
         ConfidentialResource, JSON, IO[bytes] Required.
        :type resource: ~azure.resourcemanager.commonproperties.models.ConfidentialResource or JSON or
         IO[bytes]
        :return: ConfidentialResource. The ConfidentialResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.commonproperties.models.ConfidentialResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConfidentialResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_error_create_for_user_defined_error_request(
            resource_group_name=resource_group_name,
            confidential_resource_name=confidential_resource_name,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.CloudError, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ConfidentialResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
