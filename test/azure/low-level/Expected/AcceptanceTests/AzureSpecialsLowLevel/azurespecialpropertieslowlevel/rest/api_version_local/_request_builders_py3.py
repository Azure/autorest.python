# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional

from azure.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_get_method_local_valid_request(**kwargs: Any) -> HttpRequest:
    """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: This should appear as a method parameter, use value '2.0'. The default
     value is "2.0". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop("api_version", "2.0")  # type: str

    accept = "application/json"
    # Construct URL
    _url = "/azurespecials/apiVersion/method/string/none/query/local/2.0"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


def build_get_method_local_null_request(*, api_version: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    """Get method with api-version modeled in the method.  pass in api-version = null to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: This should appear as a method parameter, use value null, this should
     result in no serialized parameter.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    _url = "/azurespecials/apiVersion/method/string/none/query/local/null"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if api_version is not None:
        _query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


def build_get_path_local_valid_request(**kwargs: Any) -> HttpRequest:
    """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: This should appear as a method parameter, use value '2.0'. The default
     value is "2.0". Note that overriding this default value may result in unsupported behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop("api_version", "2.0")  # type: str

    accept = "application/json"
    # Construct URL
    _url = "/azurespecials/apiVersion/path/string/none/query/local/2.0"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


def build_get_swagger_local_valid_request(**kwargs: Any) -> HttpRequest:
    """Get method with api-version modeled in the method.  pass in api-version = '2.0' to succeed.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword api_version: The api version, which appears in the query, the value is always '2.0'.
     The default value is "2.0". Note that overriding this default value may result in unsupported
     behavior.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop("api_version", "2.0")  # type: str

    accept = "application/json"
    # Construct URL
    _url = "/azurespecials/apiVersion/swagger/string/none/query/local/2.0"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)
