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
    from typing import IO, List, Optional

_SERIALIZER = Serializer()


def _prepare_implicit_get_required_path_request(
    path_parameter,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_implicit_put_optional_query_request(
    query_parameter=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_implicit_put_optional_header_request(
    query_parameter=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_implicit_put_optional_body_request(
    body=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_implicit_put_optional_binary_body_request(
    body=None,  # type: Optional[IO]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["stream"] = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_implicit_get_required_global_path_request(
    required_global_path,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/required/path/{required-global-path}")
    path_format_arguments = {
        "required-global-path": _SERIALIZER.url("required_global_path", required_global_path, "str"),
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


def _prepare_implicit_get_required_global_query_request(
    required_global_query,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/required/query")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters["required-global-query"] = _SERIALIZER.query("required_global_query", required_global_query, "str")

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


def _prepare_implicit_get_optional_global_query_request(
    optional_global_query=None,  # type: Optional[int]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/reqopt/global/optional/query")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if optional_global_query is not None:
        query_parameters["optional-global-query"] = _SERIALIZER.query(
            "optional_global_query", optional_global_query, "int"
        )

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


def _prepare_explicit_put_optional_binary_body_request(
    body=None,  # type: Optional[IO]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["stream"] = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_put_required_binary_body_request(
    body,  # type: IO
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["stream"] = body

    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_integer_parameter_request(
    body,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_integer_parameter_request(
    body=None,  # type: Optional[int]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_integer_property_request(
    body,  # type: "_models.IntWrapper"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_integer_property_request(
    body=None,  # type: Optional["_models.IntOptionalWrapper"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_integer_header_request(
    header_parameter,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_integer_header_request(
    header_parameter=None,  # type: Optional[int]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_string_parameter_request(
    body,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_string_parameter_request(
    body=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_string_property_request(
    body,  # type: "_models.StringWrapper"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_string_property_request(
    body=None,  # type: Optional["_models.StringOptionalWrapper"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_string_header_request(
    header_parameter,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_string_header_request(
    body_parameter=None,  # type: Optional[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_class_parameter_request(
    body,  # type: "_models.Product"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_class_parameter_request(
    body=None,  # type: Optional["_models.Product"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_class_property_request(
    body,  # type: "_models.ClassWrapper"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_class_property_request(
    body=None,  # type: Optional["_models.ClassOptionalWrapper"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_array_parameter_request(
    body,  # type: List[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_array_parameter_request(
    body=None,  # type: Optional[List[str]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_array_property_request(
    body,  # type: "_models.ArrayWrapper"
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_array_property_request(
    body=None,  # type: Optional["_models.ArrayOptionalWrapper"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    body_content_kwargs["json"] = body

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **body_content_kwargs,
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_required_array_header_request(
    header_parameter,  # type: List[str]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request


def _prepare_explicit_post_optional_array_header_request(
    header_parameter=None,  # type: Optional[List[str]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
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
    )
    if query_parameters:
        request.format_parameters(query_parameters)
    return request
