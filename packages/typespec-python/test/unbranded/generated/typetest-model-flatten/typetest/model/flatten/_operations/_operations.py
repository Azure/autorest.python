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
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import FlattenClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_flatten_put_flatten_model_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/flatten/flattenModel"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_flatten_put_nested_flatten_model_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/flatten/nestedFlattenModel"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class FlattenClientOperationsMixin(FlattenClientMixinABC):

    @overload
    def put_flatten_model(
        self, input: _models.FlattenModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FlattenModel:
        """put_flatten_model.

        :param input: Required.
        :type input: ~typetest.model.flatten.models.FlattenModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FlattenModel. The FlattenModel is compatible with MutableMapping
        :rtype: ~typetest.model.flatten.models.FlattenModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "name": "str",
                    "properties": {
                        "age": 0,
                        "description": "str"
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",
                    "properties": {
                        "age": 0,
                        "description": "str"
                    }
                }
        """

    @overload
    def put_flatten_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FlattenModel:
        """put_flatten_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FlattenModel. The FlattenModel is compatible with MutableMapping
        :rtype: ~typetest.model.flatten.models.FlattenModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",
                    "properties": {
                        "age": 0,
                        "description": "str"
                    }
                }
        """

    @overload
    def put_flatten_model(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FlattenModel:
        """put_flatten_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FlattenModel. The FlattenModel is compatible with MutableMapping
        :rtype: ~typetest.model.flatten.models.FlattenModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",
                    "properties": {
                        "age": 0,
                        "description": "str"
                    }
                }
        """

    def put_flatten_model(
        self, input: Union[_models.FlattenModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.FlattenModel:
        """put_flatten_model.

        :param input: Is one of the following types: FlattenModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.flatten.models.FlattenModel or JSON or IO[bytes]
        :return: FlattenModel. The FlattenModel is compatible with MutableMapping
        :rtype: ~typetest.model.flatten.models.FlattenModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "name": "str",
                    "properties": {
                        "age": 0,
                        "description": "str"
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",
                    "properties": {
                        "age": 0,
                        "description": "str"
                    }
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
        cls: ClsType[_models.FlattenModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_flatten_put_flatten_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            try:
                response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.FlattenModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put_nested_flatten_model(
        self, input: _models.NestedFlattenModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NestedFlattenModel:
        """put_nested_flatten_model.

        :param input: Required.
        :type input: ~typetest.model.flatten.models.NestedFlattenModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NestedFlattenModel. The NestedFlattenModel is compatible with MutableMapping
        :rtype: ~typetest.model.flatten.models.NestedFlattenModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "name": "str",
                    "properties": {
                        "properties": {
                            "age": 0,
                            "description": "str"
                        },
                        "summary": "str"
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",
                    "properties": {
                        "properties": {
                            "age": 0,
                            "description": "str"
                        },
                        "summary": "str"
                    }
                }
        """

    @overload
    def put_nested_flatten_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NestedFlattenModel:
        """put_nested_flatten_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NestedFlattenModel. The NestedFlattenModel is compatible with MutableMapping
        :rtype: ~typetest.model.flatten.models.NestedFlattenModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",
                    "properties": {
                        "properties": {
                            "age": 0,
                            "description": "str"
                        },
                        "summary": "str"
                    }
                }
        """

    @overload
    def put_nested_flatten_model(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NestedFlattenModel:
        """put_nested_flatten_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NestedFlattenModel. The NestedFlattenModel is compatible with MutableMapping
        :rtype: ~typetest.model.flatten.models.NestedFlattenModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",
                    "properties": {
                        "properties": {
                            "age": 0,
                            "description": "str"
                        },
                        "summary": "str"
                    }
                }
        """

    def put_nested_flatten_model(
        self, input: Union[_models.NestedFlattenModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.NestedFlattenModel:
        """put_nested_flatten_model.

        :param input: Is one of the following types: NestedFlattenModel, JSON, IO[bytes] Required.
        :type input: ~typetest.model.flatten.models.NestedFlattenModel or JSON or IO[bytes]
        :return: NestedFlattenModel. The NestedFlattenModel is compatible with MutableMapping
        :rtype: ~typetest.model.flatten.models.NestedFlattenModel
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "name": "str",
                    "properties": {
                        "properties": {
                            "age": 0,
                            "description": "str"
                        },
                        "summary": "str"
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",
                    "properties": {
                        "properties": {
                            "age": 0,
                            "description": "str"
                        },
                        "summary": "str"
                    }
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
        cls: ClsType[_models.NestedFlattenModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_flatten_put_nested_flatten_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            try:
                response.read()  # Load the body in memory and close the socket
            except (StreamConsumedError, StreamClosedError):
                pass
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.NestedFlattenModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
