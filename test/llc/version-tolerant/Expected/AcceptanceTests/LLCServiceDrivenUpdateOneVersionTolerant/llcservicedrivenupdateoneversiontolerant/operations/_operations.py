# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, IO, Optional, TypeVar, Union
import warnings

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

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_params_get_required_request(
    *, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/servicedriven/parameters")

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["parameter"] = _SERIALIZER.query("parameter", parameter, "str")
    if new_parameter is not None:
        query_parameters["new_parameter"] = _SERIALIZER.query("new_parameter", new_parameter, "str")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, params=query_parameters, headers=header_parameters, **kwargs)


def build_params_post_parameters_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/servicedriven/parameters")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_params_delete_parameters_request(**kwargs: Any) -> HttpRequest:
    # Construct URL
    url = kwargs.pop("template_url", "/servicedriven/parameters")

    return HttpRequest(method="DELETE", url=url, **kwargs)


def build_params_get_new_operation_request(**kwargs: Any) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/servicedriven/newpath")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=url, headers=header_parameters, **kwargs)


class ParamsOperations(object):
    """ParamsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_required(self, *, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any) -> Any:
        """Get true Boolean value on path.

        :keyword parameter: I am a required parameter.
        :paramtype parameter: str
        :keyword new_parameter: I'm a new input optional parameter.
        :paramtype new_parameter: str
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_params_get_required_request(
            parameter=parameter,
            new_parameter=new_parameter,
            template_url=self.get_required.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_required.metadata = {"url": "/servicedriven/parameters"}  # type: ignore

    @distributed_trace
    def post_parameters(self, parameter: Union[IO, JSONType], **kwargs: Any) -> Any:
        """POST a JSON or a JPEG.

        :param parameter: I am a body parameter with a new content type. My only valid JSON entry is {
         url: "http://example.org/myimage.jpeg" }.
        :type parameter: IO or JSONType
        :keyword str content_type: Media type of the body sent to the API. Default value is
         "application/json". Allowed values are: "image/jpeg", "application/json."
        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = None
        _content = None
        if content_type.split(";")[0] in ["application/json"]:
            _json = parameter
        elif content_type.split(";")[0] in ["image/jpeg"]:
            _content = parameter
        else:
            raise ValueError(
                "The content_type '{}' is not one of the allowed values: "
                "['image/jpeg', 'application/json']".format(content_type)
            )

        request = build_params_post_parameters_request(
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.post_parameters.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    post_parameters.metadata = {"url": "/servicedriven/parameters"}  # type: ignore

    @distributed_trace
    def delete_parameters(self, **kwargs: Any) -> None:
        """Delete something.

        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_params_delete_parameters_request(
            template_url=self.delete_parameters.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    delete_parameters.metadata = {"url": "/servicedriven/parameters"}  # type: ignore

    @distributed_trace
    def get_new_operation(self, **kwargs: Any) -> Any:
        """I'm a new operation.

        :return: any
        :rtype: any
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_params_get_new_operation_request(
            template_url=self.get_new_operation.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_new_operation.metadata = {"url": "/servicedriven/newpath"}  # type: ignore
