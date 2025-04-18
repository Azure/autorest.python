# coding=utf-8
from collections.abc import MutableMapping
from io import IOBase
import json
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .. import models as _models
from .._configuration import JsonMergePatchClientConfiguration
from .._utils.model_base import SdkJSONEncoder, _deserialize
from .._utils.serialization import Serializer
from .._utils.utils import ClientMixinABC

JSON = MutableMapping[str, Any]
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_json_merge_patch_create_resource_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/json-merge-patch/create/resource"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_json_merge_patch_update_resource_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/json-merge-patch/update/resource"

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, headers=_headers, **kwargs)


def build_json_merge_patch_update_optional_resource_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/json-merge-patch/update/resource/optional"

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, headers=_headers, **kwargs)


class JsonMergePatchClientOperationsMixin(ClientMixinABC[PipelineClient, JsonMergePatchClientConfiguration]):

    @overload
    def create_resource(
        self, body: _models.Resource, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: ~payload.jsonmergepatch.models.Resource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_resource(self, body: JSON, *, content_type: str = "application/json", **kwargs: Any) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def create_resource(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def create_resource(self, body: Union[_models.Resource, JSON, IO[bytes]], **kwargs: Any) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Is one of the following types: Resource, JSON, IO[bytes] Required.
        :type body: ~payload.jsonmergepatch.models.Resource or JSON or IO[bytes]
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Resource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_json_merge_patch_create_resource_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Resource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update_resource(
        self, body: _models.ResourcePatch, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: ~payload.jsonmergepatch.models.ResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update_resource(
        self, body: JSON, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update_resource(
        self, body: IO[bytes], *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update_resource(self, body: Union[_models.ResourcePatch, JSON, IO[bytes]], **kwargs: Any) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Is one of the following types: ResourcePatch, JSON, IO[bytes] Required.
        :type body: ~payload.jsonmergepatch.models.ResourcePatch or JSON or IO[bytes]
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[_models.Resource] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_json_merge_patch_update_resource_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Resource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def update_optional_resource(
        self,
        body: Optional[_models.ResourcePatch] = None,
        *,
        content_type: str = "application/merge-patch+json",
        **kwargs: Any,
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with optional body.

        :param body: Default value is None.
        :type body: ~payload.jsonmergepatch.models.ResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update_optional_resource(
        self, body: Optional[JSON] = None, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with optional body.

        :param body: Default value is None.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    def update_optional_resource(
        self, body: Optional[IO[bytes]] = None, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with optional body.

        :param body: Default value is None.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    def update_optional_resource(
        self, body: Optional[Union[_models.ResourcePatch, JSON, IO[bytes]]] = None, **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with optional body.

        :param body: Is one of the following types: ResourcePatch, JSON, IO[bytes] Default value is
         None.
        :type body: ~payload.jsonmergepatch.models.ResourcePatch or JSON or IO[bytes]
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map: MutableMapping = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[_models.Resource] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            if body is not None:
                _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore
            else:
                _content = None

        _request = build_json_merge_patch_update_optional_resource_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(_request, stream=_stream, **kwargs)

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Resource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
