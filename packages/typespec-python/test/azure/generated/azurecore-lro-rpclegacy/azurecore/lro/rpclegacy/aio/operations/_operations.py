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
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ...operations._operations import (
    build_create_resource_poll_via_operation_location_create_job_request,
    build_create_resource_poll_via_operation_location_get_job_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CreateResourcePollViaOperationLocationOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azurecore.lro.rpclegacy.aio.LegacyClient`'s
        :attr:`create_resource_poll_via_operation_location` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_job(self, job_id: str, **kwargs: Any) -> _models.JobResult:
        # pylint: disable=line-too-long
        """Poll a Job.

        :param job_id: A processing job identifier. Required.
        :type job_id: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: JobResult. The JobResult is compatible with MutableMapping
        :rtype: ~azurecore.lro.rpclegacy.models.JobResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "comment": "str",  # Comment. Required.
                    "jobId": "str",  # A processing job identifier. Required.
                    "status": "str",  # The status of the processing job. Required. Known values
                      are: "notStarted", "running", "succeeded", "failed", "canceled", and
                      "partiallyCompleted".
                    "errors": [
                        {
                            "error": {
                                "code": "str",  # One of a server-defined set of
                                  error codes. Required.
                                "message": "str",  # A human-readable representation
                                  of the error. Required.
                                "details": [
                                    ...
                                ],
                                "innererror": {
                                    "code": "str",  # Optional. One of a
                                      server-defined set of error codes.
                                    "innererror": ...
                                },
                                "target": "str"  # Optional. The target of the error.
                            }
                        }
                    ],
                    "results": [
                        "str"  # Optional. The results.
                    ]
                }
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

        cls: ClsType[_models.JobResult] = kwargs.pop("cls", None)

        _request = build_create_resource_poll_via_operation_location_get_job_request(
            job_id=job_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.JobResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_job_initial(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.JobData, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
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
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_create_resource_poll_via_operation_location_create_job_request(
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Operation-Location"] = self._deserialize("str", response.headers.get("Operation-Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @overload
    async def begin_create_job(
        self, body: _models.JobData, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.JobResult]:
        # pylint: disable=line-too-long
        """Creates a Job.

        :param body: Required.
        :type body: ~azurecore.lro.rpclegacy.models.JobData
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns JobResult. The JobResult is compatible with
         MutableMapping
        :rtype: ~azure.core.polling.AsyncLROPoller[~azurecore.lro.rpclegacy.models.JobResult]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "comment": "str"  # Comment. Required.
                }

                # response body for status code(s): 202
                response == {
                    "comment": "str",  # Comment. Required.
                    "jobId": "str",  # A processing job identifier. Required.
                    "status": "str",  # The status of the processing job. Required. Known values
                      are: "notStarted", "running", "succeeded", "failed", "canceled", and
                      "partiallyCompleted".
                    "errors": [
                        {
                            "error": {
                                "code": "str",  # One of a server-defined set of
                                  error codes. Required.
                                "message": "str",  # A human-readable representation
                                  of the error. Required.
                                "details": [
                                    ...
                                ],
                                "innererror": {
                                    "code": "str",  # Optional. One of a
                                      server-defined set of error codes.
                                    "innererror": ...
                                },
                                "target": "str"  # Optional. The target of the error.
                            }
                        }
                    ],
                    "results": [
                        "str"  # Optional. The results.
                    ]
                }
        """

    @overload
    async def begin_create_job(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.JobResult]:
        # pylint: disable=line-too-long
        """Creates a Job.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns JobResult. The JobResult is compatible with
         MutableMapping
        :rtype: ~azure.core.polling.AsyncLROPoller[~azurecore.lro.rpclegacy.models.JobResult]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 202
                response == {
                    "comment": "str",  # Comment. Required.
                    "jobId": "str",  # A processing job identifier. Required.
                    "status": "str",  # The status of the processing job. Required. Known values
                      are: "notStarted", "running", "succeeded", "failed", "canceled", and
                      "partiallyCompleted".
                    "errors": [
                        {
                            "error": {
                                "code": "str",  # One of a server-defined set of
                                  error codes. Required.
                                "message": "str",  # A human-readable representation
                                  of the error. Required.
                                "details": [
                                    ...
                                ],
                                "innererror": {
                                    "code": "str",  # Optional. One of a
                                      server-defined set of error codes.
                                    "innererror": ...
                                },
                                "target": "str"  # Optional. The target of the error.
                            }
                        }
                    ],
                    "results": [
                        "str"  # Optional. The results.
                    ]
                }
        """

    @overload
    async def begin_create_job(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> AsyncLROPoller[_models.JobResult]:
        # pylint: disable=line-too-long
        """Creates a Job.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns JobResult. The JobResult is compatible with
         MutableMapping
        :rtype: ~azure.core.polling.AsyncLROPoller[~azurecore.lro.rpclegacy.models.JobResult]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 202
                response == {
                    "comment": "str",  # Comment. Required.
                    "jobId": "str",  # A processing job identifier. Required.
                    "status": "str",  # The status of the processing job. Required. Known values
                      are: "notStarted", "running", "succeeded", "failed", "canceled", and
                      "partiallyCompleted".
                    "errors": [
                        {
                            "error": {
                                "code": "str",  # One of a server-defined set of
                                  error codes. Required.
                                "message": "str",  # A human-readable representation
                                  of the error. Required.
                                "details": [
                                    ...
                                ],
                                "innererror": {
                                    "code": "str",  # Optional. One of a
                                      server-defined set of error codes.
                                    "innererror": ...
                                },
                                "target": "str"  # Optional. The target of the error.
                            }
                        }
                    ],
                    "results": [
                        "str"  # Optional. The results.
                    ]
                }
        """

    @distributed_trace_async
    async def begin_create_job(
        self, body: Union[_models.JobData, JSON, IO[bytes]], **kwargs: Any
    ) -> AsyncLROPoller[_models.JobResult]:
        # pylint: disable=line-too-long
        """Creates a Job.

        :param body: Is one of the following types: JobData, JSON, IO[bytes] Required.
        :type body: ~azurecore.lro.rpclegacy.models.JobData or JSON or IO[bytes]
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncLROBasePolling. Pass in False
         for this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns JobResult. The JobResult is compatible with
         MutableMapping
        :rtype: ~azure.core.polling.AsyncLROPoller[~azurecore.lro.rpclegacy.models.JobResult]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "comment": "str"  # Comment. Required.
                }

                # response body for status code(s): 202
                response == {
                    "comment": "str",  # Comment. Required.
                    "jobId": "str",  # A processing job identifier. Required.
                    "status": "str",  # The status of the processing job. Required. Known values
                      are: "notStarted", "running", "succeeded", "failed", "canceled", and
                      "partiallyCompleted".
                    "errors": [
                        {
                            "error": {
                                "code": "str",  # One of a server-defined set of
                                  error codes. Required.
                                "message": "str",  # A human-readable representation
                                  of the error. Required.
                                "details": [
                                    ...
                                ],
                                "innererror": {
                                    "code": "str",  # Optional. One of a
                                      server-defined set of error codes.
                                    "innererror": ...
                                },
                                "target": "str"  # Optional. The target of the error.
                            }
                        }
                    ],
                    "results": [
                        "str"  # Optional. The results.
                    ]
                }
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.JobResult] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_job_initial(  # type: ignore
                body=body, content_type=content_type, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["Operation-Location"] = self._deserialize(
                "str", response.headers.get("Operation-Location")
            )

            deserialized = _deserialize(_models.JobResult, response.json())
            if cls:
                return cls(pipeline_response, deserialized, response_headers)  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncLROBasePolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.JobResult].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.JobResult](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )
