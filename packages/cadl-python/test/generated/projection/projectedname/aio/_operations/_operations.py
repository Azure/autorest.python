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
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder
from ..._operations._operations import (
    build_projected_name_client_projection_request,
    build_projected_name_json_projection_request,
    build_projected_name_language_projection_request,
)
from .._vendor import ProjectedNameClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ProjectedNameClientOperationsMixin(ProjectedNameClientMixinABC):
    @overload
    async def json_projection(  # pylint: disable=inconsistent-return-statements
        self, body: _models.Project, **kwargs: Any
    ) -> None:
        """json_projection.

        :param body: Required.
        :type body: ~projectedname.models.Project
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
    async def json_projection(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """json_projection.

        :param body: Required.
        :type body: JSON
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
    async def json_projection(self, body: IO, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """json_projection.

        :param body: Required.
        :type body: IO
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
    async def json_projection(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.Project, JSON, IO], **kwargs: Any
    ) -> None:
        """json_projection.

        :param body: Is one of the following types: Project, JSON, IO Required.
        :type body: ~projectedname.models.Project or JSON or IO
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(body, (IO, bytes)):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        elif isinstance(body, MutableMapping):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        elif isinstance(body, _model_base.Model):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for body")

        request = build_projected_name_json_projection_request(
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
    async def client_projection(  # pylint: disable=inconsistent-return-statements
        self, body: _models.Project, **kwargs: Any
    ) -> None:
        """client_projection.

        :param body: Required.
        :type body: ~projectedname.models.Project
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
    async def client_projection(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """client_projection.

        :param body: Required.
        :type body: JSON
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
    async def client_projection(  # pylint: disable=inconsistent-return-statements
        self, body: IO, **kwargs: Any
    ) -> None:
        """client_projection.

        :param body: Required.
        :type body: IO
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
    async def client_projection(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.Project, JSON, IO], **kwargs: Any
    ) -> None:
        """client_projection.

        :param body: Is one of the following types: Project, JSON, IO Required.
        :type body: ~projectedname.models.Project or JSON or IO
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(body, (IO, bytes)):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        elif isinstance(body, MutableMapping):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        elif isinstance(body, _model_base.Model):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for body")

        request = build_projected_name_client_projection_request(
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
    async def language_projection(  # pylint: disable=inconsistent-return-statements
        self, body: _models.Project, **kwargs: Any
    ) -> None:
        """language_projection.

        :param body: Required.
        :type body: ~projectedname.models.Project
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
    async def language_projection(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, **kwargs: Any
    ) -> None:
        """language_projection.

        :param body: Required.
        :type body: JSON
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
    async def language_projection(  # pylint: disable=inconsistent-return-statements
        self, body: IO, **kwargs: Any
    ) -> None:
        """language_projection.

        :param body: Required.
        :type body: IO
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
    async def language_projection(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.Project, JSON, IO], **kwargs: Any
    ) -> None:
        """language_projection.

        :param body: Is one of the following types: Project, JSON, IO Required.
        :type body: ~projectedname.models.Project or JSON or IO
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content: Any = None
        if isinstance(body, (IO, bytes)):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        elif isinstance(body, MutableMapping):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        elif isinstance(body, _model_base.Model):
            _content = json.dumps(body, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for body")

        request = build_projected_name_language_projection_request(
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
