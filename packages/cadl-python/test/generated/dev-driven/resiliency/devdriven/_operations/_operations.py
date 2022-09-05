# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from .._model_base import AzureJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import MixinABC, _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_model_request(mode: Union[str, "_models.Mode"], **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/resilency/devdriven/customization/model/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_post_model_request(mode: Union[str, "_models.Mode"], **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/resilency/devdriven/customization/model/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_get_pages_request(*, api_version: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/resilency/devdriven"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str", min_length=1)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_lro_request(mode: Union[str, "_models.Mode"], **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/resilency/devdriven/customization/lro/{mode}"
    path_format_arguments = {
        "mode": _SERIALIZER.url("mode", mode, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class ResiliencyDevDrivenOperationsMixin(MixinABC):
    @distributed_trace
    def get_model(self, mode: Union[str, "_models.Mode"], **kwargs: Any) -> _models.Product:
        """Get models that you will either return to end users as a raw body, or with a model added during
        grow up.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :return: Product. This object is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Product]

        request = build_get_model_request(
            mode=mode,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = _deserialize(_models.Product, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @overload
    def post_model(
        self,
        mode: Union[str, "_models.Mode"],
        input: Union[_models.Input, JSON],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Required.
        :type input: ~resiliency.devdriven.models.Input or JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Product. This object is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def post_model(
        self, mode: Union[str, "_models.Mode"], input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Product. This object is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def post_model(
        self, mode: Union[str, "_models.Mode"], input: Union[_models.Input, JSON, IO], **kwargs: Any
    ) -> _models.Product:
        """Post either raw response as a model and pass in 'raw' for mode, or grow up your operation to
        take a model instead, and put in 'model' as mode.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :param input: Please put {'hello': 'world!'}. Is either a model type or a IO type. Required.
        :type input: ~resiliency.devdriven.models.Input or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: Product. This object is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.Product
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.Product]

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder)

        request = build_post_model_request(
            mode=mode,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = _deserialize(_models.Product, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace
    def get_pages(self, *, api_version: str, **kwargs: Any) -> _models.CustomPageProduct:
        """Get pages that you will either return to users in pages of raw bodies, or pages of models
        following growup.

        :keyword api_version: The API version to use for this operation. Required.
        :paramtype api_version: str
        :return: CustomPageProduct. This object is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.CustomPageProduct
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CustomPageProduct]

        request = build_get_pages_request(
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error)

        deserialized = _deserialize(_models.CustomPageProduct, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace
    def lro(self, mode: Union[str, "_models.Mode"], **kwargs: Any) -> _models.LROProduct:
        """Long running put request that will either return to end users a final payload of a raw body, or
        a final payload of a model after the SDK has grown up.

        :param mode: The mode with which you'll be handling your returned body. 'raw' for just dealing
         with the raw body, and 'model' if you are going to convert the raw body to a customized body
         before returning to users. Known values are: "raw" and "model". Required.
        :type mode: str or ~resiliency.devdriven.models.Mode
        :return: LROProduct. This object is compatible with MutableMapping
        :rtype: ~resiliency.devdriven.models.LROProduct
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[_models.LROProduct]

        request = build_lro_request(
            mode=mode,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = _deserialize(_models.LROProduct, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
