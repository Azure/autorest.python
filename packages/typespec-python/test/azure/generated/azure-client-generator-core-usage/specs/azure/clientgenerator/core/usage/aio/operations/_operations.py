# coding=utf-8
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core import AsyncPipelineClient
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
from ..._serialization import Deserializer, Serializer
from ...operations._operations import (
    build_model_in_operation_input_to_input_output_request,
    build_model_in_operation_model_in_read_only_property_request,
    build_model_in_operation_orphan_model_serializable_request,
    build_model_in_operation_output_to_input_output_request,
)
from .._configuration import UsageClientConfiguration

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ModelInOperationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~specs.azure.clientgenerator.core.usage.aio.UsageClient`'s
        :attr:`model_in_operation` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: UsageClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def input_to_input_output(
        self, body: _models.InputModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Expected body parameter:

        .. code-block:: json

           {
             "name": "Madge"
           }.

        :param body: Required.
        :type body: ~specs.azure.clientgenerator.core.usage.models.InputModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def input_to_input_output(self, body: JSON, *, content_type: str = "application/json", **kwargs: Any) -> None:
        """Expected body parameter:

        .. code-block:: json

           {
             "name": "Madge"
           }.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def input_to_input_output(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Expected body parameter:

        .. code-block:: json

           {
             "name": "Madge"
           }.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def input_to_input_output(self, body: Union[_models.InputModel, JSON, IO[bytes]], **kwargs: Any) -> None:
        """Expected body parameter:

        .. code-block:: json

           {
             "name": "Madge"
           }.

        :param body: Is one of the following types: InputModel, JSON, IO[bytes] Required.
        :type body: ~specs.azure.clientgenerator.core.usage.models.InputModel or JSON or IO[bytes]
        :return: None
        :rtype: None
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_model_in_operation_input_to_input_output_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def output_to_input_output(self, **kwargs: Any) -> _models.OutputModel:
        """Expected response body:

        .. code-block:: json

           {
             "name": "Madge"
           }.

        :return: OutputModel. The OutputModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.OutputModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.OutputModel] = kwargs.pop("cls", None)

        _request = build_model_in_operation_output_to_input_output_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.OutputModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def model_in_read_only_property(
        self, body: _models.RoundTripModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RoundTripModel:
        """ "ResultModel" should be usage=output, as it is read-only and does not exist in request body.

        Expected body parameter:

        .. code-block:: json

           {
           }

        Expected response body:

        .. code-block:: json

           {
             "result": {
               "name": "Madge"
             }
           }.

        :param body: Required.
        :type body: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoundTripModel. The RoundTripModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def model_in_read_only_property(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RoundTripModel:
        """ "ResultModel" should be usage=output, as it is read-only and does not exist in request body.

        Expected body parameter:

        .. code-block:: json

           {
           }

        Expected response body:

        .. code-block:: json

           {
             "result": {
               "name": "Madge"
             }
           }.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoundTripModel. The RoundTripModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def model_in_read_only_property(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RoundTripModel:
        """ "ResultModel" should be usage=output, as it is read-only and does not exist in request body.

        Expected body parameter:

        .. code-block:: json

           {
           }

        Expected response body:

        .. code-block:: json

           {
             "result": {
               "name": "Madge"
             }
           }.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoundTripModel. The RoundTripModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def model_in_read_only_property(
        self, body: Union[_models.RoundTripModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.RoundTripModel:
        """ "ResultModel" should be usage=output, as it is read-only and does not exist in request body.

        Expected body parameter:

        .. code-block:: json

           {
           }

        Expected response body:

        .. code-block:: json

           {
             "result": {
               "name": "Madge"
             }
           }.

        :param body: Is one of the following types: RoundTripModel, JSON, IO[bytes] Required.
        :type body: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel or JSON or IO[bytes]
        :return: RoundTripModel. The RoundTripModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
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
        cls: ClsType[_models.RoundTripModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_model_in_operation_model_in_read_only_property_request(
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.RoundTripModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def orphan_model_serializable(self, body: Any, **kwargs: Any) -> None:
        """Serialize the 'OrphanModel' as request body.

        Expected body parameter:

        .. code-block:: json

           {
             "name": "name",
             "desc": "desc"
           }.

        :param body: Required.
        :type body: any
        :return: None
        :rtype: None
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

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_model_in_operation_orphan_model_serializable_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
