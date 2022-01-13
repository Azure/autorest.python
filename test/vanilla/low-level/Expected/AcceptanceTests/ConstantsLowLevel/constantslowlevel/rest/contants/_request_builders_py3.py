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

from ..._vendor import _format_url_section

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_put_no_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putNoModelAsStringNoRequiredTwoValueNoDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_no_model_as_string_no_required_two_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putNoModelAsStringNoRequiredTwoValueDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_no_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: The default value is "value1".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putNoModelAsStringNoRequiredOneValueNoDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_no_model_as_string_no_required_one_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: The default value is "value1".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putNoModelAsStringNoRequiredOneValueDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_no_model_as_string_required_two_value_no_default_request(*, input: str, **kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putNoModelAsStringRequiredTwoValueNoDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_no_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putNoModelAsStringRequiredTwoValueDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_no_model_as_string_required_one_value_no_default_request(**kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: The default value is "value1". Note that overriding this default value may
     result in unsupported behavior.
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    input = kwargs.pop("input", "value1")  # type: str

    # Construct URL
    url = "/constants/putNoModelAsStringRequiredOneValueNoDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_no_model_as_string_required_one_value_default_request(**kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: The default value is "value1". Note that overriding this default value may
     result in unsupported behavior.
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    input = kwargs.pop("input", "value1")  # type: str

    # Construct URL
    url = "/constants/putNoModelAsStringRequiredOneValueDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_model_as_string_no_required_two_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putModelAsStringNoRequiredTwoValueNoDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_model_as_string_no_required_two_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putModelAsStringNoRequiredTwoValueDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_model_as_string_no_required_one_value_no_default_request(
    *, input: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: "value1"
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putModelAsStringNoRequiredOneValueNoDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_model_as_string_no_required_one_value_default_request(
    *, input: Optional[str] = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: "value1"
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putModelAsStringNoRequiredOneValueDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if input is not None:
        query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_model_as_string_required_two_value_no_default_request(*, input: str, **kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putModelAsStringRequiredTwoValueNoDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_model_as_string_required_two_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: Possible values are: "value1" or "value2".
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putModelAsStringRequiredTwoValueDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_model_as_string_required_one_value_no_default_request(*, input: str, **kwargs: Any) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: "value1"
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putModelAsStringRequiredOneValueNoDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_model_as_string_required_one_value_default_request(
    *, input: str = "value1", **kwargs: Any
) -> HttpRequest:
    """Puts constants to the testserver.

    Puts constants to the testserver.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword input: "value1"
    :paramtype input: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = "/constants/putModelAsStringRequiredOneValueDefault"

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["input"] = _SERIALIZER.query("input", input, "str")

    return HttpRequest(method="PUT", url=url, params=query_parameters, **kwargs)


def build_put_client_constants_request(**kwargs: Any) -> HttpRequest:
    """Pass constants from the client to this function. Will pass in constant path, query, and header
    parameters.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    header_constant = kwargs.pop("header_constant", True)  # type: bool
    query_constant = kwargs.pop("query_constant", 100)  # type: int
    path_constant = kwargs.pop("path_constant", "path")  # type: str

    # Construct URL
    url = "/constants/clientConstants/{path-constant}"
    path_format_arguments = {
        "path-constant": _SERIALIZER.url("path_constant", path_constant, "str"),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters["query-constant"] = _SERIALIZER.query("query_constant", query_constant, "int")

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters["header-constant"] = _SERIALIZER.header("header_constant", header_constant, "bool")

    return HttpRequest(method="PUT", url=url, params=query_parameters, headers=header_parameters, **kwargs)
