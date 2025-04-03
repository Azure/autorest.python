# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ..._operations._operations import (
    build_flatten_property_put_flatten_model_request,
    build_flatten_property_put_nested_flatten_model_request,
)
from .._vendor import FlattenPropertyClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class FlattenPropertyClientOperationsMixin(FlattenPropertyClientMixinABC):

    @overload
    async def put_flatten_model(
        self, input: _models.FlattenModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FlattenModel:
        """put_flatten_model.

        :param input: Required.
        :type input: ~specs.azure.clientgenerator.core.flattenproperty.models.FlattenModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FlattenModel. The FlattenModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.flattenproperty.models.FlattenModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_flatten_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FlattenModel:
        """put_flatten_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FlattenModel. The FlattenModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.flattenproperty.models.FlattenModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_flatten_model(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.FlattenModel:
        """put_flatten_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: FlattenModel. The FlattenModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.flattenproperty.models.FlattenModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put_flatten_model(
        self, input: Union[_models.FlattenModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.FlattenModel:
        """put_flatten_model.

        :param input: Is one of the following types: FlattenModel, JSON, IO[bytes] Required.
        :type input: ~specs.azure.clientgenerator.core.flattenproperty.models.FlattenModel or JSON or
         IO[bytes]
        :return: FlattenModel. The FlattenModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.flattenproperty.models.FlattenModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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

        _request = build_flatten_property_put_flatten_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
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
    async def put_nested_flatten_model(
        self, input: _models.NestedFlattenModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NestedFlattenModel:
        """put_nested_flatten_model.

        :param input: Required.
        :type input: ~specs.azure.clientgenerator.core.flattenproperty.models.NestedFlattenModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NestedFlattenModel. The NestedFlattenModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.flattenproperty.models.NestedFlattenModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_nested_flatten_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NestedFlattenModel:
        """put_nested_flatten_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NestedFlattenModel. The NestedFlattenModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.flattenproperty.models.NestedFlattenModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def put_nested_flatten_model(
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NestedFlattenModel:
        """put_nested_flatten_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NestedFlattenModel. The NestedFlattenModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.flattenproperty.models.NestedFlattenModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def put_nested_flatten_model(
        self, input: Union[_models.NestedFlattenModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.NestedFlattenModel:
        """put_nested_flatten_model.

        :param input: Is one of the following types: NestedFlattenModel, JSON, IO[bytes] Required.
        :type input: ~specs.azure.clientgenerator.core.flattenproperty.models.NestedFlattenModel or
         JSON or IO[bytes]
        :return: NestedFlattenModel. The NestedFlattenModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.flattenproperty.models.NestedFlattenModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
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

        _request = build_flatten_property_put_nested_flatten_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    await response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.NestedFlattenModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
