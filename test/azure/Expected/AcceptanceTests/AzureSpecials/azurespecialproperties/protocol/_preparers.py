# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from azure.core.pipeline.transport import HttpRequest
from azure.core.pipeline.transport._base import _format_url_section
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Optional

_SERIALIZER = Serializer()


def _prepare_xmsclientrequestid_get_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/overwrite/x-ms-client-request-id/method/")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_xmsclientrequestid_param_get_request(
    x_ms_client_request_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/overwrite/x-ms-client-request-id/via-param/method/")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["x-ms-client-request-id"] = _SERIALIZER.header(
        "x_ms_client_request_id", x_ms_client_request_id, "str"
    )
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptionincredentials_post_method_global_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/method/string/none/path/global/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptionincredentials_post_method_global_null_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url", "/azurespecials/subscriptionId/method/string/none/path/global/null/{subscriptionId}"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptionincredentials_post_method_global_not_provided_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-07-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/method/string/none/path/globalNotProvided/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptionincredentials_post_path_global_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/path/string/none/path/global/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptionincredentials_post_swagger_global_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/swagger/string/none/path/global/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptioninmethod_post_method_local_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/method/string/none/path/local/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptioninmethod_post_method_local_null_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url", "/azurespecials/subscriptionId/method/string/none/path/local/null/{subscriptionId}"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptioninmethod_post_path_local_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url", "/azurespecials/subscriptionId/path/string/none/path/local/1234-5678-9012-3456/{subscriptionId}"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_subscriptioninmethod_post_swagger_local_valid_request(
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url",
        "/azurespecials/subscriptionId/swagger/string/none/path/local/1234-5678-9012-3456/{subscriptionId}",
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_apiversiondefault_get_method_global_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-07-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/method/string/none/query/global/2015-07-01-preview")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_apiversiondefault_get_method_global_not_provided_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-07-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop(
        "template_url", "/azurespecials/apiVersion/method/string/none/query/globalNotProvided/2015-07-01-preview"
    )

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_apiversiondefault_get_path_global_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-07-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/path/string/none/query/global/2015-07-01-preview")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_apiversiondefault_get_swagger_global_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2015-07-01-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/swagger/string/none/query/global/2015-07-01-preview")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_apiversionlocal_get_method_local_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/method/string/none/query/local/2.0")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_apiversionlocal_get_method_local_null_request(
    api_version=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/method/string/none/query/local/null")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if api_version is not None:
        query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_apiversionlocal_get_path_local_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/path/string/none/query/local/2.0")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_apiversionlocal_get_swagger_local_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/apiVersion/swagger/string/none/query/local/2.0")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_skipurlencoding_get_method_path_valid_request(
    unencoded_path_param,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/skipUrlEncoding/method/path/valid/{unencodedPathParam}")
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_skipurlencoding_get_path_valid_request(
    unencoded_path_param,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/skipUrlEncoding/path/path/valid/{unencodedPathParam}")
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_skipurlencoding_get_swagger_path_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    unencoded_path_param = "path1/path2/path3"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/skipUrlEncoding/swagger/path/valid/{unencodedPathParam}")
    path_format_arguments = {
        "unencodedPathParam": _SERIALIZER.url("unencoded_path_param", unencoded_path_param, "str", skip_quote=True),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_skipurlencoding_get_method_query_valid_request(
    q1,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/skipUrlEncoding/method/query/valid")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["q1"] = _SERIALIZER.query("q1", q1, "str", skip_quote=True)

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_skipurlencoding_get_method_query_null_request(
    q1=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/skipUrlEncoding/method/query/null")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if q1 is not None:
        query_parameters["q1"] = _SERIALIZER.query("q1", q1, "str", skip_quote=True)

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_skipurlencoding_get_path_query_valid_request(
    q1,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/skipUrlEncoding/path/query/valid")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["q1"] = _SERIALIZER.query("q1", q1, "str", skip_quote=True)

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_skipurlencoding_get_swagger_query_valid_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    q1 = "value1&q2=value2&q3=value3"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/skipUrlEncoding/swagger/query/valid")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["q1"] = _SERIALIZER.query("q1", q1, "str", skip_quote=True)

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_odata_get_with_filter_request(
    filter=None,  # type: Optional[str]
    top=None,  # type: Optional[int]
    orderby=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/odata/filter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if filter is not None:
        query_parameters["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if top is not None:
        query_parameters["$top"] = _SERIALIZER.query("top", top, "int")
    if orderby is not None:
        query_parameters["$orderby"] = _SERIALIZER.query("orderby", orderby, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_header_custom_named_request_id_request(
    foo_client_request_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/customNamedRequestId")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["foo-client-request-id"] = _SERIALIZER.header(
        "foo_client_request_id", foo_client_request_id, "str"
    )
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_header_custom_named_request_id_param_grouping_request(
    foo_client_request_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/customNamedRequestIdParamGrouping")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["foo-client-request-id"] = _SERIALIZER.header(
        "foo_client_request_id", foo_client_request_id, "str"
    )
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_header_custom_named_request_id_head_request(
    foo_client_request_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/azurespecials/customNamedRequestIdHead")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["foo-client-request-id"] = _SERIALIZER.header(
        "foo_client_request_id", foo_client_request_id, "str"
    )
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="HEAD",
        url=url,
        headers=header_parameters,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request
