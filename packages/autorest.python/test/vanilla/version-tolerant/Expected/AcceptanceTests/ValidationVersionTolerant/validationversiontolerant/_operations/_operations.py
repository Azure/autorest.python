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
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .._serialization import Serializer
from .._vendor import AutoRestValidationTestMixinABC, _format_url_section

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
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_auto_rest_validation_test_validation_of_method_parameters_request(
    resource_group_name: str, id: int, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["1.0.0"] = kwargs.pop("api_version", _params.pop("apiVersion", "1.0.0"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=10, min_length=3, pattern=r"[a-zA-Z0-9\']+"
        ),
        "id": _SERIALIZER.url("id", id, "int", maximum=1000, minimum=100, multiple=10),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["apiVersion"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_auto_rest_validation_test_validation_of_body_request(
    resource_group_name: str, id: int, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    api_version: Literal["1.0.0"] = kwargs.pop("api_version", _params.pop("apiVersion", "1.0.0"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/fakepath/{subscriptionId}/{resourceGroupName}/{id}"
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=10, min_length=3, pattern=r"[a-zA-Z0-9]+"
        ),
        "id": _SERIALIZER.url("id", id, "int", maximum=1000, minimum=100, multiple=10),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["apiVersion"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_auto_rest_validation_test_get_with_constant_in_path_request(**kwargs: Any) -> HttpRequest:
    constant_param: Literal["constant"] = kwargs.pop("constant_param", "constant")
    # Construct URL
    _url = "/validation/constantsInPath/{constantParam}/value"
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    return HttpRequest(method="GET", url=_url, **kwargs)


def build_auto_rest_validation_test_post_with_constant_in_body_request(**kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    constant_param: Literal["constant"] = kwargs.pop("constant_param", "constant")
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/validation/constantsInPath/{constantParam}/value"
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class AutoRestValidationTestOperationsMixin(AutoRestValidationTestMixinABC):
    @distributed_trace
    def validation_of_method_parameters(self, resource_group_name: str, id: int, **kwargs: Any) -> JSON:
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

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
    def validation_of_body(
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
    def validation_of_body(
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

    @distributed_trace
    def validation_of_body(
        self, resource_group_name: str, id: int, body: Optional[Union[JSON, IO]] = None, **kwargs: Any
    ) -> JSON:
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
         Required.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000. Required.
        :type id: int
        :param body: Is either a JSON type or a IO type. Default value is None.
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

        _json: Any = None
        _content: Any = None
        if isinstance(body, MutableMapping):
            if body is not None:
                _json = body
            else:
                _json = None
            content_type = content_type or "application/json"
        elif isinstance(body, (IO, bytes)):
            if body is not None:
                _content = body
            else:
                _content = None
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for body")

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

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
    def get_with_constant_in_path(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
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

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @overload
    def post_with_constant_in_body(
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
    def post_with_constant_in_body(
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

    @distributed_trace
    def post_with_constant_in_body(self, body: Optional[Union[JSON, IO]] = None, **kwargs: Any) -> JSON:
        """post_with_constant_in_body.

        :param body: Is either a JSON type or a IO type. Default value is None.
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

        _json: Any = None
        _content: Any = None
        if isinstance(body, MutableMapping):
            if body is not None:
                _json = body
            else:
                _json = None
            content_type = content_type or "application/json"
        elif isinstance(body, (IO, bytes)):
            if body is not None:
                _content = body
            else:
                _content = None
            content_type = content_type or "application/json"
        else:
            raise TypeError("unrecognized type for body")

        request = build_auto_rest_validation_test_post_with_constant_in_body_request(
            constant_param=constant_param,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
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
