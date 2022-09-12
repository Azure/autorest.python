# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

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

from .._serialization import Serializer
from .._vendor import _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_params_head_no_params_request(*, new_parameter: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    # Construct URL
    _url = "/serviceDriven2/serviceDriven/parameters"

    # Construct parameters
    if new_parameter is not None:
        _params["new_parameter"] = _SERIALIZER.query("new_parameter", new_parameter, "str")

    return HttpRequest(method="HEAD", url=_url, params=_params, **kwargs)


def build_params_get_required_request(
    *, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/serviceDriven2/serviceDriven/parameters"

    # Construct parameters
    _params["parameter"] = _SERIALIZER.query("parameter", parameter, "str")
    if new_parameter is not None:
        _params["new_parameter"] = _SERIALIZER.query("new_parameter", new_parameter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_params_put_required_optional_request(
    *, required_param: str, optional_param: Optional[str] = None, new_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/serviceDriven2/serviceDriven/parameters"

    # Construct parameters
    _params["requiredParam"] = _SERIALIZER.query("required_param", required_param, "str")
    if optional_param is not None:
        _params["optionalParam"] = _SERIALIZER.query("optional_param", optional_param, "str")
    if new_parameter is not None:
        _params["new_parameter"] = _SERIALIZER.query("new_parameter", new_parameter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_params_post_parameters_request(content_type_path: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/serviceDriven2/serviceDriven/parameters/{contentTypePath}"
    path_format_arguments = {
        "contentTypePath": _SERIALIZER.url("content_type_path", content_type_path, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_params_delete_parameters_request(**kwargs: Any) -> HttpRequest:
    # Construct URL
    _url = "/serviceDriven2/serviceDriven/parameters"

    return HttpRequest(method="DELETE", url=_url, **kwargs)


def build_params_get_optional_request(
    *, optional_param: Optional[str] = None, new_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/serviceDriven2/serviceDriven/moreParameters"

    # Construct parameters
    if optional_param is not None:
        _params["optionalParam"] = _SERIALIZER.query("optional_param", optional_param, "str")
    if new_parameter is not None:
        _params["new_parameter"] = _SERIALIZER.query("new_parameter", new_parameter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_params_get_new_operation_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/serviceDriven2/serviceDriven/newPath"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


class ParamsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~resiliency.servicedriven2.ResiliencyServiceDriven2`'s
        :attr:`params` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def head_no_params(self, *, new_parameter: Optional[str] = None, **kwargs: Any) -> bool:
        """Head request, no params.
         Initially has no query parameters. After evolution, a new optional query parameter is added.

        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: bool
        :rtype: bool
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
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_params_head_no_params_request(
            new_parameter=new_parameter,
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

        if cls:
            return cls(pipeline_response, None, {})
        return 200 <= response.status_code <= 299

    @distributed_trace
    def get_required(self, *, parameter: str, new_parameter: Optional[str] = None, **kwargs: Any) -> JSON:
        """Get true Boolean value on path.
         Initially only has one required Query Parameter. After evolution, a new optional query
        parameter is added.

        :keyword parameter: I am a required parameter. Required.
        :paramtype parameter: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "message": "str"  # Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_params_get_required_request(
            parameter=parameter,
            new_parameter=new_parameter,
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @distributed_trace
    def put_required_optional(
        self,
        *,
        required_param: str,
        optional_param: Optional[str] = None,
        new_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> JSON:
        """Initially has one required query parameter and one optional query parameter.  After evolution,
        a new optional query parameter is added.

        :keyword required_param: I am a required parameter. Required.
        :paramtype required_param: str
        :keyword optional_param: I am an optional parameter. Default value is None.
        :paramtype optional_param: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "message": "str"  # Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_params_put_required_optional_request(
            required_param=required_param,
            optional_param=optional_param,
            new_parameter=new_parameter,
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    def post_parameters(
        self, content_type_path: str, parameter: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """POST a JSON or a JPEG.

        :param content_type_path: Known values are: "json" and "jpeg". Required.
        :type content_type_path: str
        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Required.
        :type parameter: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                parameter = {
                    "url": "str"  # Required.
                }

                # response body for status code(s): 200
                response == {
                    "message": "str"  # Required.
                }
        """

    @overload
    def post_parameters(
        self, content_type_path: str, parameter: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """POST a JSON or a JPEG.

        :param content_type_path: Known values are: "json" and "jpeg". Required.
        :type content_type_path: str
        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Required.
        :type parameter: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "message": "str"  # Required.
                }
        """

    @distributed_trace
    def post_parameters(self, content_type_path: str, parameter: Union[JSON, IO], **kwargs: Any) -> JSON:
        """POST a JSON or a JPEG.

        :param content_type_path: Known values are: "json" and "jpeg". Required.
        :type content_type_path: str
        :param parameter: I am a body parameter. My only valid JSON entry is { url:
         "http://example.org/myimage.jpeg" }. Is either a model type or a IO type. Required.
        :type parameter: JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "message": "str"  # Required.
                }
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
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameter, (IO, bytes)):
            _content = parameter
        else:
            _json = parameter

        request = build_params_post_parameters_request(
            content_type_path=content_type_path,
            content_type=content_type,
            json=_json,
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @distributed_trace
    def delete_parameters(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Delete something.
         Initially the path exists but there is no delete method. After evolution this is a new method
        in a known path.

        :return: None
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
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_params_delete_parameters_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def get_optional(
        self, *, optional_param: Optional[str] = None, new_parameter: Optional[str] = None, **kwargs: Any
    ) -> JSON:
        """Get true Boolean value on path.
         Initially has one optional query parameter. After evolution, a new optional query parameter is
        added.

        :keyword optional_param: I am an optional parameter. Default value is None.
        :paramtype optional_param: str
        :keyword new_parameter: I'm a new input optional parameter. Default value is None.
        :paramtype new_parameter: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "message": "str"  # Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_params_get_optional_request(
            optional_param=optional_param,
            new_parameter=new_parameter,
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @distributed_trace
    def get_new_operation(self, **kwargs: Any) -> JSON:
        """I'm a new operation.
         Initially neither path or method exist for this operation. After evolution, this is a new
        method in a new path.

        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "message": "str"  # Required.
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_params_get_new_operation_request(
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

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)
