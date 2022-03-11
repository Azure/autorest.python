# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._http_server_failure_operations import (
    build_delete505_request,
    build_get501_request,
    build_head501_request,
    build_post505_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class HttpServerFailureOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~httpinfrastructure.aio.AutoRestHttpInfrastructureTestService`'s
        :attr:`http_server_failure` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def head501(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Return 501 status code - should be represented in the client as an error.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_head501_request(
            template_url=self.head501.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    head501.metadata = {"url": "/http/failure/server/501"}  # type: ignore

    @distributed_trace_async
    async def get501(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Return 501 status code - should be represented in the client as an error.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get501_request(
            template_url=self.get501.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get501.metadata = {"url": "/http/failure/server/501"}  # type: ignore

    @distributed_trace_async
    async def post505(  # pylint: disable=inconsistent-return-statements
        self, boolean_value: Optional[bool] = True, **kwargs: Any
    ) -> None:
        """Return 505 status code - should be represented in the client as an error.

        :param boolean_value: Simple boolean value true. Possible values are True or None. Default
         value is True.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        if boolean_value is not None:
            _json = self._serialize.body(boolean_value, "bool")
        else:
            _json = None

        request = build_post505_request(
            content_type=content_type,
            json=_json,
            template_url=self.post505.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post505.metadata = {"url": "/http/failure/server/505"}  # type: ignore

    @distributed_trace_async
    async def delete505(  # pylint: disable=inconsistent-return-statements
        self, boolean_value: Optional[bool] = True, **kwargs: Any
    ) -> None:
        """Return 505 status code - should be represented in the client as an error.

        :param boolean_value: Simple boolean value true. Possible values are True or None. Default
         value is True.
        :type boolean_value: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        if boolean_value is not None:
            _json = self._serialize.body(boolean_value, "bool")
        else:
            _json = None

        request = build_delete505_request(
            content_type=content_type,
            json=_json,
            template_url=self.delete505.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in []:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete505.metadata = {"url": "/http/failure/server/505"}  # type: ignore
