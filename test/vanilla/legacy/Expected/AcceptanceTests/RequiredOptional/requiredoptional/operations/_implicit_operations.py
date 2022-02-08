# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

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
from msrest import Serializer

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
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/required/path/{pathParameter}")
    path_format_arguments = {
        "pathParameter": _SERIALIZER.url("path_parameter", path_parameter, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_put_optional_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    query_parameter = kwargs.pop('query_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/optional/query")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if query_parameter is not None:
        _query_parameters['queryParameter'] = _SERIALIZER.query("query_parameter", query_parameter, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_put_optional_header_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    query_parameter = kwargs.pop('query_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/optional/header")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if query_parameter is not None:
        _header_parameters['queryParameter'] = _SERIALIZER.header("query_parameter", query_parameter, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_put_optional_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/optional/body")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_put_optional_binary_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/implicit/optional/binary-body")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_get_required_global_path_request(
    required_global_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/global/required/path/{required-global-path}")
    path_format_arguments = {
        "required-global-path": _SERIALIZER.url("required_global_path", required_global_path, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_get_required_global_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    required_global_query = kwargs.pop('required_global_query')  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/global/required/query")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['required-global-query'] = _SERIALIZER.query("required_global_query", required_global_query, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_optional_global_query_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    optional_global_query = kwargs.pop('optional_global_query', None)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/reqopt/global/optional/query")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if optional_global_query is not None:
        _query_parameters['optional-global-query'] = _SERIALIZER.query("optional_global_query", optional_global_query, 'int')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class ImplicitOperations(object):
    """ImplicitOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~requiredoptional.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

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
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_required_path_request(
            path_parameter=path_parameter,
            template_url=self.get_required_path.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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

        :param query_parameter:
        :type query_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_put_optional_query_request(
            query_parameter=query_parameter,
            template_url=self.put_optional_query.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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

        :param query_parameter:
        :type query_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_put_optional_header_request(
            query_parameter=query_parameter,
            template_url=self.put_optional_header.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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

        :param body_parameter:
        :type body_parameter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if body_parameter is not None:
            _json = self._serialize.body(body_parameter, "str")
        else:
            _json = None

        request = build_put_optional_body_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_optional_body.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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

        :param body_parameter:
        :type body_parameter: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/octet-stream")  # type: Optional[str]

        _content = body_parameter

        request = build_put_optional_binary_body_request(
            content_type=content_type,
            content=_content,
            template_url=self.put_optional_binary_body.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_required_global_path_request(
            required_global_path=self._config.required_global_path,
            template_url=self.get_required_global_path.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_required_global_query_request(
            required_global_query=self._config.required_global_query,
            template_url=self.get_required_global_query.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_optional_global_query_request(
            optional_global_query=self._config.optional_global_query,
            template_url=self.get_optional_global_query.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
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
