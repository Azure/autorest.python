# pylint: disable=too-many-lines
# coding=utf-8

from typing import Any, Callable, Dict, Iterable, List, Optional, TypeVar

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.paging import ItemPaged
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import _deserialize
from .._serialization import Serializer
from .._vendor import PageableClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_pageable_list_request(*, maxpagesize: Optional[int] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/payload/pageable"

    # Construct parameters
    if maxpagesize is not None:
        _params["maxpagesize"] = _SERIALIZER.query("maxpagesize", maxpagesize, "int")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class PageableClientOperationsMixin(PageableClientMixinABC):
    def list(self, **kwargs: Any) -> Iterable["_models.User"]:
        """List users.

        :return: An iterator like instance of User
        :rtype: ~corehttp.paging.ItemPaged[~payload.pageable.models.User]
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        maxpagesize = kwargs.pop("maxpagesize", None)
        cls: ClsType[List[_models.User]] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_pageable_list_request(
                    maxpagesize=maxpagesize,
                    headers=_headers,
                    params=_params,
                )
                _request.url = self._client.format_url(_request.url)

            else:
                _request = HttpRequest("GET", next_link)
                _request.url = self._client.format_url(_request.url)

            return _request

        def extract_data(pipeline_response):
            deserialized = pipeline_response.http_response.json()
            list_of_elem = _deserialize(List[_models.User], deserialized["value"])
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.get("nextLink") or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                if _stream:
                    response.read()  # Load the body in memory and close the socket
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return ItemPaged(get_next, extract_data)
