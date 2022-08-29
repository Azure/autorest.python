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
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ..._operations._operations import (
    build_get_optional_property_model_request,
    build_set_optional_property_model_request,
)
from .._vendor import MixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ReadonlyPropertiesOperationsMixin(MixinABC):
    @distributed_trace_async
    async def get_optional_property_model(self, **kwargs: Any) -> JSON:
        """get_optional_property_model.

        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "requiredReadonlyInt": 0,  # Required int, illustrating a readonly value type
                      property. Required.
                    "requiredReadonlyIntList": [
                        0  # Required readonly int collection. Required.
                    ],
                    "requiredReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "requiredReadonlyString": "str",  # Required string, illustrating a readonly
                      reference type property. Required.
                    "requiredReadonlyStringList": [
                        "str"  # Required readonly string collection. Required.
                    ],
                    "optionalReadonlyInt": 0,  # Optional. Optional int, illustrating a readonly
                      value type property.
                    "optionalReadonlyIntList": [
                        0  # Optional. Optional readonly int collection.
                    ],
                    "optionalReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "optionalReadonlyString": "str",  # Optional. Optional string, illustrating a
                      readonly reference type property.
                    "optionalReadonlyStringList": [
                        "str"  # Optional. Optional readonly string collection.
                    ]
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        request = build_get_optional_property_model_request(
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
    async def set_optional_property_model(
        self, input: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """set_optional_property_model.

        :param input: Required.
        :type input: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                input = {
                    "requiredReadonlyInt": 0,  # Required int, illustrating a readonly value type
                      property. Required.
                    "requiredReadonlyIntList": [
                        0  # Required readonly int collection. Required.
                    ],
                    "requiredReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "requiredReadonlyString": "str",  # Required string, illustrating a readonly
                      reference type property. Required.
                    "requiredReadonlyStringList": [
                        "str"  # Required readonly string collection. Required.
                    ],
                    "optionalReadonlyInt": 0,  # Optional. Optional int, illustrating a readonly
                      value type property.
                    "optionalReadonlyIntList": [
                        0  # Optional. Optional readonly int collection.
                    ],
                    "optionalReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "optionalReadonlyString": "str",  # Optional. Optional string, illustrating a
                      readonly reference type property.
                    "optionalReadonlyStringList": [
                        "str"  # Optional. Optional readonly string collection.
                    ]
                }

                # response body for status code(s): 200
                response == {
                    "requiredReadonlyInt": 0,  # Required int, illustrating a readonly value type
                      property. Required.
                    "requiredReadonlyIntList": [
                        0  # Required readonly int collection. Required.
                    ],
                    "requiredReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "requiredReadonlyString": "str",  # Required string, illustrating a readonly
                      reference type property. Required.
                    "requiredReadonlyStringList": [
                        "str"  # Required readonly string collection. Required.
                    ],
                    "optionalReadonlyInt": 0,  # Optional. Optional int, illustrating a readonly
                      value type property.
                    "optionalReadonlyIntList": [
                        0  # Optional. Optional readonly int collection.
                    ],
                    "optionalReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "optionalReadonlyString": "str",  # Optional. Optional string, illustrating a
                      readonly reference type property.
                    "optionalReadonlyStringList": [
                        "str"  # Optional. Optional readonly string collection.
                    ]
                }
        """

    @overload
    async def set_optional_property_model(
        self, input: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """set_optional_property_model.

        :param input: Required.
        :type input: IO
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
                    "requiredReadonlyInt": 0,  # Required int, illustrating a readonly value type
                      property. Required.
                    "requiredReadonlyIntList": [
                        0  # Required readonly int collection. Required.
                    ],
                    "requiredReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "requiredReadonlyString": "str",  # Required string, illustrating a readonly
                      reference type property. Required.
                    "requiredReadonlyStringList": [
                        "str"  # Required readonly string collection. Required.
                    ],
                    "optionalReadonlyInt": 0,  # Optional. Optional int, illustrating a readonly
                      value type property.
                    "optionalReadonlyIntList": [
                        0  # Optional. Optional readonly int collection.
                    ],
                    "optionalReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "optionalReadonlyString": "str",  # Optional. Optional string, illustrating a
                      readonly reference type property.
                    "optionalReadonlyStringList": [
                        "str"  # Optional. Optional readonly string collection.
                    ]
                }
        """

    @distributed_trace_async
    async def set_optional_property_model(self, input: Union[JSON, IO], **kwargs: Any) -> JSON:
        """set_optional_property_model.

        :param input: Is either a model type or a IO type. Required.
        :type input: JSON or IO
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
                    "requiredReadonlyInt": 0,  # Required int, illustrating a readonly value type
                      property. Required.
                    "requiredReadonlyIntList": [
                        0  # Required readonly int collection. Required.
                    ],
                    "requiredReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "requiredReadonlyString": "str",  # Required string, illustrating a readonly
                      reference type property. Required.
                    "requiredReadonlyStringList": [
                        "str"  # Required readonly string collection. Required.
                    ],
                    "optionalReadonlyInt": 0,  # Optional. Optional int, illustrating a readonly
                      value type property.
                    "optionalReadonlyIntList": [
                        0  # Optional. Optional readonly int collection.
                    ],
                    "optionalReadonlyModel": {
                        "requiredString": "str"  # Required string. Required.
                    },
                    "optionalReadonlyString": "str",  # Optional. Optional string, illustrating a
                      readonly reference type property.
                    "optionalReadonlyStringList": [
                        "str"  # Optional. Optional readonly string collection.
                    ]
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(input, (IO, bytes)):
            _content = input
        else:
            _json = input

        request = build_set_optional_property_model_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
