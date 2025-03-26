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
from ..._operations._operations import build_azure_example_basic_action_request
from .._vendor import AzureExampleClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AzureExampleClientOperationsMixin(AzureExampleClientMixinABC):

    @overload
    async def basic_action(
        self,
        body: _models.ActionRequest,
        *,
        query_param: str,
        header_param: str,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ActionResponse:
        """basic_action.

        :param body: Required.
        :type body: ~specs.azure.example.basic.models.ActionRequest
        :keyword query_param: Required.
        :paramtype query_param: str
        :keyword header_param: Required.
        :paramtype header_param: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ActionResponse. The ActionResponse is compatible with MutableMapping
        :rtype: ~specs.azure.example.basic.models.ActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def basic_action(
        self, body: JSON, *, query_param: str, header_param: str, content_type: str = "application/json", **kwargs: Any
    ) -> _models.ActionResponse:
        """basic_action.

        :param body: Required.
        :type body: JSON
        :keyword query_param: Required.
        :paramtype query_param: str
        :keyword header_param: Required.
        :paramtype header_param: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ActionResponse. The ActionResponse is compatible with MutableMapping
        :rtype: ~specs.azure.example.basic.models.ActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def basic_action(
        self,
        body: IO[bytes],
        *,
        query_param: str,
        header_param: str,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ActionResponse:
        """basic_action.

        :param body: Required.
        :type body: IO[bytes]
        :keyword query_param: Required.
        :paramtype query_param: str
        :keyword header_param: Required.
        :paramtype header_param: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ActionResponse. The ActionResponse is compatible with MutableMapping
        :rtype: ~specs.azure.example.basic.models.ActionResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def basic_action(
        self, body: Union[_models.ActionRequest, JSON, IO[bytes]], *, query_param: str, header_param: str, **kwargs: Any
    ) -> _models.ActionResponse:
        """basic_action.

        :param body: Is one of the following types: ActionRequest, JSON, IO[bytes] Required.
        :type body: ~specs.azure.example.basic.models.ActionRequest or JSON or IO[bytes]
        :keyword query_param: Required.
        :paramtype query_param: str
        :keyword header_param: Required.
        :paramtype header_param: str
        :return: ActionResponse. The ActionResponse is compatible with MutableMapping
        :rtype: ~specs.azure.example.basic.models.ActionResponse
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
        cls: ClsType[_models.ActionResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_azure_example_basic_action_request(
            query_param=query_param,
            header_param=header_param,
            content_type=content_type,
            api_version=self._config.api_version,
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
            deserialized = _deserialize(_models.ActionResponse, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
