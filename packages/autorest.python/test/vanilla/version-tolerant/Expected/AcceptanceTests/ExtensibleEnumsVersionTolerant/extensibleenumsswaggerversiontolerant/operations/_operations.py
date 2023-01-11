# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer
from .._vendor import _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_pet_get_by_pet_id_request(pet_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/extensibleenums/pet/{petId}"
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_pet_add_pet_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/extensibleenums/pet/addPet"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class PetOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~extensibleenumsswaggerversiontolerant.PetStoreInc`'s
        :attr:`pet` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_by_pet_id(self, pet_id: str, **kwargs: Any) -> JSON:
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

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    def add_pet(
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
    def add_pet(self, pet_param: Optional[IO] = None, *, content_type: str = "application/json", **kwargs: Any) -> JSON:
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

    @distributed_trace
    def add_pet(self, pet_param: Optional[Union[JSON, IO]] = None, **kwargs: Any) -> JSON:
        """add pet.

        :param pet_param: pet param. Is either a model type or a IO type. Default value is None.
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
        if isinstance(pet_param, (IO, bytes)):
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

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)
