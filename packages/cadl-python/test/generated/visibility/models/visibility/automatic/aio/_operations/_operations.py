# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import (
    build_automatic_delete_model_request,
    build_automatic_get_model_request,
    build_automatic_head_model_request,
    build_automatic_patch_model_request,
    build_automatic_post_model_request,
    build_automatic_put_model_request,
)
from .._vendor import AutomaticClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutomaticClientOperationsMixin(AutomaticClientMixinABC):
    @overload
    async def get_model(
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~models.visibility.automatic.models.VisibilityModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~models.visibility.automatic.models.VisibilityModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def get_model(
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~models.visibility.automatic.models.VisibilityModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def get_model(
        self, input: Union[_models.VisibilityModel, JSON, IO], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.VisibilityModel:
        """get_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: VisibilityModel. The VisibilityModel is compatible with MutableMapping
        :rtype: ~models.visibility.automatic.models.VisibilityModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.VisibilityModel] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(input, (IO, bytes)):
            _content = input
            content_type = content_type or "application/json"
        elif isinstance(input, MutableMapping):
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for input")

        request = build_automatic_get_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
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
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: bool
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def head_model(self, input: JSON, *, content_type: str = "application/json", **kwargs: Any) -> bool:
        """head_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: bool
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def head_model(self, input: IO, *, content_type: str = "application/json", **kwargs: Any) -> bool:
        """head_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: bool
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def head_model(
        self, input: Union[_models.VisibilityModel, JSON, IO], *, content_type: str = "application/json", **kwargs: Any
    ) -> bool:
        """head_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: bool
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(input, (IO, bytes)):
            _content = input
            content_type = content_type or "application/json"
        elif isinstance(input, MutableMapping):
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for input")

        request = build_automatic_head_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
        return 200 <= response.status_code <= 299

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(input, (IO, bytes)):
            _content = input
            content_type = content_type or "application/json"
        elif isinstance(input, MutableMapping):
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for input")

        request = build_automatic_put_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    async def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def patch_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """patch_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(input, (IO, bytes)):
            _content = input
            content_type = content_type or "application/json"
        elif isinstance(input, MutableMapping):
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for input")

        request = build_automatic_patch_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    async def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def post_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """post_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(input, (IO, bytes)):
            _content = input
            content_type = content_type or "application/json"
        elif isinstance(input, MutableMapping):
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for input")

        request = build_automatic_post_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    async def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.VisibilityModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def delete_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.VisibilityModel, JSON, IO], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """delete_model.

        :param input: Is one of the following types: VisibilityModel, JSON, IO Required.
        :type input: ~models.visibility.automatic.models.VisibilityModel or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(input, (IO, bytes)):
            _content = input
            content_type = content_type or "application/json"
        elif isinstance(input, MutableMapping):
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for input")

        request = build_automatic_delete_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
