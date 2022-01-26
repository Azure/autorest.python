# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
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


def build_pets_create_ap_true_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = "/additionalProperties/true"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_pets_create_cat_ap_true_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = "/additionalProperties/true-subclass"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_pets_create_ap_object_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = "/additionalProperties/type/object"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_pets_create_ap_string_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = "/additionalProperties/type/string"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_pets_create_ap_in_properties_request(
    *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = "/additionalProperties/in/properties"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_pets_create_ap_in_properties_with_ap_string_request(
    *, json: JSONType = None, content: Any = None, **kwargs: Any
) -> HttpRequest:
    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = "/additionalProperties/in/properties/with/additionalProperties/string"

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


class PetsOperations(object):
    """PetsOperations operations.

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
    def create_ap_true(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = create_parameters

        request = build_pets_create_ap_true_request(
            content_type=content_type,
            json=_json,
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

    @distributed_trace
    def create_cat_ap_true(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "friendly": bool,  # Optional.
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "friendly": bool,  # Optional.
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = create_parameters

        request = build_pets_create_cat_ap_true_request(
            content_type=content_type,
            json=_json,
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

    @distributed_trace
    def create_ap_object(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = create_parameters

        request = build_pets_create_ap_object_request(
            content_type=content_type,
            json=_json,
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

    @distributed_trace
    def create_ap_string(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = create_parameters

        request = build_pets_create_ap_string_request(
            content_type=content_type,
            json=_json,
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

    @distributed_trace
    def create_ap_in_properties(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = create_parameters

        request = build_pets_create_ap_in_properties_request(
            content_type=content_type,
            json=_json,
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

    @distributed_trace
    def create_ap_in_properties_with_ap_string(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters:
        :type create_parameters: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "@odata.location": "str",  # Required.
                    "additionalProperties": {
                        "str": 0.0  # Optional. Dictionary of :code:`<number>`.
                    },
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "@odata.location": "str",  # Required.
                    "additionalProperties": {
                        "str": 0.0  # Optional. Dictionary of :code:`<number>`.
                    },
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        _json = create_parameters

        request = build_pets_create_ap_in_properties_with_ap_string_request(
            content_type=content_type,
            json=_json,
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
