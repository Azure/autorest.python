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
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._inheritance_operations import build_get_valid_request, build_put_valid_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class InheritanceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodycomplex.aio.AutoRestComplexTestService`'s
        :attr:`inheritance` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_valid(self, **kwargs: Any) -> _models.Siamese:
        """Get complex types that extend others.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Siamese or the result of cls(response)
        :rtype: ~bodycomplex.models.Siamese
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Siamese]

        request = build_get_valid_request(
            template_url=self.get_valid.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Siamese", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_valid.metadata = {"url": "/complex/inheritance/valid"}  # type: ignore

    @overload
    async def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: _models.Siamese, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Put complex types that extend others.

        :param complex_body: Please put a siamese with id=2, name="Siameee", color=green,
         breed=persion, which hates 2 dogs, the 1st one named "Potato" with id=1 and food="tomato", and
         the 2nd one named "Tomato" with id=-1 and food="french fries". Required.
        :type complex_body: ~bodycomplex.models.Siamese
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @overload
    async def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: IO, *, content_type: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Put complex types that extend others.

        :param complex_body: Please put a siamese with id=2, name="Siameee", color=green,
         breed=persion, which hates 2 dogs, the 1st one named "Potato" with id=1 and food="tomato", and
         the 2nd one named "Tomato" with id=-1 and food="french fries". Required.
        :type complex_body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        ...

    @distributed_trace_async
    async def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: Union[_models.Siamese, IO], **kwargs: Any
    ) -> None:
        """Put complex types that extend others.

        :param complex_body: Please put a siamese with id=2, name="Siameee", color=green,
         breed=persion, which hates 2 dogs, the 1st one named "Potato" with id=1 and food="tomato", and
         the 2nd one named "Tomato" with id=-1 and food="french fries". Is either a model type or a IO
         type. Required.
        :type complex_body: ~bodycomplex.models.Siamese or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = None
        _content = None
        if isinstance(complex_body, (IO, bytes)):
            _content = complex_body
        else:
            _json = self._serialize.body(complex_body, "Siamese")
            content_type = content_type or "application/json"

        request = build_put_valid_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.put_valid.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid.metadata = {"url": "/complex/inheritance/valid"}  # type: ignore
