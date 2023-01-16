# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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
from ..._vendor import _convert_request
from ...operations._media_types_client_operations import (
    build_analyze_body_no_accept_header_request,
    build_analyze_body_request,
    build_binary_body_with_three_content_types_request,
    build_binary_body_with_two_content_types_request,
    build_body_three_types_request,
    build_content_type_with_encoding_request,
    build_put_text_and_json_body_request,
)
from .._vendor import MediaTypesClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MediaTypesClientOperationsMixin(MediaTypesClientMixinABC):
    @overload
    async def analyze_body(
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
    async def analyze_body(
        self, input: Optional[IO] = None, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> str:
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

    @distributed_trace_async
    async def analyze_body(self, input: Optional[Union[_models.SourcePath, IO]] = None, **kwargs: Any) -> str:
        """Analyze body, that could be different media types.

        :param input: Input parameter. Is either a model type or a IO type. Default value is None.
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
        if isinstance(input, (IO, bytes)):
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
            template_url=self.analyze_body.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    analyze_body.metadata = {"url": "/mediatypes/analyze"}

    @overload
    async def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
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
    async def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
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

    @distributed_trace_async
    async def analyze_body_no_accept_header(  # pylint: disable=inconsistent-return-statements
        self, input: Optional[Union[_models.SourcePath, IO]] = None, **kwargs: Any
    ) -> None:
        """Analyze body, that could be different media types. Adds to AnalyzeBody by not having an accept
        type.

        :param input: Input parameter. Is either a model type or a IO type. Default value is None.
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
        if isinstance(input, (IO, bytes)):
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
            template_url=self.analyze_body_no_accept_header.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    analyze_body_no_accept_header.metadata = {"url": "/mediatypes/analyzeNoAccept"}

    @distributed_trace_async
    async def content_type_with_encoding(self, input: Optional[str] = None, **kwargs: Any) -> str:
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
            template_url=self.content_type_with_encoding.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    content_type_with_encoding.metadata = {"url": "/mediatypes/contentTypeWithEncoding"}

    @distributed_trace_async
    async def binary_body_with_two_content_types(self, message: IO, **kwargs: Any) -> str:
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
            template_url=self.binary_body_with_two_content_types.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    binary_body_with_two_content_types.metadata = {"url": "/mediatypes/binaryBodyTwoContentTypes"}

    @distributed_trace_async
    async def binary_body_with_three_content_types(self, message: IO, **kwargs: Any) -> str:
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
            template_url=self.binary_body_with_three_content_types.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    binary_body_with_three_content_types.metadata = {"url": "/mediatypes/binaryBodyThreeContentTypes"}

    @overload
    async def body_three_types(self, message: Any, *, content_type: str = "application/json", **kwargs: Any) -> str:
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
    async def body_three_types(
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
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def body_three_types(self, message: str, *, content_type: Optional[str] = None, **kwargs: Any) -> str:
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

    @distributed_trace_async
    async def body_three_types(self, message: Union[Any, IO, str], **kwargs: Any) -> str:
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
        if isinstance(message, (IO, bytes)):
            content_type = content_type or "application/octet-stream"
            _content = message
        else:
            _json = self._serialize.body(message, "object")
            content_type = content_type or "application/json"

        request = build_body_three_types_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.body_three_types.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    body_three_types.metadata = {"url": "/mediatypes/bodyThreeTypes"}

    @distributed_trace_async
    async def put_text_and_json_body(self, message: str, **kwargs: Any) -> str:
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
            template_url=self.put_text_and_json_body.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize("str", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    put_text_and_json_body.metadata = {"url": "/mediatypes/textAndJson"}
