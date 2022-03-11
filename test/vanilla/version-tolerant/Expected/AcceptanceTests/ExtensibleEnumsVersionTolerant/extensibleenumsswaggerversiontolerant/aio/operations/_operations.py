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

from ...operations._operations import build_pet_add_pet_request, build_pet_get_by_pet_id_request

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~extensibleenumsswaggerversiontolerant.aio.PetStoreInc`'s
        :attr:`pet` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        args = list(args)
        self._client = args.pop(0) if args else kwargs.pop("client")
        self._config = args.pop(0) if args else kwargs.pop("config")
        self._serialize = args.pop(0) if args else kwargs.pop("serializer")
        self._deserialize = args.pop(0) if args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_by_pet_id(self, pet_id: str, **kwargs: Any) -> JSONType:
        """get pet by id.

        :param pet_id: Pet id.
        :type pet_id: str
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", "Sunday". Default value: "Friday".
                    "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                    "name": "str"  # Optional. name.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_pet_get_by_pet_id_request(
            pet_id=pet_id,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.json()

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def add_pet(self, pet_param: JSONType = None, **kwargs: Any) -> JSONType:
        """add pet.

        :param pet_param: pet param. Default value is None.
        :type pet_param: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                pet_param = {
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", "Sunday". Default value: "Friday".
                    "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                    "name": "str"  # Optional. name.
                }

                # response body for status code(s): 200
                response.json() == {
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Possible values include: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", "Sunday". Default value: "Friday".
                    "IntEnum": "str",  # Required. Possible values include: "1", "2", "3".
                    "name": "str"  # Optional. name.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        if pet_param is not None:
            _json = pet_param
        else:
            _json = None

        request = build_pet_add_pet_request(
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

        deserialized = response.json()

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
