# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

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

from ...operations._operations import build_pet_add_pet_request, build_pet_get_by_pet_id_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
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
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_by_pet_id(self, pet_id: str, **kwargs: Any) -> JSON:
        """get pet by id.

        :param pet_id: Pet id. Required.
        :type pet_id: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "IntEnum": "str",  # Required. Known values are: "1", "2", and "3".
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Known values are: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", and "Sunday".
                    "name": "str"  # Optional. name.
                }
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

        cls: ClsType[JSON] = kwargs.pop("cls", None)

        request = build_pet_get_by_pet_id_request(
            pet_id=pet_id,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def add_pet(
        self, pet_param: Optional[JSON] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """add pet.

        :param pet_param: pet param. Default value is None.
        :type pet_param: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                pet_param = {
                    "IntEnum": "str",  # Required. Known values are: "1", "2", and "3".
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Known values are: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", and "Sunday".
                    "name": "str"  # Optional. name.
                }

                # response body for status code(s): 200
                response == {
                    "IntEnum": "str",  # Required. Known values are: "1", "2", and "3".
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Known values are: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", and "Sunday".
                    "name": "str"  # Optional. name.
                }
        """

    @overload
    async def add_pet(
        self, pet_param: Optional[IO] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """add pet.

        :param pet_param: pet param. Default value is None.
        :type pet_param: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "IntEnum": "str",  # Required. Known values are: "1", "2", and "3".
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Known values are: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", and "Sunday".
                    "name": "str"  # Optional. name.
                }
        """

    @distributed_trace_async
    async def add_pet(self, pet_param: Optional[Union[JSON, IO]] = None, **kwargs: Any) -> JSON:
        """add pet.

        :param pet_param: pet param. Is either a JSON type or a IO type. Default value is None.
        :type pet_param: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                pet_param = {
                    "IntEnum": "str",  # Required. Known values are: "1", "2", and "3".
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Known values are: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", and "Sunday".
                    "name": "str"  # Optional. name.
                }

                # response body for status code(s): 200
                response == {
                    "IntEnum": "str",  # Required. Known values are: "1", "2", and "3".
                    "DaysOfWeek": "Friday",  # Optional. Default value is "Friday". Type of Pet.
                      Known values are: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
                      "Saturday", and "Sunday".
                    "name": "str"  # Optional. name.
                }
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
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(pet_param, (IOBase, bytes)):
            _content = pet_param
        else:
            if pet_param is not None:
                _json = pet_param
            else:
                _json = None

        request = build_pet_add_pet_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)
