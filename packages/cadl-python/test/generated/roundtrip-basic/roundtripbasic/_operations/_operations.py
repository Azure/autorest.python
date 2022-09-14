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
    ResourceNotModifiedError,
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
from .._vendor import MixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_model_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/roundtrip-basic/models"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


class RoundTripBasicOperationsMixin(MixinABC):
    @overload
    def get_model(
        self, input: Union[_models.RoundTripModel, JSON], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RoundTripModel:
        """get_model.

        :param input: Required.
        :type input: ~roundtripbasic.models.RoundTripModel or JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoundTripModel. This object is compatible with MutableMapping
        :rtype: ~roundtripbasic.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def get_model(self, input: IO, *, content_type: str = "application/json", **kwargs: Any) -> _models.RoundTripModel:
        """get_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoundTripModel. This object is compatible with MutableMapping
        :rtype: ~roundtripbasic.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def get_model(self, input: Union[_models.RoundTripModel, JSON, IO], **kwargs: Any) -> _models.RoundTripModel:
        """get_model.

        :param input: Is either a model type or a IO type. Required.
        :type input: ~roundtripbasic.models.RoundTripModel or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: RoundTripModel. This object is compatible with MutableMapping
        :rtype: ~roundtripbasic.models.RoundTripModel
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

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoundTripModel]

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder)

        request = build_get_model_request(
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
            error = _deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error)

        deserialized = _deserialize(_models.RoundTripModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
