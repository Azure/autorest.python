# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

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

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_model_in_operation_input_to_input_output_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/azure/client-generator-core/usage/inputToInputOutput"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


def build_model_in_operation_output_to_input_output_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/client-generator-core/usage/outputToInputOutput"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_model_in_operation_model_in_read_only_property_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/azure/client-generator-core/usage/modelInReadOnlyProperty"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class ModelInOperationOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~specs.azure.clientgenerator.core.usage.UsageClient`'s
        :attr:`model_in_operation` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def input_to_input_output(  # pylint: disable=inconsistent-return-statements
        self, body: _models.InputModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Expected body parameter:

        .. code-block:: json

           {
             "name": <any string>
           }.

        :param body: Required.
        :type body: ~specs.azure.clientgenerator.core.usage.models.InputModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str"
                }
        """

    @overload
    def input_to_input_output(  # pylint: disable=inconsistent-return-statements
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Expected body parameter:

        .. code-block:: json

           {
             "name": <any string>
           }.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def input_to_input_output(  # pylint: disable=inconsistent-return-statements
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Expected body parameter:

        .. code-block:: json

           {
             "name": <any string>
           }.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def input_to_input_output(  # pylint: disable=inconsistent-return-statements
        self, body: Union[_models.InputModel, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """Expected body parameter:

        .. code-block:: json

           {
             "name": <any string>
           }.

        :param body: Is one of the following types: InputModel, JSON, IO[bytes] Required.
        :type body: ~specs.azure.clientgenerator.core.usage.models.InputModel or JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str"
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
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_model_in_operation_input_to_input_output_request(
            content_type=content_type,
            content=_content,
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

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def output_to_input_output(self, **kwargs: Any) -> _models.OutputModel:
        """Expected response body:

        .. code-block:: json

           {
             "name": <any string>
           }.

        :return: OutputModel. The OutputModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.OutputModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str"
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.OutputModel] = kwargs.pop("cls", None)

        _request = build_model_in_operation_output_to_input_output_request(
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
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
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.OutputModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def model_in_read_only_property(
        self, body: _models.RoundTripModel, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RoundTripModel:
        """ "ResultModel" should be usage=output, as it is read-only and does not exist in request body.

        Expected body parameter:

        .. code-block:: json

           {
           }

        Expected response body:

        .. code-block:: json

           {
             "result": {
               "name": <any string>
             }
           }.

        :param body: Required.
        :type body: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoundTripModel. The RoundTripModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "result": {
                        "name": "str"
                    }
                }

                # response body for status code(s): 200
                response == {
                    "result": {
                        "name": "str"
                    }
                }
        """

    @overload
    def model_in_read_only_property(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RoundTripModel:
        """ "ResultModel" should be usage=output, as it is read-only and does not exist in request body.

        Expected body parameter:

        .. code-block:: json

           {
           }

        Expected response body:

        .. code-block:: json

           {
             "result": {
               "name": <any string>
             }
           }.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoundTripModel. The RoundTripModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "result": {
                        "name": "str"
                    }
                }
        """

    @overload
    def model_in_read_only_property(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.RoundTripModel:
        """ "ResultModel" should be usage=output, as it is read-only and does not exist in request body.

        Expected body parameter:

        .. code-block:: json

           {
           }

        Expected response body:

        .. code-block:: json

           {
             "result": {
               "name": <any string>
             }
           }.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: RoundTripModel. The RoundTripModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "result": {
                        "name": "str"
                    }
                }
        """

    @distributed_trace
    def model_in_read_only_property(
        self, body: Union[_models.RoundTripModel, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.RoundTripModel:
        """ "ResultModel" should be usage=output, as it is read-only and does not exist in request body.

        Expected body parameter:

        .. code-block:: json

           {
           }

        Expected response body:

        .. code-block:: json

           {
             "result": {
               "name": <any string>
             }
           }.

        :param body: Is one of the following types: RoundTripModel, JSON, IO[bytes] Required.
        :type body: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel or JSON or IO[bytes]
        :return: RoundTripModel. The RoundTripModel is compatible with MutableMapping
        :rtype: ~specs.azure.clientgenerator.core.usage.models.RoundTripModel
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "result": {
                        "name": "str"
                    }
                }

                # response body for status code(s): 200
                response == {
                    "result": {
                        "name": "str"
                    }
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
        cls: ClsType[_models.RoundTripModel] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_model_in_operation_model_in_read_only_property_request(
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
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.RoundTripModel, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
