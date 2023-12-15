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
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import SdkJSONEncoder, _deserialize
from ..._operations._operations import (
    build_nested_discriminator_get_missing_discriminator_request,
    build_nested_discriminator_get_model_request,
    build_nested_discriminator_get_recursive_model_request,
    build_nested_discriminator_get_wrong_discriminator_request,
    build_nested_discriminator_put_model_request,
    build_nested_discriminator_put_recursive_model_request,
)
from .._vendor import NestedDiscriminatorClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class NestedDiscriminatorClientOperationsMixin(NestedDiscriminatorClientMixinABC):
    async def get_model(self, **kwargs: Any) -> _models.Fish:
        """get_model.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Fish. The Fish is compatible with MutableMapping
        :rtype: ~typetest.model.nesteddiscriminator.models.Fish
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "salmon":
                fish = {
                    "age": 0,  # Required.
                    "kind": "salmon",
                    "friends": [
                        fish
                    ],
                    "hate": {
                        "str": fish
                    },
                    "partner": fish
                }

                # JSON input template for discriminator value "goblin":
                fish = {
                    "age": 0,  # Required.
                    "kind": "goblin"
                }

                # JSON input template for discriminator value "saw":
                fish = {
                    "age": 0,  # Required.
                    "kind": "saw"
                }

                # response body for status code(s): 200
                response == fish
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

        cls: ClsType[_models.Fish] = kwargs.pop("cls", None)

        _request = build_nested_discriminator_get_model_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Fish, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.Fish, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: ~typetest.model.nesteddiscriminator.models.Fish
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "salmon":
                fish = {
                    "age": 0,  # Required.
                    "kind": "salmon",
                    "friends": [
                        fish
                    ],
                    "hate": {
                        "str": fish
                    },
                    "partner": fish
                }

                # JSON input template for discriminator value "goblin":
                fish = {
                    "age": 0,  # Required.
                    "kind": "goblin"
                }

                # JSON input template for discriminator value "saw":
                fish = {
                    "age": 0,  # Required.
                    "kind": "saw"
                }

                # JSON input template you can fill out and use as your body input.
                input = fish
        """

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def put_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.Fish, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """put_model.

        :param input: Is one of the following types: Fish, JSON, IO[bytes] Required.
        :type input: ~typetest.model.nesteddiscriminator.models.Fish or JSON or IO[bytes]
        :keyword content_type: Body parameter's content type. Known values are application/json.
         Default value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "salmon":
                fish = {
                    "age": 0,  # Required.
                    "kind": "salmon",
                    "friends": [
                        fish
                    ],
                    "hate": {
                        "str": fish
                    },
                    "partner": fish
                }

                # JSON input template for discriminator value "goblin":
                fish = {
                    "age": 0,  # Required.
                    "kind": "goblin"
                }

                # JSON input template for discriminator value "saw":
                fish = {
                    "age": 0,  # Required.
                    "kind": "saw"
                }

                # JSON input template you can fill out and use as your body input.
                input = fish
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
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_nested_discriminator_put_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def get_recursive_model(self, **kwargs: Any) -> _models.Fish:
        """get_recursive_model.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Fish. The Fish is compatible with MutableMapping
        :rtype: ~typetest.model.nesteddiscriminator.models.Fish
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "salmon":
                fish = {
                    "age": 0,  # Required.
                    "kind": "salmon",
                    "friends": [
                        fish
                    ],
                    "hate": {
                        "str": fish
                    },
                    "partner": fish
                }

                # JSON input template for discriminator value "goblin":
                fish = {
                    "age": 0,  # Required.
                    "kind": "goblin"
                }

                # JSON input template for discriminator value "saw":
                fish = {
                    "age": 0,  # Required.
                    "kind": "saw"
                }

                # response body for status code(s): 200
                response == fish
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

        cls: ClsType[_models.Fish] = kwargs.pop("cls", None)

        _request = build_nested_discriminator_get_recursive_model_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Fish, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def put_recursive_model(  # pylint: disable=inconsistent-return-statements
        self, input: _models.Fish, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_recursive_model.

        :param input: Required.
        :type input: ~typetest.model.nesteddiscriminator.models.Fish
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "salmon":
                fish = {
                    "age": 0,  # Required.
                    "kind": "salmon",
                    "friends": [
                        fish
                    ],
                    "hate": {
                        "str": fish
                    },
                    "partner": fish
                }

                # JSON input template for discriminator value "goblin":
                fish = {
                    "age": 0,  # Required.
                    "kind": "goblin"
                }

                # JSON input template for discriminator value "saw":
                fish = {
                    "age": 0,  # Required.
                    "kind": "saw"
                }

                # JSON input template you can fill out and use as your body input.
                input = fish
        """

    @overload
    async def put_recursive_model(  # pylint: disable=inconsistent-return-statements
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_recursive_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    @overload
    async def put_recursive_model(  # pylint: disable=inconsistent-return-statements
        self, input: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """put_recursive_model.

        :param input: Required.
        :type input: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """

    async def put_recursive_model(  # pylint: disable=inconsistent-return-statements
        self, input: Union[_models.Fish, JSON, IO[bytes]], **kwargs: Any
    ) -> None:
        """put_recursive_model.

        :param input: Is one of the following types: Fish, JSON, IO[bytes] Required.
        :type input: ~typetest.model.nesteddiscriminator.models.Fish or JSON or IO[bytes]
        :keyword content_type: Body parameter's content type. Known values are application/json.
         Default value is None.
        :paramtype content_type: str
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # The input is polymorphic. The following are possible polymorphic inputs based off
                  discriminator "kind":

                # JSON input template for discriminator value "salmon":
                fish = {
                    "age": 0,  # Required.
                    "kind": "salmon",
                    "friends": [
                        fish
                    ],
                    "hate": {
                        "str": fish
                    },
                    "partner": fish
                }

                # JSON input template for discriminator value "goblin":
                fish = {
                    "age": 0,  # Required.
                    "kind": "goblin"
                }

                # JSON input template for discriminator value "saw":
                fish = {
                    "age": 0,  # Required.
                    "kind": "saw"
                }

                # JSON input template you can fill out and use as your body input.
                input = fish
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
            _content = json.dumps(input, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_nested_discriminator_put_recursive_model_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    async def get_missing_discriminator(self, **kwargs: Any) -> _models.Fish:
        """get_missing_discriminator.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Fish. The Fish is compatible with MutableMapping
        :rtype: ~typetest.model.nesteddiscriminator.models.Fish
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "salmon":
                fish = {
                    "age": 0,  # Required.
                    "kind": "salmon",
                    "friends": [
                        fish
                    ],
                    "hate": {
                        "str": fish
                    },
                    "partner": fish
                }

                # JSON input template for discriminator value "goblin":
                fish = {
                    "age": 0,  # Required.
                    "kind": "goblin"
                }

                # JSON input template for discriminator value "saw":
                fish = {
                    "age": 0,  # Required.
                    "kind": "saw"
                }

                # response body for status code(s): 200
                response == fish
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

        cls: ClsType[_models.Fish] = kwargs.pop("cls", None)

        _request = build_nested_discriminator_get_missing_discriminator_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Fish, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def get_wrong_discriminator(self, **kwargs: Any) -> _models.Fish:
        """get_wrong_discriminator.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: Fish. The Fish is compatible with MutableMapping
        :rtype: ~typetest.model.nesteddiscriminator.models.Fish
        :raises ~corehttp.exceptions.HttpResponseError:

        Example:
            .. code-block:: python
                # The response is polymorphic. The following are possible polymorphic responses based
                  off discriminator "kind":

                # JSON input template for discriminator value "salmon":
                fish = {
                    "age": 0,  # Required.
                    "kind": "salmon",
                    "friends": [
                        fish
                    ],
                    "hate": {
                        "str": fish
                    },
                    "partner": fish
                }

                # JSON input template for discriminator value "goblin":
                fish = {
                    "age": 0,  # Required.
                    "kind": "goblin"
                }

                # JSON input template for discriminator value "saw":
                fish = {
                    "age": 0,  # Required.
                    "kind": "saw"
                }

                # response body for status code(s): 200
                response == fish
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

        cls: ClsType[_models.Fish] = kwargs.pop("cls", None)

        _request = build_nested_discriminator_get_wrong_discriminator_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client.pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Fish, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
