# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ..._operations._operations import build_type_changed_from_test_request
from .._vendor import TypeChangedFromClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class TypeChangedFromClientOperationsMixin(TypeChangedFromClientMixinABC):

    @overload
    async def test(
        self, body: _models.TestModel, *, param: str, content_type: str = "application/json", **kwargs: Any
    ) -> _models.TestModel:
        """test.

        :param body: Required.
        :type body: ~versioning.typechangedfrom.models.TestModel
        :keyword param: Required.
        :paramtype param: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TestModel. The TestModel is compatible with MutableMapping
        :rtype: ~versioning.typechangedfrom.models.TestModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "changedProp": "str",
                    "prop": "str"
                }

                # response body for status code(s): 200
                response == {
                    "changedProp": "str",
                    "prop": "str"
                }
        """

    @overload
    async def test(
        self, body: JSON, *, param: str, content_type: str = "application/json", **kwargs: Any
    ) -> _models.TestModel:
        """test.

        :param body: Required.
        :type body: JSON
        :keyword param: Required.
        :paramtype param: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TestModel. The TestModel is compatible with MutableMapping
        :rtype: ~versioning.typechangedfrom.models.TestModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "changedProp": "str",
                    "prop": "str"
                }
        """

    @overload
    async def test(
        self, body: IO[bytes], *, param: str, content_type: str = "application/json", **kwargs: Any
    ) -> _models.TestModel:
        """test.

        :param body: Required.
        :type body: IO[bytes]
        :keyword param: Required.
        :paramtype param: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: TestModel. The TestModel is compatible with MutableMapping
        :rtype: ~versioning.typechangedfrom.models.TestModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "changedProp": "str",
                    "prop": "str"
                }
        """

    @distributed_trace_async
    async def test(
        self, body: Union[_models.TestModel, JSON, IO[bytes]], *, param: str, **kwargs: Any
    ) -> _models.TestModel:
        """test.

        :param body: Is one of the following types: TestModel, JSON, IO[bytes] Required.
        :type body: ~versioning.typechangedfrom.models.TestModel or JSON or IO[bytes]
        :keyword param: Required.
        :paramtype param: str
        :return: TestModel. The TestModel is compatible with MutableMapping
        :rtype: ~versioning.typechangedfrom.models.TestModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "changedProp": "str",
                    "prop": "str"
                }

                # response body for status code(s): 200
                response == {
                    "changedProp": "str",
                    "prop": "str"
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
        cls: ClsType[_models.TestModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_type_changed_from_test_request(
            param=param,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "version": self._serialize.url("self._config.version", self._config.version, "str"),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.TestModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
