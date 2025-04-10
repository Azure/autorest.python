# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from collections.abc import MutableMapping
import datetime
from typing import Any, Callable, Dict, Optional, TypeVar
import uuid

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer
from .._vendor import RepeatabilityClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_repeatability_immediate_success_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/special-headers/repeatability/immediateSuccess"

    # Construct headers
    if "Repeatability-Request-ID" not in _headers:
        _headers["Repeatability-Request-ID"] = str(uuid.uuid4())
    if "Repeatability-First-Sent" not in _headers:
        _headers["Repeatability-First-Sent"] = _SERIALIZER.serialize_data(
            datetime.datetime.now(datetime.timezone.utc), "rfc-1123"
        )

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class RepeatabilityClientOperationsMixin(RepeatabilityClientMixinABC):

    @distributed_trace
    def immediate_success(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Check we recognize Repeatability-Request-ID and Repeatability-First-Sent.

        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_repeatability_immediate_success_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Repeatability-Result"] = self._deserialize(
            "str", response.headers.get("Repeatability-Result")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore
