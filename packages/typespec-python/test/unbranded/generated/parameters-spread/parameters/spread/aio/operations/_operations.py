# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, MutableMapping, Optional, Type, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder
from ...operations._operations import (
    build_alias_spread_as_request_body_request,
    build_alias_spread_as_request_parameter_request,
    build_alias_spread_with_multiple_parameters_request,
    build_model_spread_as_request_body_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]
_Unset: Any = object()


class ModelOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~parameters.spread.aio.SpreadClient`'s
        :attr:`model` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, body: _models.BodyParameter, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :param body: Required.
        :type body: ~parameters.spread.models.BodyParameter
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str"  # Required.
                }
        """

    @overload
    async def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.BodyParameter, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :param body: Is one of the following types: BodyParameter, JSON, IO[bytes] Required.
        :type body: ~parameters.spread.models.BodyParameter or JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str"  # Required.
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
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

        _request = build_model_spread_as_request_body_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore


class AliasOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~parameters.spread.aio.SpreadClient`'s
        :attr:`alias` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str"  # Required.
                }
        """

    @overload
    async def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, *, name: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :keyword name: Required.
        :paramtype name: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def spread_as_request_body(  # pylint: disable=inconsistent-return-statements
        self, body: Union[JSON, IO[bytes]] = _Unset, *, name: str = _Unset, **kwargs: Any
    ) -> None:
        """spread_as_request_body.

        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword name: Required.
        :paramtype name: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str"  # Required.
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
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

        if body is _Unset:
            if name is _Unset:
                raise TypeError("missing required argument: name")
            body = {"name": name}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_alias_spread_as_request_body_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def spread_as_request_parameter(  # pylint: disable=inconsistent-return-statements
        self, id: str, body: JSON, *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_parameter.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: JSON
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str"  # Required.
                }
        """

    @overload
    async def spread_as_request_parameter(  # pylint: disable=inconsistent-return-statements
        self, id: str, *, x_ms_test_header: str, name: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_parameter.

        :param id: Required.
        :type id: str
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword name: Required.
        :paramtype name: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def spread_as_request_parameter(  # pylint: disable=inconsistent-return-statements
        self, id: str, body: IO[bytes], *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_as_request_parameter.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def spread_as_request_parameter(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        x_ms_test_header: str,
        name: str = _Unset,
        **kwargs: Any
    ) -> None:
        """spread_as_request_parameter.

        :param id: Required.
        :type id: str
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword name: Required.
        :paramtype name: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str"  # Required.
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
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

        if body is _Unset:
            if name is _Unset:
                raise TypeError("missing required argument: name")
            body = {"name": name}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_alias_spread_as_request_parameter_request(
            id=id,
            x_ms_test_header=x_ms_test_header,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def spread_with_multiple_parameters(  # pylint: disable=inconsistent-return-statements
        self, id: str, body: JSON, *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_with_multiple_parameters.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: JSON
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "prop1": "str",  # Required.
                    "prop2": "str",  # Required.
                    "prop3": "str",  # Required.
                    "prop4": "str",  # Required.
                    "prop5": "str",  # Required.
                    "prop6": "str"  # Required.
                }
        """

    @overload
    async def spread_with_multiple_parameters(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        *,
        x_ms_test_header: str,
        prop1: str,
        prop2: str,
        prop3: str,
        prop4: str,
        prop5: str,
        prop6: str,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """spread_with_multiple_parameters.

        :param id: Required.
        :type id: str
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword prop1: Required.
        :paramtype prop1: str
        :keyword prop2: Required.
        :paramtype prop2: str
        :keyword prop3: Required.
        :paramtype prop3: str
        :keyword prop4: Required.
        :paramtype prop4: str
        :keyword prop5: Required.
        :paramtype prop5: str
        :keyword prop6: Required.
        :paramtype prop6: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def spread_with_multiple_parameters(  # pylint: disable=inconsistent-return-statements
        self, id: str, body: IO[bytes], *, x_ms_test_header: str, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """spread_with_multiple_parameters.

        :param id: Required.
        :type id: str
        :param body: Required.
        :type body: IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def spread_with_multiple_parameters(  # pylint: disable=inconsistent-return-statements
        self,
        id: str,
        body: Union[JSON, IO[bytes]] = _Unset,
        *,
        x_ms_test_header: str,
        prop1: str = _Unset,
        prop2: str = _Unset,
        prop3: str = _Unset,
        prop4: str = _Unset,
        prop5: str = _Unset,
        prop6: str = _Unset,
        **kwargs: Any
    ) -> None:
        """spread_with_multiple_parameters.

        :param id: Required.
        :type id: str
        :param body: Is either a JSON type or a IO[bytes] type. Required.
        :type body: JSON or IO[bytes]
        :keyword x_ms_test_header: Required.
        :paramtype x_ms_test_header: str
        :keyword prop1: Required.
        :paramtype prop1: str
        :keyword prop2: Required.
        :paramtype prop2: str
        :keyword prop3: Required.
        :paramtype prop3: str
        :keyword prop4: Required.
        :paramtype prop4: str
        :keyword prop5: Required.
        :paramtype prop5: str
        :keyword prop6: Required.
        :paramtype prop6: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "prop1": "str",  # Required.
                    "prop2": "str",  # Required.
                    "prop3": "str",  # Required.
                    "prop4": "str",  # Required.
                    "prop5": "str",  # Required.
                    "prop6": "str"  # Required.
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
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

        if body is _Unset:
            if prop1 is _Unset:
                raise TypeError("missing required argument: prop1")
            if prop2 is _Unset:
                raise TypeError("missing required argument: prop2")
            if prop3 is _Unset:
                raise TypeError("missing required argument: prop3")
            if prop4 is _Unset:
                raise TypeError("missing required argument: prop4")
            if prop5 is _Unset:
                raise TypeError("missing required argument: prop5")
            if prop6 is _Unset:
                raise TypeError("missing required argument: prop6")
            body = {"prop1": prop1, "prop2": prop2, "prop3": prop3, "prop4": prop4, "prop5": prop5, "prop6": prop6}
            body = {k: v for k, v in body.items() if v is not None}
        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_alias_spread_with_multiple_parameters_request(
            id=id,
            x_ms_test_header=x_ms_test_header,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
