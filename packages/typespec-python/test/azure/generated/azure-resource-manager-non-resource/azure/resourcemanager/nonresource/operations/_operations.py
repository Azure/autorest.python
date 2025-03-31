# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core import PipelineClient
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    StreamClosedError,
    StreamConsumedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._configuration import NonResourceClientConfiguration
from .._model_base import SdkJSONEncoder, _deserialize, _failsafe_deserialize
from .._serialization import Deserializer, Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_non_resource_operations_get_request(  # pylint: disable=name-too-long
    location: str, parameter: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/providers/Microsoft.NonResource/locations/{location}/otherParameters/{parameter}"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "location": _SERIALIZER.url("location", location, "str"),
        "parameter": _SERIALIZER.url("parameter", parameter, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_non_resource_operations_create_request(  # pylint: disable=name-too-long
    location: str, parameter: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-12-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/subscriptions/{subscriptionId}/providers/Microsoft.NonResource/locations/{location}/otherParameters/{parameter}"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "location": _SERIALIZER.url("location", location, "str"),
        "parameter": _SERIALIZER.url("parameter", parameter, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


class NonResourceOperationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.resourcemanager.nonresource.NonResourceClient`'s
        :attr:`non_resource_operations` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: NonResourceClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(self, location: str, parameter: str, **kwargs: Any) -> _models.NonResource:
        """get.

        :param location: The location parameter. Required.
        :type location: str
        :param parameter: Another parameter. Required.
        :type parameter: str
        :return: NonResource. The NonResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.nonresource.models.NonResource
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

        cls: ClsType[_models.NonResource] = kwargs.pop("cls", None)

        _request = build_non_resource_operations_get_request(
            location=location,
            parameter=parameter,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.NonResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create(
        self,
        location: str,
        parameter: str,
        body: _models.NonResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NonResource:
        """create.

        :param location: The location parameter. Required.
        :type location: str
        :param parameter: Another parameter. Required.
        :type parameter: str
        :param body: The request body. Required.
        :type body: ~azure.resourcemanager.nonresource.models.NonResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NonResource. The NonResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.nonresource.models.NonResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, location: str, parameter: str, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NonResource:
        """create.

        :param location: The location parameter. Required.
        :type location: str
        :param parameter: Another parameter. Required.
        :type parameter: str
        :param body: The request body. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NonResource. The NonResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.nonresource.models.NonResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self, location: str, parameter: str, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.NonResource:
        """create.

        :param location: The location parameter. Required.
        :type location: str
        :param parameter: Another parameter. Required.
        :type parameter: str
        :param body: The request body. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NonResource. The NonResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.nonresource.models.NonResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self, location: str, parameter: str, body: Union[_models.NonResource, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.NonResource:
        """create.

        :param location: The location parameter. Required.
        :type location: str
        :param parameter: Another parameter. Required.
        :type parameter: str
        :param body: The request body. Is one of the following types: NonResource, JSON, IO[bytes]
         Required.
        :type body: ~azure.resourcemanager.nonresource.models.NonResource or JSON or IO[bytes]
        :return: NonResource. The NonResource is compatible with MutableMapping
        :rtype: ~azure.resourcemanager.nonresource.models.NonResource
        :raises ~azure.core.exceptions.HttpResponseError:
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
        cls: ClsType[_models.NonResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_non_resource_operations_create_request(
            location=location,
            parameter=parameter,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.base_url", self._config.base_url, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                try:
                    response.read()  # Load the body in memory and close the socket
                except (StreamConsumedError, StreamClosedError):
                    pass
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _failsafe_deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.NonResource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
