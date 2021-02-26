# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import IO, List, Optional

from azure.core.pipeline.transport import HttpRequest
from azure.core.pipeline.transport._base import _format_url_section
from msrest import Serializer

_SERIALIZER = Serializer()


def _get_required_path_request(path_parameter: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/required/path/{pathParameter}")
    path_format_arguments = {
        "pathParameter": _SERIALIZER.url("path_parameter", path_parameter, "str"),
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
        query=query_parameters,
    )
    return request


def _put_optional_query_request(query_parameter: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/optional/query")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if query_parameter is not None:
        query_parameters["queryParameter"] = _SERIALIZER.query("query_parameter", query_parameter, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _put_optional_header_request(query_parameter: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/optional/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if query_parameter is not None:
        header_parameters["queryParameter"] = _SERIALIZER.header("query_parameter", query_parameter, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _put_optional_body_request(body: Optional[str] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/optional/body")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _put_optional_binary_body_request(body: Optional[IO] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/octet-stream")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/implicit/optional/binary-body")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        stream=content,
        query=query_parameters,
    )
    return request


def _get_required_global_path_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/required/path/{required-global-path}")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _get_required_global_query_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/required/query")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["required-global-query"] = _SERIALIZER.query(
        "self._config.required_global_query", self._config.required_global_query, "str"
    )

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _get_optional_global_query_request(**kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/optional/query")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if self._config.optional_global_query is not None:
        query_parameters["optional-global-query"] = _SERIALIZER.query(
            "self._config.optional_global_query", self._config.optional_global_query, "int"
        )

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _put_optional_binary_body_request(body: Optional[IO] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/octet-stream")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/explicit/optional/binary-body")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        stream=content,
        query=query_parameters,
    )
    return request


def _put_required_binary_body_request(body: IO, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/octet-stream")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/explicit/required/binary-body")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        stream=content,
        query=query_parameters,
    )
    return request


def _post_required_integer_parameter_request(body: int, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/integer/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_integer_parameter_request(body: Optional[int] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/integer/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_required_integer_property_request(body: "_models.IntWrapper", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/integer/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_integer_property_request(
    body: Optional["_models.IntOptionalWrapper"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/integer/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_required_integer_header_request(header_parameter: int, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/integer/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["headerParameter"] = _SERIALIZER.header("header_parameter", header_parameter, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _post_optional_integer_header_request(header_parameter: Optional[int] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/integer/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if header_parameter is not None:
        header_parameters["headerParameter"] = _SERIALIZER.header("header_parameter", header_parameter, "int")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _post_required_string_parameter_request(body: str, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/string/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_string_parameter_request(body: Optional[str] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/string/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_required_string_property_request(body: "_models.StringWrapper", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/string/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_string_property_request(
    body: Optional["_models.StringOptionalWrapper"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/string/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_required_string_header_request(header_parameter: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/string/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["headerParameter"] = _SERIALIZER.header("header_parameter", header_parameter, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _post_optional_string_header_request(body_parameter: Optional[str] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/string/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if body_parameter is not None:
        header_parameters["bodyParameter"] = _SERIALIZER.header("body_parameter", body_parameter, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _post_required_class_parameter_request(body: "_models.Product", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/class/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_class_parameter_request(body: Optional["_models.Product"] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/class/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_required_class_property_request(body: "_models.ClassWrapper", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/class/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_class_property_request(
    body: Optional["_models.ClassOptionalWrapper"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/class/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_required_array_parameter_request(body: List[str], **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/array/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_array_parameter_request(body: Optional[List[str]] = None, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/array/parameter")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_required_array_property_request(body: "_models.ArrayWrapper", **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/array/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_optional_array_property_request(
    body: Optional["_models.ArrayOptionalWrapper"] = None, **kwargs
) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/array/property")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request


def _post_required_array_header_request(header_parameter: List[str], **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/requied/array/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["headerParameter"] = _SERIALIZER.header("header_parameter", header_parameter, "[str]", div=",")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request


def _post_optional_array_header_request(header_parameter: Optional[List[str]] = None, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/optional/array/header")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if header_parameter is not None:
        header_parameters["headerParameter"] = _SERIALIZER.header(
            "header_parameter", header_parameter, "[str]", div=","
        )
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request
