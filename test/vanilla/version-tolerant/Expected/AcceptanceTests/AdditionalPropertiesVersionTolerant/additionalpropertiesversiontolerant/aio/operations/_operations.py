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

from ...operations._operations import (
    build_pets_create_ap_in_properties_request,
    build_pets_create_ap_in_properties_with_ap_string_request,
    build_pets_create_ap_object_request,
    build_pets_create_ap_string_request,
    build_pets_create_ap_true_request,
    build_pets_create_cat_ap_true_request,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~additionalpropertiesversiontolerant.aio.AdditionalPropertiesClient`'s
        :attr:`~additionalpropertiesversiontolerant.aio.AdditionalPropertiesClient.pets` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def create_ap_true(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
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

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
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

    @distributed_trace_async
    async def create_cat_ap_true(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
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

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
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

    @distributed_trace_async
    async def create_ap_object(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
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

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
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

    @distributed_trace_async
    async def create_ap_string(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
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

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
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

    @distributed_trace_async
    async def create_ap_in_properties(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
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

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
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

    @distributed_trace_async
    async def create_ap_in_properties_with_ap_string(self, create_parameters: JSONType, **kwargs: Any) -> JSONType:
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

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
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
