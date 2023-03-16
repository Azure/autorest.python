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
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import AzureJSONEncoder
from .._serialization import Serializer
from .._vendor import OverloadClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_overload_upload_bytes_or_string_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
    # Construct URL
    _url = "/overload/bytesOrString"

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_overload_upload_json_or_string_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
    # Construct URL
    _url = "/overload/JsonOrString"

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class OverloadClientOperationsMixin(OverloadClientMixinABC):
    @overload
    def upload_bytes_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: str, *, content_type: str = "text/plain", **kwargs: Any
    ) -> None:
        """upload_bytes_or_string.

        :param data: Required.
        :type data: str
        :keyword content_type: Default value is "text/plain".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def upload_bytes_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: bytes, *, content_type: str = "application/octet-stream", **kwargs: Any
    ) -> None:
        """upload_bytes_or_string.

        :param data: Required.
        :type data: bytes
        :keyword content_type: Default value is "application/octet-stream".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def upload_bytes_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: IO, *, content_type: str = "application/octet-stream", **kwargs: Any
    ) -> None:
        """upload_bytes_or_string.

        :param data: Required.
        :type data: IO
        :keyword content_type: Default value is "application/octet-stream".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def upload_bytes_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: Union[str, bytes, IO], **kwargs: Any
    ) -> None:
        """upload_bytes_or_string.

        :param data: Is one of the following types: str, bytes, IO Required.
        :type data: str or bytes or IO
        :keyword content_type: Known values are: "text/plain" and "application/octet-stream". Default
         value is None.
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = None
        if isinstance(data, (IO, bytes)):
            _content = data
            content_type = content_type or "application/octet-stream"
        else:
            _content = data
            content_type = content_type or "text/plain"

        request = build_overload_upload_bytes_or_string_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    def upload_json_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: str, *, content_type: str = "text/plain", **kwargs: Any
    ) -> None:
        """upload_json_or_string.

        :param data: Required.
        :type data: str
        :keyword content_type: Default value is "text/plain".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def upload_json_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: _models.Data, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """upload_json_or_string.

        :param data: Required.
        :type data: ~overload.models.Data
        :keyword content_type: Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def upload_json_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """upload_json_or_string.

        :param data: Required.
        :type data: IO
        :keyword content_type: Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def upload_json_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """upload_json_or_string.

        :param data: Required.
        :type data: JSON
        :keyword content_type: Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def upload_json_or_string(  # pylint: disable=inconsistent-return-statements
        self, data: Union[str, _models.Data, JSON, IO], **kwargs: Any
    ) -> None:
        """upload_json_or_string.

        :param data: Is one of the following types: str, Data, JSON, IO Required.
        :type data: str or ~overload.models.Data or JSON or IO
        :keyword content_type: Known values are: "text/plain" and "application/json". Default value is
         None.
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = None
        if isinstance(data, (IO, bytes)):
            _content = data
            content_type = content_type or "application/json"
        elif isinstance(data, str):
            _content = data
            content_type = content_type or "text/plain"
        else:
            _content = json.dumps(data, cls=AzureJSONEncoder)  # type: ignore
            content_type = content_type or "application/json"

        request = build_overload_upload_json_or_string_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
