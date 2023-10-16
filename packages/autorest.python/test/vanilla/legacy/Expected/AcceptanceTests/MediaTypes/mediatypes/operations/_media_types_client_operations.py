# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
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
from .._serialization import Serializer
from .._vendor import MediaTypesClientMixinABC, _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_analyze_body_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/mediatypes/analyze")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_analyze_body_no_accept_header_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = kwargs.pop("template_url", "/mediatypes/analyzeNoAccept")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_content_type_with_encoding_request(*, content: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/mediatypes/contentTypeWithEncoding")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, content=content, **kwargs)


def build_binary_body_with_two_content_types_request(  # pylint: disable=name-too-long
    *, content: IO, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "text/plain")

    # Construct URL
    _url = kwargs.pop("template_url", "/mediatypes/binaryBodyTwoContentTypes")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, content=content, **kwargs)


def build_binary_body_with_three_content_types_request(  # pylint: disable=name-too-long
    *, content: IO, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "text/plain")

    # Construct URL
    _url = kwargs.pop("template_url", "/mediatypes/binaryBodyThreeContentTypes")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, content=content, **kwargs)


def build_body_three_types_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "text/plain")

    # Construct URL
    _url = kwargs.pop("template_url", "/mediatypes/bodyThreeTypes")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_put_text_and_json_body_request(*, content: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "text/plain")

    # Construct URL
    _url = kwargs.pop("template_url", "/mediatypes/textAndJson")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, content=content, **kwargs)


class MediaTypesClientOperationsMixin(MediaTypesClientMixinABC):
    @overload
    def analyze_body(
        self, input: Optional[_models.SourcePath] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter. Default value is None.
        :type input: ~mediatypes.models.SourcePath
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def analyze_body(self, input: Optional[IO] = None, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter. Default value is None.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Known values are: 'application/json', 'application/pdf', 'image/jpeg', 'image/png',
         'image/tiff'. Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def analyze_body(self, input: Optional[Union[_models.SourcePath, IO]] = None, **kwargs: Any) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter. Is either a SourcePath type or a IO type. Default value is None.
        :type input: ~mediatypes.models.SourcePath or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
         'application/pdf', 'image/jpeg', 'image/png', 'image/tiff'. Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[str] = kwargs.pop("cls", None)

        _json = None
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            if input is not None:
                _json = self._serialize.body(input, "SourcePath")
            else:
                _json = None
            content_type = content_type or "application/json"

        request = build_analyze_body_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[_models.SourcePath] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter. Default value is None.
        :type input: ~mediatypes.models.SourcePath
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[IO] = None, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter. Default value is None.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Known values are: 'application/json', 'application/pdf', 'image/jpeg', 'image/png',
         'image/tiff'. Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[Union[_models.SourcePath, IO]] = None, **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter. Is either a SourcePath type or a IO type. Default value is None.
        :type input: ~mediatypes.models.SourcePath or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
         'application/pdf', 'image/jpeg', 'image/png', 'image/tiff'. Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _json = None
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            if input is not None:
                _json = self._serialize.body(input, "SourcePath")
            else:
                _json = None
            content_type = content_type or "application/json"

        request = build_analyze_body_no_accept_header_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def content_type_with_encoding(self, input: Optional[str] = None, **kwargs: Any) -> str:
        """Pass in contentType 'text/plain; charset=UTF-8' to pass test. Value for input does not matter.

        :param input: Input parameter. Default value is None.
        :type input: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[str] = kwargs.pop("cls", None)

        if input is not None:
            _content = self._serialize.body(input, "str")
        else:
            _content = None

        request = build_content_type_with_encoding_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def binary_body_with_two_content_types(self, message: IO, **kwargs: Any) -> str:
        """Binary body with two content types. Pass in of {'hello': 'world'} for the application/json
        content type, and a byte stream of 'hello, world!' for application/octet-stream.

        :param message: The payload body. Required.
        :type message: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
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
        cls: ClsType[str] = kwargs.pop("cls", None)

        _content = message

        request = build_binary_body_with_two_content_types_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def binary_body_with_three_content_types(self, message: IO, **kwargs: Any) -> str:
        """Binary body with three content types. Pass in string 'hello, world' with content type
        'text/plain', {'hello': world'} with content type 'application/json' and a byte string for
        'application/octet-stream'.

        :param message: The payload body. Required.
        :type message: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
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
        cls: ClsType[str] = kwargs.pop("cls", None)

        _content = message

        request = build_binary_body_with_three_content_types_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

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
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def body_three_types(self, message: IO, *, content_type: str = "application/octet-stream", **kwargs: Any) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Required.
        :type message: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Known values are: 'application/json', 'application/octet-stream', 'text/plain'. Default value
         is "application/octet-stream".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
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
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def body_three_types(self, message: Union[Any, IO, str], **kwargs: Any) -> str:
        """Body with three types. Can be stream, string, or JSON. Pass in string 'hello, world' with
        content type 'text/plain', {'hello': world'} with content type 'application/json' and a byte
        string for 'application/octet-stream'.

        :param message: The payload body. Is one of the following types: Any, IO, str Required.
        :type message: any or IO or str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json',
         'application/octet-stream', 'text/plain'. Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[str] = kwargs.pop("cls", None)

        _json = None
        _content = None
        if isinstance(message, (IOBase, bytes)):
            content_type = content_type or "application/octet-stream"
            _content = message
        else:
            _json = self._serialize.body(message, "object")
            content_type = content_type or "application/json"

        request = build_body_three_types_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def put_text_and_json_body(self, message: str, **kwargs: Any) -> str:
        """Body that's either text/plain or application/json.

        :param message: The payload body. Required.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
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
        cls: ClsType[str] = kwargs.pop("cls", None)

        _content = self._serialize.body(message, "str")

        request = build_put_text_and_json_body_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
