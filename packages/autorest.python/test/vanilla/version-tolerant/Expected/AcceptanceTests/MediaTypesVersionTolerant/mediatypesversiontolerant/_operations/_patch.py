# pyright: reportUnnecessaryTypeIgnoreComment=false
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List, Any, overload, IO, Optional, cast, Union, Tuple, Dict

from azure.core.exceptions import (
    ClientAuthenticationError,
    ResourceExistsError,
    ResourceNotFoundError,
    HttpResponseError,
    map_error,
)
from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict
from azure.core.tracing.decorator import distributed_trace
from azure.core.pipeline import PipelineResponse

from ._operations import _MediaTypesClientOperationsMixin as _MediaTypesClientOperationsMixinGen
from .._utils.serialization import Serializer

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_body_three_types_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "text/plain")

    # Construct URL

    _url = "/mediatypes/bodyThreeTypes"

    # Construct headers

    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class MediaTypesSharedMixin:
    def _prepare_body_three_types(
        self, message: Union[Any, IO, str], **kwargs: Any
    ) -> Tuple[HttpRequest, Dict[str, Any]]:
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        _json = None
        _content: Optional[Union[IO, str, bytes]] = None
        if isinstance(message, (IO, bytes)):
            content_type = content_type or "application/octet-stream"
            _content = message
        elif isinstance(message, str):
            content_type = content_type or "text/plain"
            _content = message
        else:
            _json = message
            content_type = content_type or "application/json"
        request = build_body_three_types_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore
        return request, kwargs

    @staticmethod
    def _handle_body_three_types_response(pipeline_response: PipelineResponse, error_map, cls):
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)
        if response.content:
            deserialized = response.json()
        else:
            deserialized = None
        if cls:
            return cls(pipeline_response, cast(str, deserialized), {})
        return cast(str, deserialized)


__all__: List[str] = [
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
