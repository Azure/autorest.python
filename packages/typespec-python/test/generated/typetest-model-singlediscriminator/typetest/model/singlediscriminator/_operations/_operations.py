# pylint: disable=too-many-lines
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
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import AzureJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import SingleDiscriminatorClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_single_discriminator_get_model_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/single-discriminator/model"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_single_discriminator_put_model_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/inheritance/single-discriminator/model"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_single_discriminator_get_recursive_model_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/single-discriminator/recursivemodel"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_single_discriminator_put_recursive_model_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/inheritance/single-discriminator/recursivemodel"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_single_discriminator_get_missing_discriminator_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/single-discriminator/missingdiscriminator"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_single_discriminator_get_wrong_discriminator_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/single-discriminator/wrongdiscriminator"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_single_discriminator_get_legacy_model_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/single-discriminator/legacy-model"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


class SingleDiscriminatorClientOperationsMixin(SingleDiscriminatorClientMixinABC):
    @distributed_trace
    def get_model(self, **kwargs: Any) -> _models.Bird:
        """get_model.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Bird. The Bird is compatible with MutableMapping
        :rtype: ~typetest.model.singlediscriminator.models.Bird
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "eagle":
                bird = {
                    "kind": "eagle",
                    "wingspan": 0,  # Required.
                    "friends": [
                        bird
                    ],
                    "hate": {
                        "str": bird
                    },
                    "partner": bird
                }

                # JSON input template for discriminator value "goose":
                bird = {
                    "kind": "goose",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "seagull":
                bird = {
                    "kind": "seagull",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "sparrow":
                bird = {
                    "kind": "sparrow",
                    "wingspan": 0  # Required.
                }

                # response body for status code(s): 200
                response == bird
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

        cls: ClsType[_models.Bird] = kwargs.pop("cls", None)

        request = build_single_discriminator_get_model_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
            deserialized = _deserialize(_models.Bird, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.Bird, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: ~typetest.model.singlediscriminator.models.Bird
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "eagle":
                bird = {
                    "kind": "eagle",
                    "wingspan": 0,  # Required.
                    "friends": [
                        bird
                    ],
                    "hate": {
                        "str": bird
                    },
                    "partner": bird
                }

                # JSON input template for discriminator value "goose":
                bird = {
                    "kind": "goose",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "seagull":
                bird = {
                    "kind": "seagull",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "sparrow":
                bird = {
                    "kind": "sparrow",
                    "wingspan": 0  # Required.
                }

                # JSON input template you can fill out and use as your body input.
                input = bird
        """

    @overload
    def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.Bird, JSON, IO], **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Is one of the following types: Bird, JSON, IO Required.
        :type input: ~typetest.model.singlediscriminator.models.Bird or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "eagle":
                bird = {
                    "kind": "eagle",
                    "wingspan": 0,  # Required.
                    "friends": [
                        bird
                    ],
                    "hate": {
                        "str": bird
                    },
                    "partner": bird
                }

                # JSON input template for discriminator value "goose":
                bird = {
                    "kind": "goose",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "seagull":
                bird = {
                    "kind": "seagull",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "sparrow":
                bird = {
                    "kind": "sparrow",
                    "wingspan": 0  # Required.
                }

                # JSON input template you can fill out and use as your body input.
                input = bird
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        request = build_single_discriminator_put_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def get_recursive_model(self, **kwargs: Any) -> _models.Bird:
        """get_recursive_model.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Bird. The Bird is compatible with MutableMapping
        :rtype: ~typetest.model.singlediscriminator.models.Bird
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "eagle":
                bird = {
                    "kind": "eagle",
                    "wingspan": 0,  # Required.
                    "friends": [
                        bird
                    ],
                    "hate": {
                        "str": bird
                    },
                    "partner": bird
                }

                # JSON input template for discriminator value "goose":
                bird = {
                    "kind": "goose",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "seagull":
                bird = {
                    "kind": "seagull",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "sparrow":
                bird = {
                    "kind": "sparrow",
                    "wingspan": 0  # Required.
                }

                # response body for status code(s): 200
                response == bird
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

        cls: ClsType[_models.Bird] = kwargs.pop("cls", None)

        request = build_single_discriminator_get_recursive_model_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
            deserialized = _deserialize(_models.Bird, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put_recursive_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.Bird, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_recursive_model.

        :param input: Required.
        :type input: ~typetest.model.singlediscriminator.models.Bird
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "eagle":
                bird = {
                    "kind": "eagle",
                    "wingspan": 0,  # Required.
                    "friends": [
                        bird
                    ],
                    "hate": {
                        "str": bird
                    },
                    "partner": bird
                }

                # JSON input template for discriminator value "goose":
                bird = {
                    "kind": "goose",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "seagull":
                bird = {
                    "kind": "seagull",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "sparrow":
                bird = {
                    "kind": "sparrow",
                    "wingspan": 0  # Required.
                }

                # JSON input template you can fill out and use as your body input.
                input = bird
        """

    @overload
    def put_recursive_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_recursive_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put_recursive_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_recursive_model.

        :param input: Required.
        :type input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put_recursive_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.Bird, JSON, IO], **kwargs: Any
    ) -> None:
        """put_recursive_model.

        :param input: Is one of the following types: Bird, JSON, IO Required.
        :type input: ~typetest.model.singlediscriminator.models.Bird or JSON or IO
        :keyword content_type: Body parameter Content-Type. Known values are: application/json. Default
         value is None.
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "eagle":
                bird = {
                    "kind": "eagle",
                    "wingspan": 0,  # Required.
                    "friends": [
                        bird
                    ],
                    "hate": {
                        "str": bird
                    },
                    "partner": bird
                }

                # JSON input template for discriminator value "goose":
                bird = {
                    "kind": "goose",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "seagull":
                bird = {
                    "kind": "seagull",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "sparrow":
                bird = {
                    "kind": "sparrow",
                    "wingspan": 0  # Required.
                }

                # JSON input template you can fill out and use as your body input.
                input = bird
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=AzureJSONEncoder, exclude_readonly=True)  # type: ignore

        request = build_single_discriminator_put_recursive_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace
    def get_missing_discriminator(self, **kwargs: Any) -> _models.Bird:
        """get_missing_discriminator.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Bird. The Bird is compatible with MutableMapping
        :rtype: ~typetest.model.singlediscriminator.models.Bird
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "eagle":
                bird = {
                    "kind": "eagle",
                    "wingspan": 0,  # Required.
                    "friends": [
                        bird
                    ],
                    "hate": {
                        "str": bird
                    },
                    "partner": bird
                }

                # JSON input template for discriminator value "goose":
                bird = {
                    "kind": "goose",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "seagull":
                bird = {
                    "kind": "seagull",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "sparrow":
                bird = {
                    "kind": "sparrow",
                    "wingspan": 0  # Required.
                }

                # response body for status code(s): 200
                response == bird
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

        cls: ClsType[_models.Bird] = kwargs.pop("cls", None)

        request = build_single_discriminator_get_missing_discriminator_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
            deserialized = _deserialize(_models.Bird, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_wrong_discriminator(self, **kwargs: Any) -> _models.Bird:
        """get_wrong_discriminator.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Bird. The Bird is compatible with MutableMapping
        :rtype: ~typetest.model.singlediscriminator.models.Bird
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "eagle":
                bird = {
                    "kind": "eagle",
                    "wingspan": 0,  # Required.
                    "friends": [
                        bird
                    ],
                    "hate": {
                        "str": bird
                    },
                    "partner": bird
                }

                # JSON input template for discriminator value "goose":
                bird = {
                    "kind": "goose",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "seagull":
                bird = {
                    "kind": "seagull",
                    "wingspan": 0  # Required.
                }

                # JSON input template for discriminator value "sparrow":
                bird = {
                    "kind": "sparrow",
                    "wingspan": 0  # Required.
                }

                # response body for status code(s): 200
                response == bird
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

        cls: ClsType[_models.Bird] = kwargs.pop("cls", None)

        request = build_single_discriminator_get_wrong_discriminator_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
            deserialized = _deserialize(_models.Bird, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_legacy_model(self, **kwargs: Any) -> _models.Dinosaur:
        """get_legacy_model.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Dinosaur. The Dinosaur is compatible with MutableMapping
        :rtype: ~typetest.model.singlediscriminator.models.Dinosaur
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "t-rex":
                dinosaur = {
                    "kind": "t-rex",
                    "size": 0  # Required.
                }

                # response body for status code(s): 200
                response == dinosaur
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

        cls: ClsType[_models.Dinosaur] = kwargs.pop("cls", None)

        request = build_single_discriminator_get_legacy_model_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
            deserialized = _deserialize(_models.Dinosaur, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
