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


def prepare_paging_get_no_item_name_pages(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/noitemname")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_null_next_link_name_pages(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/nullnextlink")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_single_pages(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/single")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_first_response_empty(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/firstResponseEmpty/1")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    client_request_id = kwargs.pop("client_request_id", None)  # type: Optional[str]
    maxresults = kwargs.pop("maxresults", None)  # type: Optional[int]
    timeout = kwargs.pop("timeout", 30)  # type: Optional[int]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if maxresults is not None:
        header_parameters["maxresults"] = _SERIALIZER.header("maxresults", maxresults, "int")
    if timeout is not None:
        header_parameters["timeout"] = _SERIALIZER.header("timeout", timeout, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_with_query_params(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    required_query_parameter = kwargs.pop("required_query_parameter")  # type: int
    query_constant = True
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/getWithQueryParams")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["requiredQueryParameter"] = _SERIALIZER.query(
        "required_query_parameter", required_query_parameter, "int"
    )
    query_parameters["queryConstant"] = _SERIALIZER.query("query_constant", query_constant, "bool")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_paging_next_operation_with_query_params(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    query_constant = True
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/nextOperationWithQueryParams")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["queryConstant"] = _SERIALIZER.query("query_constant", query_constant, "bool")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_paging_get_odata_multiple_pages(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    client_request_id = kwargs.pop("client_request_id", None)  # type: Optional[str]
    maxresults = kwargs.pop("maxresults", None)  # type: Optional[int]
    timeout = kwargs.pop("timeout", 30)  # type: Optional[int]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/odata")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if maxresults is not None:
        header_parameters["maxresults"] = _SERIALIZER.header("maxresults", maxresults, "int")
    if timeout is not None:
        header_parameters["timeout"] = _SERIALIZER.header("timeout", timeout, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages_with_offset(
    offset,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    client_request_id = kwargs.pop("client_request_id", None)  # type: Optional[str]
    maxresults = kwargs.pop("maxresults", None)  # type: Optional[int]
    timeout = kwargs.pop("timeout", 30)  # type: Optional[int]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/withpath/{offset}")
    path_format_arguments = {
        "offset": _SERIALIZER.url("offset", offset, "int"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if maxresults is not None:
        header_parameters["maxresults"] = _SERIALIZER.header("maxresults", maxresults, "int")
    if timeout is not None:
        header_parameters["timeout"] = _SERIALIZER.header("timeout", timeout, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages_retry_first(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/retryfirst")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages_retry_second(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/retrysecond")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_single_pages_failure(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/single/failure")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages_failure(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/failure")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages_failure_uri(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/failureuri")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages_fragment_next_link(
    tenant,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop("api_version")  # type: str
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/fragment/{tenant}")
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api_version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages_fragment_with_grouping_next_link(
    tenant,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop("api_version")  # type: str
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/fragmentwithgrouping/{tenant}")
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api_version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_paging_get_multiple_pages_lro_initial(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    client_request_id = kwargs.pop("client_request_id", None)  # type: Optional[str]
    maxresults = kwargs.pop("maxresults", None)  # type: Optional[int]
    timeout = kwargs.pop("timeout", 30)  # type: Optional[int]
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/lro")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if client_request_id is not None:
        header_parameters["client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    if maxresults is not None:
        header_parameters["maxresults"] = _SERIALIZER.header("maxresults", maxresults, "int")
    if timeout is not None:
        header_parameters["timeout"] = _SERIALIZER.header("timeout", timeout, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )


def prepare_paging_next_fragment(
    tenant,  # type: str
    next_link,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop("api_version")  # type: str
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/fragment/{tenant}/{nextLink}")
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, "str"),
        "nextLink": _SERIALIZER.url("next_link", next_link, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api_version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_paging_next_fragment_with_grouping(
    tenant,  # type: str
    next_link,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop("api_version")  # type: str
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/multiple/fragmentwithgrouping/{tenant}/{nextLink}")
    path_format_arguments = {
        "tenant": _SERIALIZER.url("tenant", tenant, "str"),
        "nextLink": _SERIALIZER.url("next_link", next_link, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api_version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
    )


def prepare_paging_get_paging_model_with_item_name_with_xms_client_name(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/paging/itemNameWithXMSClientName")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
