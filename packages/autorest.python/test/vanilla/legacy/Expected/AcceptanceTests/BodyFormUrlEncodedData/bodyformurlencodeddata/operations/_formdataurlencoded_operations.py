# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Literal, Optional, TypeVar, Union

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

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_update_pet_with_form_request(pet_id: int, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = kwargs.pop("template_url", "/formsdataurlencoded/pet/add/{petId}")
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, "int"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_partial_constant_body_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = kwargs.pop("template_url", "/formsdataurlencoded/partialConstantBody")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class FormdataurlencodedOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodyformurlencodeddata.BodyFormsDataURLEncoded`'s
        :attr:`formdataurlencoded` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def update_pet_with_form(  # pylint: disable=inconsistent-return-statements
        self,
        pet_id: int,
        pet_type: Union[str, _models.PetType],
        pet_food: Union[str, _models.PetFood],
        pet_age: int,
        name: Optional[str] = None,
        status: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Updates a pet in the store with form data.

        Updates a pet in the store with form data.

        :param pet_id: ID of pet that needs to be updated. Required.
        :type pet_id: int
        :param pet_type: Can take a value of dog, or cat, or fish. Known values are: "dog", "cat", and
         "fish". Required.
        :type pet_type: str or ~bodyformurlencodeddata.models.PetType
        :param pet_food: Can take a value of meat, or fish, or plant. Known values are: "meat", "fish",
         and "plant". Required.
        :type pet_food: str or ~bodyformurlencodeddata.models.PetFood
        :param pet_age: How many years is it old?. Required.
        :type pet_age: int
        :param name: Updated name of the pet. Default value is None.
        :type name: str
        :param status: Updated status of the pet. Default value is None.
        :type status: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        content_type: str = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        # Construct form data
        _data = {
            "pet_type": pet_type,
            "pet_food": pet_food,
            "pet_age": pet_age,
            "name": name,
            "status": status,
        }

        _request = build_update_pet_with_form_request(
            pet_id=pet_id,
            content_type=content_type,
            data=_data,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 405]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def partial_constant_body(  # pylint: disable=inconsistent-return-statements
        self, service: str, access_token: str, **kwargs: Any
    ) -> None:
        """Test a partially constant formdata body. Pass in { grant_type: 'access_token', access_token:
        'foo', service: 'bar' } to pass the test.

        :param service: Indicates the name of your Azure container registry. Required.
        :type service: str
        :param access_token: AAD access token, mandatory when grant_type is access_token_refresh_token
         or access_token. Required.
        :type access_token: str
        :keyword grant_type: Constant part of a formdata body. Default value is "access_token". Note
         that overriding this default value may result in unsupported behavior.
        :paramtype grant_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        content_type: str = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/x-www-form-urlencoded")
        )
        grant_type: Literal["access_token"] = kwargs.pop("grant_type", "access_token")
        cls: ClsType[None] = kwargs.pop("cls", None)

        # Construct form data
        _data = {
            "grant_type": grant_type,
            "service": service,
            "access_token": access_token,
        }

        _request = build_partial_constant_body_request(
            content_type=content_type,
            data=_data,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
