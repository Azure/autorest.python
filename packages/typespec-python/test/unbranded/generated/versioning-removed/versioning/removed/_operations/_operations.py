# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import RemovedClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_removed_v2_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/v2"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class RemovedClientOperationsMixin(RemovedClientMixinABC):

    @overload
    def v2(self, body: _models.ModelV2, *, content_type: str = "application/json", **kwargs: Any) -> _models.ModelV2:
        """v2.

        :param body: Required.
        :type body: ~versioning.removed.models.ModelV2
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ModelV2. The ModelV2 is compatible with MutableMapping
        :rtype: ~versioning.removed.models.ModelV2
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "enumProp": "str",
                    "prop": "str",
                    "unionProp": "str"
                }

                # response body for status code(s): 200
                response == {
                    "enumProp": "str",
                    "prop": "str",
                    "unionProp": "str"
                }
        """

    @overload
    def v2(self, body: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.ModelV2:
        """v2.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ModelV2. The ModelV2 is compatible with MutableMapping
        :rtype: ~versioning.removed.models.ModelV2
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "enumProp": "str",
                    "prop": "str",
                    "unionProp": "str"
                }
        """

    @overload
    def v2(self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any) -> _models.ModelV2:
        """v2.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ModelV2. The ModelV2 is compatible with MutableMapping
        :rtype: ~versioning.removed.models.ModelV2
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "enumProp": "str",
                    "prop": "str",
                    "unionProp": "str"
                }
        """

    def v2(self, body: Union[_models.ModelV2, JSON, IO[bytes]], **kwargs: Any) -> _models.ModelV2:
        """v2.

        :param body: Is one of the following types: ModelV2, JSON, IO[bytes] Required.
        :type body: ~versioning.removed.models.ModelV2 or JSON or IO[bytes]
        :return: ModelV2. The ModelV2 is compatible with MutableMapping
        :rtype: ~versioning.removed.models.ModelV2
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "enumProp": "str",
                    "prop": "str",
                    "unionProp": "str"
                }

                # response body for status code(s): 200
                response == {
                    "enumProp": "str",
                    "prop": "str",
                    "unionProp": "str"
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ModelV2] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_removed_v2_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "version": self._serialize.url("self._config.version", self._config.version, "str"),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ModelV2, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
