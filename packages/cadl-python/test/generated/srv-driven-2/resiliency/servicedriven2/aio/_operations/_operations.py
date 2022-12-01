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
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import (
    build_service_driven2_delete_parameters_request,
    build_service_driven2_get_new_operation_request,
    build_service_driven2_get_optional_request,
    build_service_driven2_get_required_request,
    build_service_driven2_head_no_params_request,
    build_service_driven2_post_parameters_request,
    build_service_driven2_put_required_optional_request,
)
from ..._validation import api_version_validation
from .._vendor import ServiceDriven2ClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ServiceDriven2ClientOperationsMixin(ServiceDriven2ClientMixinABC):
    @distributed_trace_async
    @api_version_validation(
        params_added_on={"1.1.0": ["new_parameter"]},
    )
    async def head_no_params(self, *, new_parameter: Optional[str] = None, **kwargs: Any) -> bool:
        """Head request, no params.
         Initially has no query parameters. After evolution, a new optional query parameter is added.

        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: bool
        :rtype: bool
        :raises ~azure.core.exceptions.HttpResponseError:
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

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_service_driven2_head_no_params_request(
            new_parameter=new_parameter,
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
        return 200 <= response.status_code <= 299

    @distributed_trace_async
    @api_version_validation(
        params_added_on={"1.1.0": ["new_parameter"]},
    )
    async def get_required(
        self, *, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any
    ) -> _models.Message:
        """Get true Boolean value on path.
         Initially only has one required Query Parameter. After evolution, a new optional query
        parameter is added.

        :keyword parameter: I am a required parameter. Required.
        :paramtype parameter: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: Message. The Message is compatible with MutableMapping
        :rtype: ~resiliency.servicedriven2.models.Message
        :raises ~azure.core.exceptions.HttpResponseError:
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

        cls: ClsType[_models.Message] = kwargs.pop("cls", None)

        request = build_service_driven2_get_required_request(
            parameter=parameter,
            new_parameter=new_parameter,
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

        deserialized = _deserialize(_models.Message, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    @api_version_validation(
        params_added_on={"1.1.0": ["new_parameter"]},
    )
    async def put_required_optional(
        self,
        *,
        required_param: str,
        optional_param: Optional[str] = None,
        new_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Message:
        """Initially has one required query parameter and one optional query parameter.  After evolution,
        a new optional query parameter is added.

        :keyword required_param: I am a required parameter. Required.
        :paramtype required_param: str
        :keyword optional_param: I am an optional parameter. Default value is None.
        :paramtype optional_param: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: Message. The Message is compatible with MutableMapping
        :rtype: ~resiliency.servicedriven2.models.Message
        :raises ~azure.core.exceptions.HttpResponseError:
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

        cls: ClsType[_models.Message] = kwargs.pop("cls", None)

        request = build_service_driven2_put_required_optional_request(
            required_param=required_param,
            optional_param=optional_param,
            new_parameter=new_parameter,
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

        deserialized = _deserialize(_models.Message, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def post_parameters(
        self,
        content_type_path: Union[str, _models.ContentTypePathType],
        parameter: _models.PostInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Message:
        """POST a JSON or a JPEG.

        :param content_type_path: Known values are: "json" and "jpeg". Required.
        :type content_type_path: str or ~resiliency.servicedriven2.models.ContentTypePathType
        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Required.
        :type parameter: ~resiliency.servicedriven2.models.PostInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Message. The Message is compatible with MutableMapping
        :rtype: ~resiliency.servicedriven2.models.Message
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_parameters(
        self,
        content_type_path: Union[str, _models.ContentTypePathType],
        parameter: JSON,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Message:
        """POST a JSON or a JPEG.

        :param content_type_path: Known values are: "json" and "jpeg". Required.
        :type content_type_path: str or ~resiliency.servicedriven2.models.ContentTypePathType
        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Required.
        :type parameter: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Message. The Message is compatible with MutableMapping
        :rtype: ~resiliency.servicedriven2.models.Message
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def post_parameters(
        self,
        content_type_path: Union[str, _models.ContentTypePathType],
        parameter: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Message:
        """POST a JSON or a JPEG.

        :param content_type_path: Known values are: "json" and "jpeg". Required.
        :type content_type_path: str or ~resiliency.servicedriven2.models.ContentTypePathType
        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Required.
        :type parameter: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Message. The Message is compatible with MutableMapping
        :rtype: ~resiliency.servicedriven2.models.Message
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def post_parameters(
        self,
        content_type_path: Union[str, _models.ContentTypePathType],
        parameter: Union[_models.PostInput, JSON, IO],
        **kwargs: Any
    ) -> _models.Message:
        """POST a JSON or a JPEG.

        :param content_type_path: Known values are: "json" and "jpeg". Required.
        :type content_type_path: str or ~resiliency.servicedriven2.models.ContentTypePathType
        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Is one of the following types: model, JSON, IO Required.
        :type parameter: ~resiliency.servicedriven2.models.PostInput or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: Message. The Message is compatible with MutableMapping
        :rtype: ~resiliency.servicedriven2.models.Message
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
        cls: ClsType[_models.Message] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(parameter, (IO, bytes)):
            _content = parameter
        else:
            _content = json.dumps(parameter, cls=AzureJSONEncoder)

        request = build_service_driven2_post_parameters_request(
            content_type_path=content_type_path,
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

        deserialized = _deserialize(_models.Message, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    @api_version_validation(
        method_added_on="1.1.0",
    )
    async def delete_parameters(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Delete something.
         Initially the path exists but there is no delete method. After evolution this is a new method
        in a known path.

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

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_service_driven2_delete_parameters_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    @api_version_validation(
        params_added_on={"1.1.0": ["new_parameter"]},
    )
    async def get_optional(
        self, *, optional_param: Optional[str] = None, new_parameter: Optional[str] = None, **kwargs: Any
    ) -> _models.Message:
        """Get true Boolean value on path.
         Initially has one optional query parameter. After evolution, a new optional query parameter is
        added.

        :keyword optional_param: I am an optional parameter. Default value is None.
        :paramtype optional_param: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: Message. The Message is compatible with MutableMapping
        :rtype: ~resiliency.servicedriven2.models.Message
        :raises ~azure.core.exceptions.HttpResponseError:
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

        cls: ClsType[_models.Message] = kwargs.pop("cls", None)

        request = build_service_driven2_get_optional_request(
            optional_param=optional_param,
            new_parameter=new_parameter,
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

        deserialized = _deserialize(_models.Message, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    @api_version_validation(
        method_added_on="1.1.0",
    )
    async def get_new_operation(self, **kwargs: Any) -> _models.Message:
        """I'm a new operation.
         Initially neither path or method exist for this operation. After evolution, this is a new
        method in a new path.

        :return: Message. The Message is compatible with MutableMapping
        :rtype: ~resiliency.servicedriven2.models.Message
        :raises ~azure.core.exceptions.HttpResponseError:
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

        cls: ClsType[_models.Message] = kwargs.pop("cls", None)

        request = build_service_driven2_get_new_operation_request(
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

        deserialized = _deserialize(_models.Message, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
