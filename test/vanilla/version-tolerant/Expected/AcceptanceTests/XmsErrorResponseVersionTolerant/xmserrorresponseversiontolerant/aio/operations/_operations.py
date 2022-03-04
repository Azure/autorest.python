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
    build_pet_do_something_request,
    build_pet_get_pet_by_id_request,
    build_pet_has_models_param_request,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~xmserrorresponseversiontolerant.aio.XMSErrorResponseExtensions`'s
        :attr:`~xmserrorresponseversiontolerant.aio.XMSErrorResponseExtensions.pet` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_pet_by_id(self, pet_id: str, **kwargs: Any) -> Optional[JSONType]:
        """Gets pets by id.

        :param pet_id: pet id.
        :type pet_id: str
        :return: JSON object
        :rtype: JSONType or None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "aniType": "str",  # Optional.
                    "name": "str"  # Optional. Gets the Pet by id.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional[JSONType]]
        error_map = {
            401: ClientAuthenticationError,
            409: ResourceExistsError,
            400: HttpResponseError,
            404: lambda response: ResourceNotFoundError(response=response),
            501: HttpResponseError,
        }
        error_map.update(kwargs.pop("error_map", {}))

        request = build_pet_get_pet_by_id_request(
            pet_id=pet_id,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            if response.content:
                deserialized = response.json()
            else:
                deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def do_something(self, what_action: str, **kwargs: Any) -> JSONType:
        """Asks pet to do something.

        :param what_action: what action the pet should do.
        :type what_action: str
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "actionResponse": "str"  # Optional. action feedback.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: HttpResponseError,
        }
        error_map.update(kwargs.pop("error_map", {}))

        request = build_pet_do_something_request(
            what_action=what_action,
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
    async def has_models_param(  # pylint: disable=inconsistent-return-statements
        self, *, models: Optional[str] = "value1", **kwargs: Any
    ) -> None:
        """Ensure you can correctly deserialize the returned PetActionError and deserialization doesn't
        conflict with the input param name 'models'.

        :keyword models: Make sure model deserialization doesn't conflict with this param name, which
         has input name 'models'. Use client default value in call. Default value is "value1".
        :paramtype models: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: HttpResponseError,
        }
        error_map.update(kwargs.pop("error_map", {}))

        request = build_pet_has_models_param_request(
            models=models,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
