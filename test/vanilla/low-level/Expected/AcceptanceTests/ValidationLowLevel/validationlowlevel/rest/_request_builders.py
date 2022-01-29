# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.rest import HttpRequest
from msrest import Serializer

from .._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional, TypeVar
    T = TypeVar('T')
    JSONType = Any

_SERIALIZER = Serializer()

# fmt: off

def build_validation_of_method_parameters_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Validates input parameters on the method. See swagger for details.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
    :type resource_group_name: str
    :param id: Required int multiple of 10 from 100 to 1000.
    :type id: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

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

    api_version = kwargs.pop('api_version', "1.0.0")  # type: str

    accept = "application/json"
    # Construct URL
    url = '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9\']+'),
        "id": _SERIALIZER.url("id", id, 'int', maximum=1000, minimum=100, multiple=10),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['apiVersion'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_validation_of_body_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Validates body parameters on the method. See swagger for details.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param resource_group_name: Required string between 3 and 10 chars with pattern [a-zA-Z0-9]+.
    :type resource_group_name: str
    :param id: Required int multiple of 10 from 100 to 1000.
    :type id: int
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
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

    api_version = kwargs.pop('api_version', "1.0.0")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = '/fakepath/{subscriptionId}/{resourceGroupName}/{id}'
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=10, min_length=3, pattern=r'[a-zA-Z0-9]+'),
        "id": _SERIALIZER.url("id", id, 'int', maximum=1000, minimum=100, multiple=10),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['apiVersion'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_with_constant_in_path_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """get_with_constant_in_path.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword constant_param: The default value is "constant". Note that overriding this default
     value may result in unsupported behavior.
    :paramtype constant_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    constant_param = kwargs.pop('constant_param', "constant")  # type: str

    # Construct URL
    url = '/validation/constantsInPath/{constantParam}/value'
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    return HttpRequest(
        method="GET",
        url=url,
        **kwargs
    )


def build_post_with_constant_in_body_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """post_with_constant_in_body.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword constant_param: The default value is "constant". Note that overriding this default
     value may result in unsupported behavior.
    :paramtype constant_param: str
    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input).
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
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

    constant_param = kwargs.pop('constant_param', "constant")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = '/validation/constantsInPath/{constantParam}/value'
    path_format_arguments = {
        "constantParam": _SERIALIZER.url("constant_param", constant_param, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )

