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
    from typing import Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_poll_with_parameterized_endpoints_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Poll with method and client level parameters in endpoint.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/lroParameterizedEndpoints')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_poll_with_constant_parameterized_endpoints_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Poll with method and client level parameters in endpoint, with a constant value.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword constant_parameter: Next link for the list operation. The default value is
     "iAmConstant". Note that overriding this default value may result in unsupported behavior.
    :paramtype constant_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    constant_parameter = kwargs.pop('constant_parameter', "iAmConstant")  # type: str

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/lroConstantParameterizedEndpoints/{constantParameter}')
    path_format_arguments = {
        "constantParameter": _SERIALIZER.url("constant_parameter", constant_parameter, 'str', skip_quote=True),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )
