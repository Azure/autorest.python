# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    if sys.version_info >= (3, 9):
        from collections.abc import MutableMapping
    else:
        from typing import MutableMapping  # type: ignore
    JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

def build_put201_creating_succeeded200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Long running put request, service returns a 500, then a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put. Default value is None.
    :paramtype json: JSON
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of
                      :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }

            # response body for status code(s): 200, 201
            response.json() == {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of
                      :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/put/201/creating/succeeded/200"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_put_async_relative_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Long running put request, service returns a 500, then a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put. Default value is None.
    :paramtype json: JSON
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of
                      :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }

            # response body for status code(s): 200
            response.json() == {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of
                      :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/putasync/retry/succeeded"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_delete_provisioning202_accepted200_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Long running delete request, service returns a 500, then a  202 to the initial request, with an
    entity that contains ProvisioningState=’Accepted’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # response body for status code(s): 200, 202
            response.json() == {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of
                      :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/delete/provisioning/202/accepted/200/succeeded"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_delete202_retry200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Long running delete request, service returns a 500, then a 202 to the initial request. Polls
    return this value until the last poll returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/delete/202/retry/200"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_delete_async_relative_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Long running delete request, service returns a 500, then a 202 to the initial request. Poll the
    endpoint indicated in the Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/deleteasync/retry/succeeded"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_post202_retry200_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Long running post request, service returns a 500, then a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put. Default value is None.
    :paramtype json: JSON
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of
                      :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/post/202/retry/200"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )


def build_post_async_relative_retry_succeeded_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Long running post request, service returns a 500, then a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put. Default value is None.
    :paramtype json: JSON
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put. Default value is None.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "id": "str",  # Optional. Resource Id.
                "location": "str",  # Optional. Resource Location.
                "name": "str",  # Optional. Resource Name.
                "properties": {
                    "provisioningState": "str",  # Optional.
                    "provisioningStateValues": "str"  # Optional. Known values are:
                      "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created",
                      "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of
                      :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/lro/retryerror/postasync/retry/succeeded"

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_headers,
        **kwargs
    )
