# pylint: disable=line-too-long,useless-suppression
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

from ... import models as _models
from ..._operations._operations import (
    build_visibility_delete_model_request,
    build_visibility_get_model_request,
    build_visibility_head_model_request,
    build_visibility_patch_model_request,
    build_visibility_post_model_request,
    build_visibility_put_model_request,
    build_visibility_put_read_only_model_request,
)
from ..._utils.model_base import SdkJSONEncoder, _deserialize
from ..._utils.utils import ClientMixinABC
from .._configuration import VisibilityClientConfiguration

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class _VisibilityClientOperationsMixin(
    ClientMixinABC[AsyncPipelineClient[HttpRequest, AsyncHttpResponse], VisibilityClientConfiguration]
):

    @overload
    async def get_model(
        self, input: _models.VisibilityModel, *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_model(
        self, input: JSON, *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: JSON
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_model(
        self, input: IO[bytes], *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def get_model(
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], *, query_prop: int, **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.VisibilityModel
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
        cls: ClsType[_models.VisibilityModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_get_model_request(
            query_prop=query_prop,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.VisibilityModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def head_model(
        self, input: _models.VisibilityModel, *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def head_model(
        self, input: JSON, *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Required.
        :type input: JSON
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def head_model(
        self, input: IO[bytes], *, query_prop: int, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: bool
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def head_model(
        self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], *, query_prop: int, **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
        :keyword query_prop: Required int32, illustrating a query property. Required.
        :paramtype query_prop: int
        :return: bool
        :rtype: bool
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
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_head_model_request(
            query_prop=query_prop,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
        return 200 <= response.status_code <= 299

    @overload
    async def put_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """put_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """put_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put_model(self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any) -> None:
        """put_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
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
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_put_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def patch_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """patch_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """patch_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def patch_model(self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any) -> None:
        """patch_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
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
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_patch_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def post_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """post_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """post_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def post_model(self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any) -> None:
        """post_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
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
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_post_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def delete_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def delete_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """delete_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def delete_model(self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> None:
        """delete_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def delete_model(self, input: Union[_models.VisibilityModel, JSON, IO[bytes]], **kwargs: Any) -> None:
        """delete_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.VisibilityModel or JSON or IO[bytes]
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
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_delete_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def put_read_only_model(
        self, input: _models.ReadOnlyModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ReadOnlyModel:
        """put_read_only_model.

        :param input: Required.
        :type input: ~typetest.model.visibility.models.ReadOnlyModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ReadOnlyModel. The ReadOnlyModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.ReadOnlyModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_read_only_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ReadOnlyModel:
        """put_read_only_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ReadOnlyModel. The ReadOnlyModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.ReadOnlyModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_read_only_model(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ReadOnlyModel:
        """put_read_only_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ReadOnlyModel. The ReadOnlyModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.ReadOnlyModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put_read_only_model(
        self, input: Union[_models.ReadOnlyModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.ReadOnlyModel:
        """put_read_only_model.

        :param input: Is one of the following types: ReadOnlyModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.visibility.models.ReadOnlyModel or JSON or IO[bytes]
        :return: ReadOnlyModel. The ReadOnlyModel is compatible with MutableMapping
        :rtype: ~typetest.model.visibility.models.ReadOnlyModel
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
        cls: ClsType[_models.ReadOnlyModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_visibility_put_read_only_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ReadOnlyModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
