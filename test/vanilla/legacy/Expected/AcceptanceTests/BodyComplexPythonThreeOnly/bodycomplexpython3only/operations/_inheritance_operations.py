# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Serializer

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
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_valid_request(**kwargs: Any) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/inheritance/valid")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_put_valid_request(*, json: JSONType = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    _headers = kwargs.pop("headers", {}) or {}
    if isinstance(_headers, dict):
        _headers = case_insensitive_dict(_headers)

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/complex/inheritance/valid")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, json=json, content=content, **kwargs)


class InheritanceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodycomplexpython3only.AutoRestComplexTestService`'s
        :attr:`inheritance` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get_valid(self, **kwargs: Any) -> "_models.Siamese":
        """Get complex types that extend others.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Siamese, or the result of cls(response)
        :rtype: ~bodycomplexpython3only.models.Siamese
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.Siamese"]

        request = build_get_valid_request(
            template_url=self.get_valid.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("Siamese", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_valid.metadata = {"url": "/complex/inheritance/valid"}  # type: ignore

    @distributed_trace
    def put_valid(  # pylint: disable=inconsistent-return-statements
        self, complex_body: "_models.Siamese", **kwargs: Any
    ) -> None:
        """Put complex types that extend others.

        :param complex_body: Please put a siamese with id=2, name="Siameee", color=green,
         breed=persion, which hates 2 dogs, the 1st one named "Potato" with id=1 and food="tomato", and
         the 2nd one named "Tomato" with id=-1 and food="french fries".
        :type complex_body: ~bodycomplexpython3only.models.Siamese
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        content_type = kwargs.pop(
            "content_type", _headers.pop("Content-Type", "application/json")
        )  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        _json = self._serialize.body(complex_body, "Siamese")

        request = build_put_valid_request(
            content_type=content_type,
            json=_json,
            template_url=self.put_valid.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    put_valid.metadata = {"url": "/complex/inheritance/valid"}  # type: ignore
