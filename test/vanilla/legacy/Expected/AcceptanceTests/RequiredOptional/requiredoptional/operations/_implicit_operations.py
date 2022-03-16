# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, IO, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_required_path_request(
    path_parameter,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/required/path/{pathParameter}")
    path_format_arguments = {
        "pathParameter": _SERIALIZER.url("path_parameter", path_parameter, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_optional_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)
    _params = kwargs.pop("params", {}) or {}
    if isinstance(_params, dict):
        _params = case_insensitive_dict(_params)

    query_parameter = kwargs.pop('query_parameter', _params.pop('queryParameter', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/optional/query")

    # Construct parameters
    if query_parameter is not None:
        _params['queryParameter'] = _SERIALIZER.query("query_parameter", query_parameter, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_put_optional_header_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    query_parameter = kwargs.pop('query_parameter', _headers.pop('queryParameter', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/optional/header")

    # Construct headers
    if query_parameter is not None:
        _headers['queryParameter'] = _SERIALIZER.header("query_parameter", query_parameter, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_optional_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/optional/body")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_optional_binary_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/optional/binary-body")

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_required_global_path_request(
    required_global_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/global/required/path/{required-global-path}")
    path_format_arguments = {
        "required-global-path": _SERIALIZER.url("required_global_path", required_global_path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_get_required_global_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)
    _params = kwargs.pop("params", {}) or {}
    if isinstance(_params, dict):
        _params = case_insensitive_dict(_params)

    required_global_query = kwargs.pop('required_global_query')  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/global/required/query")

    # Construct parameters
    _params['required-global-query'] = _SERIALIZER.query("required_global_query", required_global_query, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_get_optional_global_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)
    _params = kwargs.pop("params", {}) or {}
    if isinstance(_params, dict):
        _params = case_insensitive_dict(_params)

    optional_global_query = kwargs.pop('optional_global_query', _params.pop('optional-global-query', None))  # type: Optional[int]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/global/optional/query")

    # Construct parameters
    if optional_global_query is not None:
        _params['optional-global-query'] = _SERIALIZER.query("optional_global_query", optional_global_query, 'int')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

# fmt: on
class ImplicitOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~requiredoptional.AutoRestRequiredOptionalTestService`'s
        :attr:`implicit` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_required_path(  # pylint: disable=inconsistent-return-statements
        self,
        path_parameter,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test implicitly required path parameter.

        :param path_parameter:
        :type path_parameter: str
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

        request = build_get_required_path_request(
            path_parameter=path_parameter,
            template_url=self.get_required_path.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_required_path.metadata = {"url": "/reqopt/implicit/required/path/{pathParameter}"}  # type: ignore

    @distributed_trace
    def put_optional_query(  # pylint: disable=inconsistent-return-statements
        self,
        query_parameter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test implicitly optional query parameter.

        :param query_parameter:  Default value is None.
        :type query_parameter: str
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

        request = build_put_optional_query_request(
            query_parameter=query_parameter,
            template_url=self.put_optional_query.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_optional_query.metadata = {"url": "/reqopt/implicit/optional/query"}  # type: ignore

    @distributed_trace
    def put_optional_header(  # pylint: disable=inconsistent-return-statements
        self,
        query_parameter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test implicitly optional header parameter.

        :param query_parameter:  Default value is None.
        :type query_parameter: str
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

        request = build_put_optional_header_request(
            query_parameter=query_parameter,
            template_url=self.put_optional_header.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_optional_header.metadata = {"url": "/reqopt/implicit/optional/header"}  # type: ignore

    @distributed_trace
    def put_optional_body(  # pylint: disable=inconsistent-return-statements
        self,
        body_parameter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test implicitly optional body parameter.

        :param body_parameter:  Default value is None.
        :type body_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        if body_parameter is not None:
            _json = self._serialize.body(body_parameter, "str")
        else:
            _json = None

        request = build_put_optional_body_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_optional_body.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_optional_body.metadata = {"url": "/reqopt/implicit/optional/body"}  # type: ignore

    @distributed_trace
    def put_optional_binary_body(  # pylint: disable=inconsistent-return-statements
        self,
        body_parameter=None,  # type: Optional[IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test implicitly optional body parameter.

        :param body_parameter:  Default value is None.
        :type body_parameter: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/octet-stream")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _content = body_parameter

        request = build_put_optional_binary_body_request(
            content_type=content_type,
            content=_content,
            template_url=self.put_optional_binary_body.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_optional_binary_body.metadata = {"url": "/reqopt/implicit/optional/binary-body"}  # type: ignore

    @distributed_trace
    def get_required_global_path(  # pylint: disable=inconsistent-return-statements
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test implicitly required path parameter.

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

        request = build_get_required_global_path_request(
            required_global_path=self._config.required_global_path,
            template_url=self.get_required_global_path.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_required_global_path.metadata = {"url": "/reqopt/global/required/path/{required-global-path}"}  # type: ignore

    @distributed_trace
    def get_required_global_query(  # pylint: disable=inconsistent-return-statements
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test implicitly required query parameter.

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

        request = build_get_required_global_query_request(
            required_global_query=self._config.required_global_query,
            template_url=self.get_required_global_query.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_required_global_query.metadata = {"url": "/reqopt/global/required/query"}  # type: ignore

    @distributed_trace
    def get_optional_global_query(  # pylint: disable=inconsistent-return-statements
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Test implicitly optional query parameter.

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

        request = build_get_optional_global_query_request(
            optional_global_query=self._config.optional_global_query,
            template_url=self.get_optional_global_query.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    get_optional_global_query.metadata = {"url": "/reqopt/global/optional/query"}  # type: ignore
