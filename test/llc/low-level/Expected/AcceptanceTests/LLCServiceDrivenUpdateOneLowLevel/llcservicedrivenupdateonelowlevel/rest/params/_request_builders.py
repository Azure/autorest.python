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

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, IO, Optional, TypeVar, Union

    T = TypeVar("T")
    JSONType = Any

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_get_required_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get true Boolean value on path.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword parameter: I am a required parameter.
    :paramtype parameter: str
    :keyword new_parameter: I'm a new input optional parameter.
    :paramtype new_parameter: str
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    parameter = kwargs.pop('parameter')  # type: str
    new_parameter = kwargs.pop('new_parameter', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = '/servicedriven/parameters'

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['parameter'] = _SERIALIZER.query("parameter", parameter, 'str')
    if new_parameter is not None:
        query_parameters['new_parameter'] = _SERIALIZER.query("new_parameter", new_parameter, 'str')

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


def build_post_parameters_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """POST a JSON or a JPEG.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. I am a body parameter with a new content type. My only
     valid JSON entry is { url: "http://example.org/myimage.jpeg" }.
    :paramtype json: JSONType
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). I am a body parameter with a new content type. My only valid
     JSON entry is { url: "http://example.org/myimage.jpeg" }.
    :paramtype content: any
    :keyword str content_type: Media type of the body sent to the API. Default value is
     "application/json". Allowed values are: "image/jpeg", "application/json."
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = b'bytes'  # Optional.
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = '/servicedriven/parameters'

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_delete_parameters_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Delete something.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    # Construct URL
    url = '/servicedriven/parameters'

    return HttpRequest(
        method="DELETE",
        url=url,
        **kwargs
    )


def build_get_new_operation_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """I'm a new operation.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    accept = "application/json"
    # Construct URL
    url = '/servicedriven/newpath'

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )
