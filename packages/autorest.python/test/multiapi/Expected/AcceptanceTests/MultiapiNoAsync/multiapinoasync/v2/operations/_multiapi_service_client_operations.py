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
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import MultiapiServiceClientMixinABC, _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_test_one_request(*, id: int, message: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2.0.0"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/multiapi/testOneEndpoint")

    # Construct parameters
    _params["id"] = _SERIALIZER.query("id", id, "int")
    if message is not None:
        _params["message"] = _SERIALIZER.query("message", message, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_test_different_calls_request(
    *, greeting_in_english: str, greeting_in_chinese: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2.0.0"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/multiapi/testDifferentCalls")

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["greetingInEnglish"] = _SERIALIZER.header("greeting_in_english", greeting_in_english, "str")
    if greeting_in_chinese is not None:
        _headers["greetingInChinese"] = _SERIALIZER.header("greeting_in_chinese", greeting_in_chinese, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class MultiapiServiceClientOperationsMixin(MultiapiServiceClientMixinABC):
    @distributed_trace
    def test_one(self, id: int, message: Optional[str] = None, **kwargs: Any) -> _models.ModelTwo:
        """TestOne should be in an SecondVersionOperationsMixin. Returns ModelTwo.

        :param id: An int parameter. Required.
        :type id: int
        :param message: An optional string parameter. Default value is None.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo or the result of cls(response)
        :rtype: ~multiapinoasync.v2.models.ModelTwo
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2.0.0"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ModelTwo]

        request = build_test_one_request(
            id=id,
            message=message,
            api_version=api_version,
            template_url=self.test_one.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ModelTwo", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    test_one.metadata = {"url": "/multiapi/testOneEndpoint"}  # type: ignore

    @distributed_trace
    def test_different_calls(  # pylint: disable=inconsistent-return-statements
        self, greeting_in_english: str, greeting_in_chinese: Optional[str] = None, **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test. Required.
        :type greeting_in_english: str
        :param greeting_in_chinese: pass in 'nihao' to pass test. Default value is None.
        :type greeting_in_chinese: str
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

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2.0.0"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_test_different_calls_request(
            greeting_in_english=greeting_in_english,
            greeting_in_chinese=greeting_in_chinese,
            api_version=api_version,
            template_url=self.test_different_calls.metadata["url"],
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
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    test_different_calls.metadata = {"url": "/multiapi/testDifferentCalls"}  # type: ignore
