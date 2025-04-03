# pylint: disable=too-many-lines
# coding=utf-8
from io import IOBase
import json
import sys
from typing import Any, AsyncIterable, AsyncIterator, Callable, Dict, IO, List, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core import AsyncPipelineClient
from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize, _failsafe_deserialize
from ..._serialization import Deserializer, Serializer
from ...operations._operations import (
    build_extensions_resources_create_or_update_request,
    build_extensions_resources_delete_request,
    build_extensions_resources_get_request,
    build_extensions_resources_list_by_scope_request,
    build_extensions_resources_update_request,
    build_location_resources_create_or_update_request,
    build_location_resources_delete_request,
    build_location_resources_get_request,
    build_location_resources_list_by_location_request,
    build_location_resources_update_request,
    build_nested_create_or_replace_request,
    build_nested_delete_request,
    build_nested_get_request,
    build_nested_list_by_top_level_tracked_resource_request,
    build_nested_update_request,
    build_singleton_create_or_update_request,
    build_singleton_get_by_resource_group_request,
    build_singleton_list_by_resource_group_request,
    build_singleton_update_request,
    build_top_level_action_sync_request,
    build_top_level_create_or_replace_request,
    build_top_level_delete_request,
    build_top_level_get_request,
    build_top_level_list_by_resource_group_request,
    build_top_level_list_by_subscription_request,
    build_top_level_update_request,
)
from .._configuration import ResourcesClientConfiguration

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class TopLevelOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.resources.aio.ResourcesClient`'s
        :attr:`top_level` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: ResourcesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, top_level_tracked_resource_name: str, **kwargs: Any
    ) -> _models.TopLevelTrackedResource:
        """Get a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :return: TopLevelTrackedResource. The TopLevelTrackedResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.TopLevelTrackedResource
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

        cls: ClsType[_models.TopLevelTrackedResource] = kwargs.pop("cls", None)

        _request = build_top_level_get_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
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
            deserialized = _deserialize(_models.TopLevelTrackedResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_or_replace_initial(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        resource: Union[_models.TopLevelTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_top_level_create_or_replace_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
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

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 201:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create_or_replace(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        resource: _models.TopLevelTrackedResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.TopLevelTrackedResource]:
        """Create a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.resourcemanager.resources.models.TopLevelTrackedResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns TopLevelTrackedResource. The
         TopLevelTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_replace(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        resource: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.TopLevelTrackedResource]:
        """Create a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns TopLevelTrackedResource. The
         TopLevelTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_replace(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.TopLevelTrackedResource]:
        """Create a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns TopLevelTrackedResource. The
         TopLevelTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_replace(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        resource: Union[_models.TopLevelTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.TopLevelTrackedResource]:
        """Create a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param resource: Resource create parameters. Is one of the following types:
         TopLevelTrackedResource, JSON, IO[bytes] Required.
        :type resource: ~azure.resourcemanager.resources.models.TopLevelTrackedResource or JSON or
         IO[bytes]
        :return: An instance of AsyncLROPoller that returns TopLevelTrackedResource. The
         TopLevelTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.TopLevelTrackedResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_replace_initial(
                resource_group_name=resource_group_name,
                top_level_tracked_resource_name=top_level_tracked_resource_name,
                resource=resource,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.TopLevelTrackedResource, response.json())
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.TopLevelTrackedResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.TopLevelTrackedResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _update_initial(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        properties: Union[_models.TopLevelTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_top_level_update_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
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

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        properties: _models.TopLevelTrackedResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.TopLevelTrackedResource]:
        """Update a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: ~azure.resourcemanager.resources.models.TopLevelTrackedResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns TopLevelTrackedResource. The
         TopLevelTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        properties: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.TopLevelTrackedResource]:
        """Update a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns TopLevelTrackedResource. The
         TopLevelTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.TopLevelTrackedResource]:
        """Update a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns TopLevelTrackedResource. The
         TopLevelTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        properties: Union[_models.TopLevelTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.TopLevelTrackedResource]:
        """Update a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param properties: The resource properties to be updated. Is one of the following types:
         TopLevelTrackedResource, JSON, IO[bytes] Required.
        :type properties: ~azure.resourcemanager.resources.models.TopLevelTrackedResource or JSON or
         IO[bytes]
        :return: An instance of AsyncLROPoller that returns TopLevelTrackedResource. The
         TopLevelTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.TopLevelTrackedResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                top_level_tracked_resource_name=top_level_tracked_resource_name,
                properties=properties,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.TopLevelTrackedResource, response.json())
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.TopLevelTrackedResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.TopLevelTrackedResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _delete_initial(
        self, resource_group_name: str, top_level_tracked_resource_name: str, **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        _request = build_top_level_delete_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, top_level_tracked_resource_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete a TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :return: An instance of AsyncLROPoller that returns None
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                top_level_tracked_resource_name=top_level_tracked_resource_name,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.TopLevelTrackedResource"]:
        """List TopLevelTrackedResource resources by resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :return: An iterator like instance of TopLevelTrackedResource
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.TopLevelTrackedResource]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_top_level_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.TopLevelTrackedResource], deserialized.get("value", []))
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _failsafe_deserialize(_models.ErrorResponse, response.json())
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace
    def list_by_subscription(self, **kwargs: Any) -> AsyncIterable["_models.TopLevelTrackedResource"]:
        """List TopLevelTrackedResource resources by subscription ID.

        :return: An iterator like instance of TopLevelTrackedResource
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.resourcemanager.resources.models.TopLevelTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.TopLevelTrackedResource]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_top_level_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.TopLevelTrackedResource], deserialized.get("value", []))
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _failsafe_deserialize(_models.ErrorResponse, response.json())
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @overload
    async def action_sync(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        body: _models.NotificationDetails,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """A synchronous resource action that returns no content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param body: The content of the action request. Required.
        :type body: ~azure.resourcemanager.resources.models.NotificationDetails
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def action_sync(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        body: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """A synchronous resource action that returns no content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param body: The content of the action request. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def action_sync(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        body: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """A synchronous resource action that returns no content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param body: The content of the action request. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def action_sync(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        body: Union[_models.NotificationDetails, JSON, IO[bytes]],
        **kwargs: Any
    ) -> None:
        """A synchronous resource action that returns no content.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param body: The content of the action request. Is one of the following types:
         NotificationDetails, JSON, IO[bytes] Required.
        :type body: ~azure.resourcemanager.resources.models.NotificationDetails or JSON or IO[bytes]
        :return: None
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_top_level_action_sync_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
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

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class NestedOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.resources.aio.ResourcesClient`'s
        :attr:`nested` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: ResourcesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        **kwargs: Any
    ) -> _models.NestedProxyResource:
        """Get a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :return: NestedProxyResource. The NestedProxyResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.NestedProxyResource
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

        cls: ClsType[_models.NestedProxyResource] = kwargs.pop("cls", None)

        _request = build_nested_get_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
            nexted_proxy_resource_name=nexted_proxy_resource_name,
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
            deserialized = _deserialize(_models.NestedProxyResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_or_replace_initial(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        resource: Union[_models.NestedProxyResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_nested_create_or_replace_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
            nexted_proxy_resource_name=nexted_proxy_resource_name,
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

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 201:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create_or_replace(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        resource: _models.NestedProxyResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NestedProxyResource]:
        """Create a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.resourcemanager.resources.models.NestedProxyResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns NestedProxyResource. The
         NestedProxyResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_replace(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        resource: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NestedProxyResource]:
        """Create a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns NestedProxyResource. The
         NestedProxyResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_replace(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NestedProxyResource]:
        """Create a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns NestedProxyResource. The
         NestedProxyResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_replace(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        resource: Union[_models.NestedProxyResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NestedProxyResource]:
        """Create a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :param resource: Resource create parameters. Is one of the following types:
         NestedProxyResource, JSON, IO[bytes] Required.
        :type resource: ~azure.resourcemanager.resources.models.NestedProxyResource or JSON or
         IO[bytes]
        :return: An instance of AsyncLROPoller that returns NestedProxyResource. The
         NestedProxyResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.NestedProxyResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_replace_initial(
                resource_group_name=resource_group_name,
                top_level_tracked_resource_name=top_level_tracked_resource_name,
                nexted_proxy_resource_name=nexted_proxy_resource_name,
                resource=resource,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.NestedProxyResource, response.json())
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.NestedProxyResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.NestedProxyResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _update_initial(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        properties: Union[_models.NestedProxyResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_nested_update_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
            nexted_proxy_resource_name=nexted_proxy_resource_name,
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

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        properties: _models.NestedProxyResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NestedProxyResource]:
        """Update a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: ~azure.resourcemanager.resources.models.NestedProxyResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns NestedProxyResource. The
         NestedProxyResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        properties: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NestedProxyResource]:
        """Update a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns NestedProxyResource. The
         NestedProxyResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NestedProxyResource]:
        """Update a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns NestedProxyResource. The
         NestedProxyResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        properties: Union[_models.NestedProxyResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.NestedProxyResource]:
        """Update a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :param properties: The resource properties to be updated. Is one of the following types:
         NestedProxyResource, JSON, IO[bytes] Required.
        :type properties: ~azure.resourcemanager.resources.models.NestedProxyResource or JSON or
         IO[bytes]
        :return: An instance of AsyncLROPoller that returns NestedProxyResource. The
         NestedProxyResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.NestedProxyResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                top_level_tracked_resource_name=top_level_tracked_resource_name,
                nexted_proxy_resource_name=nexted_proxy_resource_name,
                properties=properties,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.NestedProxyResource, response.json())
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.NestedProxyResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.NestedProxyResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _delete_initial(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        _request = build_nested_delete_request(
            resource_group_name=resource_group_name,
            top_level_tracked_resource_name=top_level_tracked_resource_name,
            nexted_proxy_resource_name=nexted_proxy_resource_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self,
        resource_group_name: str,
        top_level_tracked_resource_name: str,
        nexted_proxy_resource_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Delete a NestedProxyResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :param nexted_proxy_resource_name: Name of the nested resource. Required.
        :type nexted_proxy_resource_name: str
        :return: An instance of AsyncLROPoller that returns None
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(
                resource_group_name=resource_group_name,
                top_level_tracked_resource_name=top_level_tracked_resource_name,
                nexted_proxy_resource_name=nexted_proxy_resource_name,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    @distributed_trace
    def list_by_top_level_tracked_resource(
        self, resource_group_name: str, top_level_tracked_resource_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.NestedProxyResource"]:
        """List NestedProxyResource resources by TopLevelTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param top_level_tracked_resource_name: arm resource name for path. Required.
        :type top_level_tracked_resource_name: str
        :return: An iterator like instance of NestedProxyResource
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.resourcemanager.resources.models.NestedProxyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.NestedProxyResource]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_nested_list_by_top_level_tracked_resource_request(
                    resource_group_name=resource_group_name,
                    top_level_tracked_resource_name=top_level_tracked_resource_name,
                    subscription_id=self._config.subscription_id,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.NestedProxyResource], deserialized.get("value", []))
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _failsafe_deserialize(_models.ErrorResponse, response.json())
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)


class SingletonOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.resources.aio.ResourcesClient`'s
        :attr:`singleton` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: ResourcesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_by_resource_group(self, resource_group_name: str, **kwargs: Any) -> _models.SingletonTrackedResource:
        """Get a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :return: SingletonTrackedResource. The SingletonTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.SingletonTrackedResource
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

        cls: ClsType[_models.SingletonTrackedResource] = kwargs.pop("cls", None)

        _request = build_singleton_get_by_resource_group_request(
            resource_group_name=resource_group_name,
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
            deserialized = _deserialize(_models.SingletonTrackedResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        resource: Union[_models.SingletonTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_singleton_create_or_update_request(
            resource_group_name=resource_group_name,
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

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 201:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        resource: _models.SingletonTrackedResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SingletonTrackedResource]:
        """Create a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.resourcemanager.resources.models.SingletonTrackedResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SingletonTrackedResource. The
         SingletonTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.SingletonTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self, resource_group_name: str, resource: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.SingletonTrackedResource]:
        """Create a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource: Resource create parameters. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SingletonTrackedResource. The
         SingletonTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.SingletonTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self, resource_group_name: str, resource: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.SingletonTrackedResource]:
        """Create a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns SingletonTrackedResource. The
         SingletonTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.SingletonTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        resource: Union[_models.SingletonTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SingletonTrackedResource]:
        """Create a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource: Resource create parameters. Is one of the following types:
         SingletonTrackedResource, JSON, IO[bytes] Required.
        :type resource: ~azure.resourcemanager.resources.models.SingletonTrackedResource or JSON or
         IO[bytes]
        :return: An instance of AsyncLROPoller that returns SingletonTrackedResource. The
         SingletonTrackedResource is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.SingletonTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SingletonTrackedResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                resource=resource,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.SingletonTrackedResource, response.json())
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.SingletonTrackedResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.SingletonTrackedResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @overload
    async def update(
        self,
        resource_group_name: str,
        properties: _models.SingletonTrackedResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SingletonTrackedResource:
        """Update a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: ~azure.resourcemanager.resources.models.SingletonTrackedResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SingletonTrackedResource. The SingletonTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.SingletonTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, resource_group_name: str, properties: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.SingletonTrackedResource:
        """Update a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SingletonTrackedResource. The SingletonTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.SingletonTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self, resource_group_name: str, properties: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.SingletonTrackedResource:
        """Update a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: SingletonTrackedResource. The SingletonTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.SingletonTrackedResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        properties: Union[_models.SingletonTrackedResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.SingletonTrackedResource:
        """Update a SingletonTrackedResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param properties: The resource properties to be updated. Is one of the following types:
         SingletonTrackedResource, JSON, IO[bytes] Required.
        :type properties: ~azure.resourcemanager.resources.models.SingletonTrackedResource or JSON or
         IO[bytes]
        :return: SingletonTrackedResource. The SingletonTrackedResource is compatible with
         MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.SingletonTrackedResource
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
        cls: ClsType[_models.SingletonTrackedResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_singleton_update_request(
            resource_group_name=resource_group_name,
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
            deserialized = _deserialize(_models.SingletonTrackedResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.SingletonTrackedResource"]:
        """List SingletonTrackedResource resources by resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :return: An iterator like instance of SingletonTrackedResource
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.resourcemanager.resources.models.SingletonTrackedResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.SingletonTrackedResource]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_singleton_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.SingletonTrackedResource], deserialized.get("value", []))
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _failsafe_deserialize(_models.ErrorResponse, response.json())
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)


class ExtensionsResourcesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.resources.aio.ResourcesClient`'s
        :attr:`extensions_resources` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: ResourcesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, resource_uri: str, extensions_resource_name: str, **kwargs: Any) -> _models.ExtensionsResource:
        """Get a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :return: ExtensionsResource. The ExtensionsResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.ExtensionsResource
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

        cls: ClsType[_models.ExtensionsResource] = kwargs.pop("cls", None)

        _request = build_extensions_resources_get_request(
            resource_uri=resource_uri,
            extensions_resource_name=extensions_resource_name,
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
            deserialized = _deserialize(_models.ExtensionsResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_or_update_initial(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        resource: Union[_models.ExtensionsResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncIterator[bytes]:
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
        cls: ClsType[AsyncIterator[bytes]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_extensions_resources_create_or_update_request(
            resource_uri=resource_uri,
            extensions_resource_name=extensions_resource_name,
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

        _stream = True
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            try:
                await response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 201:
            response_headers["Azure-AsyncOperation"] = self._deserialize(
                "str", response.headers.get("Azure-AsyncOperation")
            )
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        deserialized = response.iter_bytes()

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create_or_update(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        resource: _models.ExtensionsResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ExtensionsResource]:
        """Create a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.resourcemanager.resources.models.ExtensionsResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns ExtensionsResource. The ExtensionsResource
         is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.ExtensionsResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        resource: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ExtensionsResource]:
        """Create a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns ExtensionsResource. The ExtensionsResource
         is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.ExtensionsResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ExtensionsResource]:
        """Create a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns ExtensionsResource. The ExtensionsResource
         is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.ExtensionsResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        resource: Union[_models.ExtensionsResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.ExtensionsResource]:
        """Create a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :param resource: Resource create parameters. Is one of the following types: ExtensionsResource,
         JSON, IO[bytes] Required.
        :type resource: ~azure.resourcemanager.resources.models.ExtensionsResource or JSON or IO[bytes]
        :return: An instance of AsyncLROPoller that returns ExtensionsResource. The ExtensionsResource
         is compatible with MutableMapping
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.resourcemanager.resources.models.ExtensionsResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ExtensionsResource] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_uri=resource_uri,
                extensions_resource_name=extensions_resource_name,
                resource=resource,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.ExtensionsResource, response.json())
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.ExtensionsResource].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.ExtensionsResource](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @overload
    async def update(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        properties: _models.ExtensionsResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExtensionsResource:
        """Update a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: ~azure.resourcemanager.resources.models.ExtensionsResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExtensionsResource. The ExtensionsResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.ExtensionsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        properties: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExtensionsResource:
        """Update a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExtensionsResource. The ExtensionsResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.ExtensionsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ExtensionsResource:
        """Update a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ExtensionsResource. The ExtensionsResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.ExtensionsResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_uri: str,
        extensions_resource_name: str,
        properties: Union[_models.ExtensionsResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.ExtensionsResource:
        """Update a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :param properties: The resource properties to be updated. Is one of the following types:
         ExtensionsResource, JSON, IO[bytes] Required.
        :type properties: ~azure.resourcemanager.resources.models.ExtensionsResource or JSON or
         IO[bytes]
        :return: ExtensionsResource. The ExtensionsResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.ExtensionsResource
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
        cls: ClsType[_models.ExtensionsResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_extensions_resources_update_request(
            resource_uri=resource_uri,
            extensions_resource_name=extensions_resource_name,
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
            deserialized = _deserialize(_models.ExtensionsResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(self, resource_uri: str, extensions_resource_name: str, **kwargs: Any) -> None:
        """Delete a ExtensionsResource.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :param extensions_resource_name: The name of the ExtensionsResource. Required.
        :type extensions_resource_name: str
        :return: None
        :rtype: None
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

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_extensions_resources_delete_request(
            resource_uri=resource_uri,
            extensions_resource_name=extensions_resource_name,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def list_by_scope(self, resource_uri: str, **kwargs: Any) -> AsyncIterable["_models.ExtensionsResource"]:
        """List ExtensionsResource resources by parent.

        :param resource_uri: The fully qualified Azure Resource manager identifier of the resource.
         Required.
        :type resource_uri: str
        :return: An iterator like instance of ExtensionsResource
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.resourcemanager.resources.models.ExtensionsResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.ExtensionsResource]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_extensions_resources_list_by_scope_request(
                    resource_uri=resource_uri,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.ExtensionsResource], deserialized.get("value", []))
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _failsafe_deserialize(_models.ErrorResponse, response.json())
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)


class LocationResourcesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.resources.aio.ResourcesClient`'s
        :attr:`location_resources` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: ResourcesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(self, location: str, location_resource_name: str, **kwargs: Any) -> _models.LocationResource:
        """Get a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
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

        cls: ClsType[_models.LocationResource] = kwargs.pop("cls", None)

        _request = build_location_resources_get_request(
            location=location,
            location_resource_name=location_resource_name,
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
            deserialized = _deserialize(_models.LocationResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_update(
        self,
        location: str,
        location_resource_name: str,
        resource: _models.LocationResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LocationResource:
        """Create a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.resourcemanager.resources.models.LocationResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        location: str,
        location_resource_name: str,
        resource: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LocationResource:
        """Create a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        location: str,
        location_resource_name: str,
        resource: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LocationResource:
        """Create a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        location: str,
        location_resource_name: str,
        resource: Union[_models.LocationResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.LocationResource:
        """Create a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :param resource: Resource create parameters. Is one of the following types: LocationResource,
         JSON, IO[bytes] Required.
        :type resource: ~azure.resourcemanager.resources.models.LocationResource or JSON or IO[bytes]
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
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
        cls: ClsType[_models.LocationResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _content = json.dumps(resource, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_location_resources_create_or_update_request(
            location=location,
            location_resource_name=location_resource_name,
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
            deserialized = _deserialize(_models.LocationResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        location: str,
        location_resource_name: str,
        properties: _models.LocationResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LocationResource:
        """Update a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: ~azure.resourcemanager.resources.models.LocationResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        location: str,
        location_resource_name: str,
        properties: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LocationResource:
        """Update a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        location: str,
        location_resource_name: str,
        properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.LocationResource:
        """Update a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        location: str,
        location_resource_name: str,
        properties: Union[_models.LocationResource, JSON, IO[bytes]],
        **kwargs: Any
    ) -> _models.LocationResource:
        """Update a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :param properties: The resource properties to be updated. Is one of the following types:
         LocationResource, JSON, IO[bytes] Required.
        :type properties: ~azure.resourcemanager.resources.models.LocationResource or JSON or IO[bytes]
        :return: LocationResource. The LocationResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.resources.models.LocationResource
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
        cls: ClsType[_models.LocationResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _content = json.dumps(properties, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_location_resources_update_request(
            location=location,
            location_resource_name=location_resource_name,
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
            deserialized = _deserialize(_models.LocationResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(self, location: str, location_resource_name: str, **kwargs: Any) -> None:
        """Delete a LocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param location_resource_name: The name of the LocationResource. Required.
        :type location_resource_name: str
        :return: None
        :rtype: None
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

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_location_resources_delete_request(
            location=location,
            location_resource_name=location_resource_name,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def list_by_location(self, location: str, **kwargs: Any) -> AsyncIterable["_models.LocationResource"]:
        """List LocationResource resources by SubscriptionLocationResource.

        :param location: The name of the Azure region. Required.
        :type location: str
        :return: An iterator like instance of LocationResource
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.resourcemanager.resources.models.LocationResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[List[_models.LocationResource]] = kwargs.pop("cls", None)

        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_location_resources_list_by_location_request(
                    location=location,
                    subscription_id=self._config.subscription_id,
                    api_version=self._config.api_version,
                    headers=_headers,
                    params=_params,
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                path_format_arguments = {
                    "endpoint": self._serialize.url(
                        "self._config.base_url", self._config.base_url, "str", skip_quote=True
                    ),
                }
                _request.url = self._client.format_url(_request.url, **path_format_arguments)

            return _request

        async def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.LocationResource], deserialized.get("value", []))
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = _failsafe_deserialize(_models.ErrorResponse, response.json())
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)
