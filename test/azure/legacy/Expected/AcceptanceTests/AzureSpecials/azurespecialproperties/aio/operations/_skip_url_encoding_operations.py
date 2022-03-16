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
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._skip_url_encoding_operations import (
    build_get_method_path_valid_request,
    build_get_method_query_null_request,
    build_get_method_query_valid_request,
    build_get_path_query_valid_request,
    build_get_path_valid_request,
    build_get_swagger_path_valid_request,
    build_get_swagger_query_valid_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SkipUrlEncodingOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azurespecialproperties.aio.AutoRestAzureSpecialParametersTestClient`'s
        :attr:`skip_url_encoding` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_method_path_valid(  # pylint: disable=inconsistent-return-statements
        self, unencoded_path_param: str, **kwargs: Any
    ) -> None:
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
        :type unencoded_path_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_method_path_valid_request(
            unencoded_path_param=unencoded_path_param,
            template_url=self.get_method_path_valid.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_method_path_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/method/path/valid/{unencodedPathParam}"}  # type: ignore

    @distributed_trace_async
    async def get_path_valid(  # pylint: disable=inconsistent-return-statements
        self, unencoded_path_param: str, **kwargs: Any
    ) -> None:
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
        :type unencoded_path_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_path_valid_request(
            unencoded_path_param=unencoded_path_param,
            template_url=self.get_path_valid.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_path_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/path/path/valid/{unencodedPathParam}"}  # type: ignore

    @distributed_trace_async
    async def get_swagger_path_valid(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Get method with unencoded path parameter with value 'path1/path2/path3'.

        :keyword unencoded_path_param: An unencoded path parameter with value 'path1/path2/path3'.
         Default value is "path1/path2/path3". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype unencoded_path_param: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        unencoded_path_param = kwargs.pop("unencoded_path_param", "path1/path2/path3")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_swagger_path_valid_request(
            unencoded_path_param=unencoded_path_param,
            template_url=self.get_swagger_path_valid.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_swagger_path_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/swagger/path/valid/{unencodedPathParam}"}  # type: ignore

    @distributed_trace_async
    async def get_method_query_valid(  # pylint: disable=inconsistent-return-statements
        self, q1: str, **kwargs: Any
    ) -> None:
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        :param q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
        :type q1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_method_query_valid_request(
            q1=q1,
            template_url=self.get_method_query_valid.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_method_query_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/method/query/valid"}  # type: ignore

    @distributed_trace_async
    async def get_method_query_null(  # pylint: disable=inconsistent-return-statements
        self, q1: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Get method with unencoded query parameter with value null.

        :param q1: Unencoded query parameter with value null. Default value is None.
        :type q1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_method_query_null_request(
            q1=q1,
            template_url=self.get_method_query_null.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_method_query_null.metadata = {"url": "/azurespecials/skipUrlEncoding/method/query/null"}  # type: ignore

    @distributed_trace_async
    async def get_path_query_valid(  # pylint: disable=inconsistent-return-statements
        self, q1: str, **kwargs: Any
    ) -> None:
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        :param q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
        :type q1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_path_query_valid_request(
            q1=q1,
            template_url=self.get_path_query_valid.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_path_query_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/path/query/valid"}  # type: ignore

    @distributed_trace_async
    async def get_swagger_query_valid(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

        :keyword q1: An unencoded query parameter with value 'value1&q2=value2&q3=value3'. Default
         value is "value1&q2=value2&q3=value3". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype q1: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        q1 = kwargs.pop("q1", _params.pop("q1", "value1&q2=value2&q3=value3"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_swagger_query_valid_request(
            q1=q1,
            template_url=self.get_swagger_query_valid.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_swagger_query_valid.metadata = {"url": "/azurespecials/skipUrlEncoding/swagger/query/valid"}  # type: ignore
