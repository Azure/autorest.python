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

from ._operations import MediaTypesClientOperationsMixin as _MediaTypesClientOperationsMixin
from .._serialization import Serializer

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
    def _handle_body_three_types_response(pipeline_response: PipelineResponse, cls=None, error_map={}):
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


class MediaTypesClientOperationsMixin(_MediaTypesClientOperationsMixin, MediaTypesSharedMixin):
    @overload
    def body_three_types(self, message: Any, *, content_type: str = "application/json", **kwargs: Any) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Required.
        :type message: any
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def body_three_types(  # type: ignore
        self, message: IO, *, content_type: str = "application/octet-stream", **kwargs: Any
    ) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Required.
        :type message: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Known values are: 'application/json', 'application/octet-stream', 'text/plain'. Default value
         is "application/octet-stream".
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def body_three_types(self, message: str, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Required.
        :type message: str
        :keyword content_type: Body Parameter content-type. Content type parameter for string body.
         Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def body_three_types(self, message: Union[Any, IO, str], **kwargs: Any) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Is one of the following types: any, IO, string Required.
        :type message: any or IO or str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
         'application/octet-stream', 'text/plain'. Default value is None.
        :paramtype content_type: str
        :return: str
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        cls = kwargs.pop("cls", None)
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})
        request, kwargs = self._prepare_body_three_types(message, **kwargs)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        return self._handle_body_three_types_response(pipeline_response, cls=cls, error_map=error_map)


__all__: List[str] = [
    "MediaTypesClientOperationsMixin"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
