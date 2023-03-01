# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder
from ..._operations._operations import (
    build_unions_send_first_named_union_value_request,
    build_unions_send_int_array_request,
    build_unions_send_int_request,
    build_unions_send_second_named_union_value_request,
)
from .._vendor import UnionsClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class UnionsClientOperationsMixin(UnionsClientMixinABC):
    @overload
    async def send_int(  # pylint: disable=inconsistent-return-statements
        self, input: _models.ModelWithSimpleUnionProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_int.

        :param input: Required.
        :type input: ~unions.models.ModelWithSimpleUnionProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def send_int(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_int.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def send_int(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_int.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def send_int(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.ModelWithSimpleUnionProperty, JSON, IO], **kwargs: Any
    ) -> None:
        """send_int.

        :param input: Is one of the following types: ModelWithSimpleUnionProperty, JSON, IO Required.
        :type input: ~unions.models.ModelWithSimpleUnionProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore

        request = build_unions_send_int_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    async def send_int_array(  # pylint: disable=inconsistent-return-statements
        self, input: _models.ModelWithSimpleUnionProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_int_array.

        :param input: Required.
        :type input: ~unions.models.ModelWithSimpleUnionProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def send_int_array(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_int_array.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def send_int_array(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_int_array.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def send_int_array(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.ModelWithSimpleUnionProperty, JSON, IO], **kwargs: Any
    ) -> None:
        """send_int_array.

        :param input: Is one of the following types: ModelWithSimpleUnionProperty, JSON, IO Required.
        :type input: ~unions.models.ModelWithSimpleUnionProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore

        request = build_unions_send_int_array_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    async def send_first_named_union_value(  # pylint: disable=inconsistent-return-statements
        self, input: _models.ModelWithNamedUnionProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_first_named_union_value.

        :param input: Required.
        :type input: ~unions.models.ModelWithNamedUnionProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def send_first_named_union_value(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_first_named_union_value.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def send_first_named_union_value(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_first_named_union_value.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def send_first_named_union_value(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.ModelWithNamedUnionProperty, JSON, IO], **kwargs: Any
    ) -> None:
        """send_first_named_union_value.

        :param input: Is one of the following types: ModelWithNamedUnionProperty, JSON, IO Required.
        :type input: ~unions.models.ModelWithNamedUnionProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore

        request = build_unions_send_first_named_union_value_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    async def send_second_named_union_value(  # pylint: disable=inconsistent-return-statements
        self, input: _models.ModelWithNamedUnionProperty, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_second_named_union_value.

        :param input: Required.
        :type input: ~unions.models.ModelWithNamedUnionProperty
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def send_second_named_union_value(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_second_named_union_value.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def send_second_named_union_value(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """send_second_named_union_value.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def send_second_named_union_value(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.ModelWithNamedUnionProperty, JSON, IO], **kwargs: Any
    ) -> None:
        """send_second_named_union_value.

        :param input: Is one of the following types: ModelWithNamedUnionProperty, JSON, IO Required.
        :type input: ~unions.models.ModelWithNamedUnionProperty or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder)  # type: ignore

        request = build_unions_send_second_named_union_value_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
