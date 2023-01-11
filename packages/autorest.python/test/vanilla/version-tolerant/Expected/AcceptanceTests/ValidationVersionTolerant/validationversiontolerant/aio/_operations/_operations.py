# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
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
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ..._operations._operations import (
    build_auto_rest_validation_test_get_with_constant_in_path_request,
    build_auto_rest_validation_test_post_with_constant_in_body_request,
    build_auto_rest_validation_test_validation_of_body_request,
    build_auto_rest_validation_test_validation_of_method_parameters_request,
)
from .._vendor import AutoRestValidationTestMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestValidationTestOperationsMixin(AutoRestValidationTestMixinABC):
    @distributed_trace_async
    async def validation_of_method_parameters(self, resource_group_name: str, id: int, **kwargs: Any) -> JSON:
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
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

        cls: ClsType[JSON] = kwargs.pop("cls", None)

        request = build_auto_rest_validation_test_validation_of_method_parameters_request(
            resource_group_name=resource_group_name,
            id=id,
            subscription_id=self._config.subscription_id,
            api_version=self._config.api_version,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
    async def validation_of_body(
        self,
        resource_group_name: str,
        id: int,
        body: Optional[JSON] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> JSON:
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :param body: Default value is None.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }

                # response body for status code(s): 200
                response == {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """

    @overload
    async def validation_of_body(
        self,
        resource_group_name: str,
        id: int,
        body: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> JSON:
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :param body: Default value is None.
        :type body: IO
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
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """

    @distributed_trace_async
    async def validation_of_body(
        self, resource_group_name: str, id: int, body: Optional[Union[JSON, IO]] = None, **kwargs: Any
    ) -> JSON:
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :param body: Is either a model type or a IO type. Default value is None.
        :type body: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }

                # response body for status code(s): 200
                response == {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
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

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            if body is not None:
                _json = body
            else:
                _json = None

        request = build_auto_rest_validation_test_validation_of_body_request(
            resource_group_name=resource_group_name,
            id=id,
            subscription_id=self._config.subscription_id,
            content_type=content_type,
            api_version=self._config.api_version,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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

    @distributed_trace_async
    async def get_with_constant_in_path(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """get_with_constant_in_path.

        :keyword constant_param: Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
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

        constant_param: Literal["constant"] = kwargs.pop("constant_param", "constant")
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_auto_rest_validation_test_get_with_constant_in_path_request(
            constant_param=constant_param,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    async def post_with_constant_in_body(
        self, body: Optional[JSON] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """post_with_constant_in_body.

        :param body: Default value is None.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword constant_param: Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }

                # response body for status code(s): 200
                response == {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """

    @overload
    async def post_with_constant_in_body(
        self, body: Optional[IO] = None, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """post_with_constant_in_body.

        :param body: Default value is None.
        :type body: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword constant_param: Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """

    @distributed_trace_async
    async def post_with_constant_in_body(self, body: Optional[Union[JSON, IO]] = None, **kwargs: Any) -> JSON:
        """post_with_constant_in_body.

        :param body: Is either a model type or a IO type. Default value is None.
        :type body: JSON or IO
        :keyword constant_param: Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }

                # response body for status code(s): 200
                response == {
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Required.
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Required.
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Required.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Required.
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
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

        constant_param: Literal["constant"] = kwargs.pop("constant_param", "constant")
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[JSON] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            if body is not None:
                _json = body
            else:
                _json = None

        request = build_auto_rest_validation_test_post_with_constant_in_body_request(
            constant_param=constant_param,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
