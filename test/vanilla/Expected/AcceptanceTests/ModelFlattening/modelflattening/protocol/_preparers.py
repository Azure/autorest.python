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
    from typing import Dict, List, Optional

_SERIALIZER = Serializer()


def _prepare_put_array_request(
    body=None,  # type: Optional[List["_models.Resource"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/array")

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


def _prepare_get_array_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/array")

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


def _prepare_put_wrapped_array_request(
    body=None,  # type: Optional[List["_models.WrappedProduct"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/wrappedarray")

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


def _prepare_get_wrapped_array_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/wrappedarray")

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


def _prepare_put_dictionary_request(
    body=None,  # type: Optional[Dict[str, "_models.FlattenedProduct"]]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/dictionary")

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


def _prepare_get_dictionary_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/dictionary")

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


def _prepare_put_resource_collection_request(
    body=None,  # type: Optional["_models.ResourceCollection"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/resourcecollection")

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


def _prepare_get_resource_collection_request(
    **kwargs,  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/resourcecollection")

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


def _prepare_put_simple_product_request(
    body=None,  # type: Optional["_models.SimpleProduct"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/customFlattening")

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


def _prepare_post_flattened_simple_product_request(
    body=None,  # type: Optional["_models.SimpleProduct"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/customFlattening")

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


def _prepare_put_simple_product_with_grouping_request(
    name,  # type: str
    body=None,  # type: Optional["_models.SimpleProduct"]
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/model-flatten/customFlattening/parametergrouping/{name}/")
    path_format_arguments = {
        "name": _SERIALIZER.url("name", name, "str"),
    }
    url = _format_url_section(url, **path_format_arguments)

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
