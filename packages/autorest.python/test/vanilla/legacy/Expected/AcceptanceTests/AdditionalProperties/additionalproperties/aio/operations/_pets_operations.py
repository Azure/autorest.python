# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ...operations._pets_operations import (
    build_create_ap_in_properties_request,
    build_create_ap_in_properties_with_ap_string_request,
    build_create_ap_object_request,
    build_create_ap_string_request,
    build_create_ap_true_request,
    build_create_cat_ap_true_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~additionalproperties.aio.AdditionalPropertiesClient`'s
        :attr:`pets` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_ap_true(
        self, create_parameters: _models.PetAPTrue, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPTrue:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPTrue
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_ap_true(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPTrue:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_ap_true(
        self, create_parameters: Union[_models.PetAPTrue, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPTrue:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPTrue type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPTrue or IO[bytes]
        :return: PetAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PetAPTrue] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPTrue")

        _request = build_create_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPTrue", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_cat_ap_true(
        self, create_parameters: _models.CatAPTrue, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CatAPTrue:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.CatAPTrue
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_cat_ap_true(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CatAPTrue:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_cat_ap_true(
        self, create_parameters: Union[_models.CatAPTrue, IO[bytes]], **kwargs: Any
    ) -> _models.CatAPTrue:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Is either a CatAPTrue type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.CatAPTrue or IO[bytes]
        :return: CatAPTrue or the result of cls(response)
        :rtype: ~additionalproperties.models.CatAPTrue
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CatAPTrue] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "CatAPTrue")

        _request = build_create_cat_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("CatAPTrue", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_ap_object(
        self, create_parameters: _models.PetAPObject, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPObject:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPObject
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_ap_object(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPObject:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_ap_object(
        self, create_parameters: Union[_models.PetAPObject, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPObject:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPObject type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPObject or IO[bytes]
        :return: PetAPObject or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPObject
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PetAPObject] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPObject")

        _request = build_create_ap_object_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPObject", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_ap_string(
        self, create_parameters: _models.PetAPString, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPString
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_ap_string(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_ap_string(
        self, create_parameters: Union[_models.PetAPString, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPString type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPString or IO[bytes]
        :return: PetAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PetAPString] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPString")

        _request = build_create_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPString", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_ap_in_properties(
        self, create_parameters: _models.PetAPInProperties, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPInProperties:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPInProperties
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_ap_in_properties(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPInProperties:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_ap_in_properties(
        self, create_parameters: Union[_models.PetAPInProperties, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPInProperties:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPInProperties type or a IO[bytes] type. Required.
        :type create_parameters: ~additionalproperties.models.PetAPInProperties or IO[bytes]
        :return: PetAPInProperties or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PetAPInProperties] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPInProperties")

        _request = build_create_ap_in_properties_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_ap_in_properties_with_ap_string(
        self,
        create_parameters: _models.PetAPInPropertiesWithAPString,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.PetAPInPropertiesWithAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.PetAPInPropertiesWithAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: Union[_models.PetAPInPropertiesWithAPString, IO[bytes]], **kwargs: Any
    ) -> _models.PetAPInPropertiesWithAPString:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a PetAPInPropertiesWithAPString type or a IO[bytes] type.
         Required.
        :type create_parameters: ~additionalproperties.models.PetAPInPropertiesWithAPString or
         IO[bytes]
        :return: PetAPInPropertiesWithAPString or the result of cls(response)
        :rtype: ~additionalproperties.models.PetAPInPropertiesWithAPString
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.PetAPInPropertiesWithAPString] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IOBase, bytes)):
            _content = create_parameters
        else:
            _json = self._serialize.body(create_parameters, "PetAPInPropertiesWithAPString")

        _request = build_create_ap_in_properties_with_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAPInPropertiesWithAPString", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
