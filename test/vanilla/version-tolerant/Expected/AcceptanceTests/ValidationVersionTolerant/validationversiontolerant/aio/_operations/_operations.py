# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

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

from ..._operations._operations import (
    build_get_with_constant_in_path_request,
    build_post_with_constant_in_body_request,
    build_validation_of_body_request,
    build_validation_of_method_parameters_request,
)
from .._vendor import MixinABC

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestValidationTestOperationsMixin(MixinABC):
    @distributed_trace_async
    async def validation_of_method_parameters(self, resource_group_name: str, id: int, **kwargs: Any) -> JSONType:
        """Validates input parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                      pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "1.0.0")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        request = build_validation_of_method_parameters_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            id=id,
            api_version=api_version,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.json()

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def validation_of_body(
        self, resource_group_name: str, id: int, body: JSONType = None, **kwargs: Any
    ) -> JSONType:
        """Validates body parameters on the method. See swagger for details.

        :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
        :type resource_group_name: str
        :param id: Required int multiple of 10 from 100 to 1000.
        :type id: int
        :param body:  Default value is None.
        :type body: JSONType
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                      pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }

                # response body for status code(s): 200
                response.json() == {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                      pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        api_version = kwargs.pop("api_version", "1.0.0")  # type: str
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        if body is not None:
            _json = body
        else:
            _json = None

        request = build_validation_of_body_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            id=id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.json()

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    @distributed_trace_async
    async def get_with_constant_in_path(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """get_with_constant_in_path.

        :keyword constant_param:  Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        constant_param = kwargs.pop("constant_param", "constant")  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_get_with_constant_in_path_request(
            constant_param=constant_param,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def post_with_constant_in_body(self, body: JSONType = None, **kwargs: Any) -> JSONType:
        """post_with_constant_in_body.

        :param body:  Default value is None.
        :type body: JSONType
        :keyword constant_param:  Default value is "constant". Note that overriding this default value
         may result in unsupported behavior.
        :paramtype constant_param: str
        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                      pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }

                # response body for status code(s): 200
                response.json() == {
                    "capacity": 0,  # Optional. Non required int betwen 0 and 100 exclusive.
                    "child": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "count": 0  # Optional. Count.
                    },
                    "constChild": {
                        "constProperty": "constant",  # Default value is "constant". Constant
                          string. Has constant value: "constant".
                        "constProperty2": "constant2"  # Default value is "constant2".
                          Constant string2. Has constant value: "constant2".
                    },
                    "constInt": 0,  # Default value is 0. Constant int. Has constant value: 0.
                    "constString": "constant",  # Default value is "constant". Constant string.
                      Has constant value: "constant".
                    "constStringAsEnum": "constant_string_as_enum",  # Optional. Default value is
                      "constant_string_as_enum". Constant string as Enum. The only acceptable values to
                      pass in are None and "constant_string_as_enum". The default value is None.
                    "display_names": [
                        "str"  # Optional. Non required array of unique items from 0 to 6
                          elements.
                    ],
                    "image": "str"  # Optional. Image URL representing the product.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        constant_param = kwargs.pop("constant_param", "constant")  # type: str
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        if body is not None:
            _json = body
        else:
            _json = None

        request = build_post_with_constant_in_body_request(
            constant_param=constant_param,
            content_type=content_type,
            json=_json,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.json()

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
