# pylint: disable=too-many-lines
# coding=utf-8

from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import (
    build_usage_input_and_output_request,
    build_usage_input_request,
    build_usage_output_request,
)
from .._vendor import UsageClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class UsageClientOperationsMixin(UsageClientMixinABC):
    @overload
    async def input(  # pylint: disable=inconsistent-return-statements
        self, input: _models.InputRecord, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """input.

        :param input: Required.
        :type input: ~typetest.model.usage.models.InputRecord
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def input(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """input.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def input(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """input.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def input(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.InputRecord, JSON, IO], **kwargs: Any
    ) -> None:
        """input.

        :param input: Is one of the following types: InputRecord, JSON, IO Required.
        :type input: ~typetest.model.usage.models.InputRecord or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
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

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_usage_input_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
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

    async def output(self, **kwargs: Any) -> _models.OutputRecord:
        """output.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: OutputRecord. The OutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.OutputRecord
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.OutputRecord] = kwargs.pop("cls", None)

        _request = build_usage_output_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.OutputRecord, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def input_and_output(
        self, body: _models.InputOutputRecord, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.InputOutputRecord:
        """input_and_output.

        :param body: Required.
        :type body: ~typetest.model.usage.models.InputOutputRecord
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: InputOutputRecord. The InputOutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.InputOutputRecord
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def input_and_output(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.InputOutputRecord:
        """input_and_output.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: InputOutputRecord. The InputOutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.InputOutputRecord
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def input_and_output(
        self, body: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.InputOutputRecord:
        """input_and_output.

        :param body: Required.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: InputOutputRecord. The InputOutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.InputOutputRecord
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def input_and_output(
        self, body: Union[_models.InputOutputRecord, JSON, IO], **kwargs: Any
    ) -> _models.InputOutputRecord:
        """input_and_output.

        :param body: Is one of the following types: InputOutputRecord, JSON, IO Required.
        :type body: ~typetest.model.usage.models.InputOutputRecord or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: InputOutputRecord. The InputOutputRecord is compatible with MutableMapping
        :rtype: ~typetest.model.usage.models.InputOutputRecord
        :raises ~corehttp.exceptions.HttpResponseError:
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
        cls: ClsType[_models.InputOutputRecord] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_usage_input_and_output_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.InputOutputRecord, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
