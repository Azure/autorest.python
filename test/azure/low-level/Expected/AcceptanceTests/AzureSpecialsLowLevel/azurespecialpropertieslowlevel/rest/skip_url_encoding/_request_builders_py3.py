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


def build_get_method_path_valid_request(
    unencoded_path_param: str,
    **kwargs: Any
) -> HttpRequest:
    """Get method with unencoded path parameter with value 'path1/path2/path3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
    :type unencoded_path_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = '/azurespecials/skipUrlEncoding/method/path/valid/{unencodedPathParam}'
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_path_valid_request(
    unencoded_path_param: str,
    **kwargs: Any
) -> HttpRequest:
    """Get method with unencoded path parameter with value 'path1/path2/path3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param unencoded_path_param: Unencoded path parameter with value 'path1/path2/path3'.
    :type unencoded_path_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = '/azurespecials/skipUrlEncoding/path/path/valid/{unencodedPathParam}'
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_swagger_path_valid_request(
    **kwargs: Any
) -> HttpRequest:
    """Get method with unencoded path parameter with value 'path1/path2/path3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword unencoded_path_param: An unencoded path parameter with value 'path1/path2/path3'. The
     default value is "path1/path2/path3". Note that overriding this default value may result in
     unsupported behavior.
    :paramtype unencoded_path_param: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    unencoded_path_param = kwargs.pop('unencoded_path_param', "path1/path2/path3")  # type: str

    accept = "application/json"
    # Construct URL
    url = '/azurespecials/skipUrlEncoding/swagger/path/valid/{unencodedPathParam}'
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_method_query_valid_request(
    *,
    q1: str,
    **kwargs: Any
) -> HttpRequest:
    """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
    :paramtype q1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = '/azurespecials/skipUrlEncoding/method/query/valid'

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

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


def build_get_method_query_null_request(
    *,
    q1: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Get method with unencoded query parameter with value null.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword q1: Unencoded query parameter with value null.
    :paramtype q1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = '/azurespecials/skipUrlEncoding/method/query/null'

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if q1 is not None:
        query_parameters['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

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


def build_get_path_query_valid_request(
    *,
    q1: str,
    **kwargs: Any
) -> HttpRequest:
    """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword q1: Unencoded query parameter with value 'value1&q2=value2&q3=value3'.
    :paramtype q1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = '/azurespecials/skipUrlEncoding/path/query/valid'

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

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


def build_get_swagger_query_valid_request(
    **kwargs: Any
) -> HttpRequest:
    """Get method with unencoded query parameter with value 'value1&q2=value2&q3=value3'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword q1: An unencoded query parameter with value 'value1&q2=value2&q3=value3'. The default
     value is "value1&q2=value2&q3=value3". Note that overriding this default value may result in
     unsupported behavior.
    :paramtype q1: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    q1 = kwargs.pop('q1', "value1&q2=value2&q3=value3")  # type: str

    accept = "application/json"
    # Construct URL
    url = '/azurespecials/skipUrlEncoding/swagger/query/valid'

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['q1'] = _SERIALIZER.query("q1", q1, 'str', skip_quote=True)

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

