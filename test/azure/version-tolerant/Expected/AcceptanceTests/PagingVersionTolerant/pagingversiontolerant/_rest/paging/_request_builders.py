# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_get_no_item_name_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that must return result of the default 'value' node.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/noitemname')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_null_next_link_name_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that must ignore any kind of nextLink, and stop after page 1.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/nullnextlink')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_single_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that finishes on the first call without a nextlink.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/single')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_first_response_empty_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation whose first response's items list is empty, but still returns a next link.
    Second (and final) call, will give you an items list of 1.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/firstResponseEmpty/1')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_multiple_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a nextLink that has 10 pages.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword client_request_id:
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    client_request_id = kwargs.pop('client_request_id', None)  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', None)  # type: Optional[int]
    timeout = kwargs.pop('timeout', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        header_parameters['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        header_parameters['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_with_query_params_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a next operation. It has a different query parameter from it's
    next operation nextOperationWithQueryParams. Returns a ProductResult.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword required_query_parameter: A required integer query parameter. Put in value '100' to
     pass test.
    :paramtype required_query_parameter: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    required_query_parameter = kwargs.pop('required_query_parameter')  # type: int

    query_constant = True
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/getWithQueryParams')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['requiredQueryParameter'] = _SERIALIZER.query("required_query_parameter", required_query_parameter, 'int')
    query_parameters['queryConstant'] = _SERIALIZER.query("query_constant", query_constant, 'bool')

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


def build_next_operation_with_query_params_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Next operation for getWithQueryParams. Pass in next=True to pass test. Returns a ProductResult.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    query_constant = True
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/nextOperationWithQueryParams')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['queryConstant'] = _SERIALIZER.query("query_constant", query_constant, 'bool')

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


def build_get_odata_multiple_pages_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a nextLink in odata format that has 10 pages.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword client_request_id:
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    client_request_id = kwargs.pop('client_request_id', None)  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', None)  # type: Optional[int]
    timeout = kwargs.pop('timeout', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/odata')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        header_parameters['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        header_parameters['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_multiple_pages_with_offset_request(
    offset,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a nextLink that has 10 pages.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param offset: Offset of return value.
    :type offset: int
    :keyword client_request_id:
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    client_request_id = kwargs.pop('client_request_id', None)  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', None)  # type: Optional[int]
    timeout = kwargs.pop('timeout', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/withpath/{offset}')
    path_format_arguments = {
        'offset': _SERIALIZER.url("offset", offset, 'int'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        header_parameters['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        header_parameters['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_multiple_pages_retry_first_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that fails on the first call with 500 and then retries and then get a
    response including a nextLink that has 10 pages.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/retryfirst')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_multiple_pages_retry_second_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that includes a nextLink that has 10 pages, of which the 2nd call fails
    first with 500. The client should retry and finish all 10 pages eventually.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/retrysecond')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_single_pages_failure_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that receives a 400 on the first call.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/single/failure')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_multiple_pages_failure_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that receives a 400 on the second call.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/failure')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_multiple_pages_failure_uri_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that receives an invalid nextLink.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/failureuri')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_get_multiple_pages_fragment_next_link_request(
    tenant,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that doesn't return a full URL, just a fragment.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param tenant: Sets the tenant to use.
    :type tenant: str
    :keyword api_version: Sets the api version to use.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop('api_version')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/fragment/{tenant}')
    path_format_arguments = {
        'tenant': _SERIALIZER.url("tenant", tenant, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api_version'] = _SERIALIZER.query("api_version", api_version, 'str')

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


def build_get_multiple_pages_fragment_with_grouping_next_link_request(
    tenant,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that doesn't return a full URL, just a fragment with parameters grouped.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param tenant: Sets the tenant to use.
    :type tenant: str
    :keyword api_version: Sets the api version to use.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop('api_version')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/fragmentwithgrouping/{tenant}')
    path_format_arguments = {
        'tenant': _SERIALIZER.url("tenant", tenant, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api_version'] = _SERIALIZER.query("api_version", api_version, 'str')

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


def build_get_multiple_pages_lro_request_initial(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A long-running paging operation that includes a nextLink that has 10 pages.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword client_request_id:
    :paramtype client_request_id: str
    :keyword maxresults: Sets the maximum number of items to return in the response.
    :paramtype maxresults: int
    :keyword timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :paramtype timeout: int
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    client_request_id = kwargs.pop('client_request_id', None)  # type: Optional[str]
    maxresults = kwargs.pop('maxresults', None)  # type: Optional[int]
    timeout = kwargs.pop('timeout', 30)  # type: Optional[int]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/lro')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters['client-request-id'] = _SERIALIZER.header("client_request_id", client_request_id, 'str')
    if maxresults is not None:
        header_parameters['maxresults'] = _SERIALIZER.header("maxresults", maxresults, 'int')
    if timeout is not None:
        header_parameters['timeout'] = _SERIALIZER.header("timeout", timeout, 'int')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_next_fragment_request(
    tenant,  # type: str
    next_link,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that doesn't return a full URL, just a fragment.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param tenant: Sets the tenant to use.
    :type tenant: str
    :param next_link: Next link for list operation.
    :type next_link: str
    :keyword api_version: Sets the api version to use.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop('api_version')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/fragment/{tenant}/{nextLink}')
    path_format_arguments = {
        'tenant': _SERIALIZER.url("tenant", tenant, 'str'),
        'nextLink': _SERIALIZER.url("next_link", next_link, 'str', skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api_version'] = _SERIALIZER.query("api_version", api_version, 'str')

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


def build_next_fragment_with_grouping_request(
    tenant,  # type: str
    next_link,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that doesn't return a full URL, just a fragment.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param tenant: Sets the tenant to use.
    :type tenant: str
    :param next_link: Next link for list operation.
    :type next_link: str
    :keyword api_version: Sets the api version to use.
    :paramtype api_version: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    api_version = kwargs.pop('api_version')  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/multiple/fragmentwithgrouping/{tenant}/{nextLink}')
    path_format_arguments = {
        'tenant': _SERIALIZER.url("tenant", tenant, 'str'),
        'nextLink': _SERIALIZER.url("next_link", next_link, 'str', skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api_version'] = _SERIALIZER.query("api_version", api_version, 'str')

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


def build_get_paging_model_with_item_name_with_xms_client_name_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """A paging operation that returns a paging model whose item name is is overriden by
    x-ms-client-name 'indexes'.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/paging/itemNameWithXMSClientName')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )
