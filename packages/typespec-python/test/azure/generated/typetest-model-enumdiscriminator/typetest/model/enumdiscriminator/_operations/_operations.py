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
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import EnumDiscriminatorClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_enum_discriminator_get_extensible_model_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/enum-discriminator/extensible-enum"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_enum_discriminator_put_extensible_model_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/inheritance/enum-discriminator/extensible-enum"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_enum_discriminator_get_extensible_model_missing_discriminator_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/enum-discriminator/extensible-enum/missingdiscriminator"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_enum_discriminator_get_extensible_model_wrong_discriminator_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/enum-discriminator/extensible-enum/wrongdiscriminator"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_enum_discriminator_get_fixed_model_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/enum-discriminator/fixed-enum"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_enum_discriminator_put_fixed_model_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    # Construct URL
    _url = "/type/model/inheritance/enum-discriminator/fixed-enum"

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


def build_enum_discriminator_get_fixed_model_missing_discriminator_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/enum-discriminator/fixed-enum/missingdiscriminator"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


def build_enum_discriminator_get_fixed_model_wrong_discriminator_request(  # pylint: disable=name-too-long
    **kwargs: Any,
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/type/model/inheritance/enum-discriminator/fixed-enum/wrongdiscriminator"

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, headers=_headers, **kwargs)


class EnumDiscriminatorClientOperationsMixin(EnumDiscriminatorClientMixinABC):

    @distributed_trace
    def get_extensible_model(self, **kwargs: Any) -> _models.Dog:
        """Receive model with extensible enum discriminator type.

        :return: Dog. The Dog is compatible with MutableMapping
        :rtype: ~typetest.model.enumdiscriminator.models.Dog
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "golden":
                dog = {
                    "kind": "golden",
                    "weight": 0
                }

                # response body for status code(s): 200
                response == dog
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

        cls: ClsType[_models.Dog] = kwargs.pop("cls", None)

        _request = build_enum_discriminator_get_extensible_model_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.Dog, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put_extensible_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.Dog, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Send model with extensible enum discriminator type.

        :param input: Dog to create. Required.
        :type input: ~typetest.model.enumdiscriminator.models.Dog
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "golden":
                dog = {
                    "kind": "golden",
                    "weight": 0
                }

                # JSON input template you can fill out and use as your body input.
                input = dog
        """

    @overload
    def put_extensible_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Send model with extensible enum discriminator type.

        :param input: Dog to create. Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put_extensible_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Send model with extensible enum discriminator type.

        :param input: Dog to create. Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put_extensible_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.Dog, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """Send model with extensible enum discriminator type.

        :param input: Dog to create. Is one of the following types: Dog, JSON, IO[bytes] Required.
        :type input: ~typetest.model.enumdiscriminator.models.Dog or JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "golden":
                dog = {
                    "kind": "golden",
                    "weight": 0
                }

                # JSON input template you can fill out and use as your body input.
                input = dog
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
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_enum_discriminator_put_extensible_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

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
    def get_extensible_model_missing_discriminator(self, **kwargs: Any) -> _models.Dog:  # pylint: disable=name-too-long
        """Get a model omitting the discriminator.

        :return: Dog. The Dog is compatible with MutableMapping
        :rtype: ~typetest.model.enumdiscriminator.models.Dog
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "golden":
                dog = {
                    "kind": "golden",
                    "weight": 0
                }

                # response body for status code(s): 200
                response == dog
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

        cls: ClsType[_models.Dog] = kwargs.pop("cls", None)

        _request = build_enum_discriminator_get_extensible_model_missing_discriminator_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.Dog, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_extensible_model_wrong_discriminator(self, **kwargs: Any) -> _models.Dog:
        """Get a model containing discriminator value never defined.

        :return: Dog. The Dog is compatible with MutableMapping
        :rtype: ~typetest.model.enumdiscriminator.models.Dog
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "golden":
                dog = {
                    "kind": "golden",
                    "weight": 0
                }

                # response body for status code(s): 200
                response == dog
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

        cls: ClsType[_models.Dog] = kwargs.pop("cls", None)

        _request = build_enum_discriminator_get_extensible_model_wrong_discriminator_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.Dog, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_fixed_model(self, **kwargs: Any) -> _models.Snake:
        """Receive model with fixed enum discriminator type.

        :return: Snake. The Snake is compatible with MutableMapping
        :rtype: ~typetest.model.enumdiscriminator.models.Snake
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "cobra":
                snake = {
                    "kind": "cobra",
                    "length": 0
                }

                # response body for status code(s): 200
                response == snake
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

        cls: ClsType[_models.Snake] = kwargs.pop("cls", None)

        _request = build_enum_discriminator_get_fixed_model_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.Snake, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def put_fixed_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.Snake, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Send model with fixed enum discriminator type.

        :param input: Snake to create. Required.
        :type input: ~typetest.model.enumdiscriminator.models.Snake
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "cobra":
                snake = {
                    "kind": "cobra",
                    "length": 0
                }

                # JSON input template you can fill out and use as your body input.
                input = snake
        """

    @overload
    def put_fixed_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Send model with fixed enum discriminator type.

        :param input: Snake to create. Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def put_fixed_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Send model with fixed enum discriminator type.

        :param input: Snake to create. Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def put_fixed_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.Snake, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """Send model with fixed enum discriminator type.

        :param input: Snake to create. Is one of the following types: Snake, JSON, IO[bytes] Required.
        :type input: ~typetest.model.enumdiscriminator.models.Snake or JSON or IO[bytes]
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "cobra":
                snake = {
                    "kind": "cobra",
                    "length": 0
                }

                # JSON input template you can fill out and use as your body input.
                input = snake
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
        if isinstance(input, (IOBase, bytes)):
            _content = input
        else:
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_enum_discriminator_put_fixed_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

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
    def get_fixed_model_missing_discriminator(self, **kwargs: Any) -> _models.Snake:
        """Get a model omitting the discriminator.

        :return: Snake. The Snake is compatible with MutableMapping
        :rtype: ~typetest.model.enumdiscriminator.models.Snake
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "cobra":
                snake = {
                    "kind": "cobra",
                    "length": 0
                }

                # response body for status code(s): 200
                response == snake
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

        cls: ClsType[_models.Snake] = kwargs.pop("cls", None)

        _request = build_enum_discriminator_get_fixed_model_missing_discriminator_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.Snake, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get_fixed_model_wrong_discriminator(self, **kwargs: Any) -> _models.Snake:
        """Get a model containing discriminator value never defined.

        :return: Snake. The Snake is compatible with MutableMapping
        :rtype: ~typetest.model.enumdiscriminator.models.Snake
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "cobra":
                snake = {
                    "kind": "cobra",
                    "length": 0
                }

                # response body for status code(s): 200
                response == snake
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

        cls: ClsType[_models.Snake] = kwargs.pop("cls", None)

        _request = build_enum_discriminator_get_fixed_model_wrong_discriminator_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
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
            deserialized = _deserialize(_models.Snake, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
