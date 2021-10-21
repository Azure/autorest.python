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

_SERIALIZER = Serializer()


def build_put_async_retry_succeeded_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running put request, service returns a 200 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put.
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
                    "provisioningStateValues": "str"  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
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
                    "provisioningStateValues": "str"  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/customheader/putasync/retry/succeeded")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}) or {})

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_put201_creating_succeeded200_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running put request, service returns a 201 to the initial request, with an
    entity that contains ProvisioningState=’Creating’.  Polls return this value until the last poll
    returns a ‘200’ with ProvisioningState=’Succeeded’.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put.
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
                    "provisioningStateValues": "str"  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
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
                    "provisioningStateValues": "str"  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/customheader/put/201/creating/succeeded/200")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}) or {})

    return HttpRequest(method="PUT", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_post202_retry200_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running post request, service returns a 202 to the initial request, with
    'Location' and 'Retry-After' headers, Polls return a 200 with a response body after success.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put.
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
                    "provisioningStateValues": "str"  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/customheader/post/202/retry/200")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}) or {})

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)


def build_post_async_retry_succeeded_request(*, json: Any = None, content: Any = None, **kwargs: Any) -> HttpRequest:
    """x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 is required message header for
    all requests. Long running post request, service returns a 202 to the initial request, with an
    entity that contains ProvisioningState=’Creating’. Poll the endpoint indicated in the
    Azure-AsyncOperation header for operation status.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword json: Pass in a JSON-serializable object (usually a dictionary). See the template in
     our example to find the input shape. Product to put.
    :paramtype json: any
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Product to put.
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
                    "provisioningStateValues": "str"  # Optional. Possible values include: "Succeeded", "Failed", "canceled", "Accepted", "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted", "OK".
                },
                "tags": {
                    "str": "str"  # Optional. A set of tags. Dictionary of :code:`<string>`.
                },
                "type": "str"  # Optional. Resource Type.
            }
    """

    content_type = kwargs.pop("content_type", None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", "/lro/customheader/postasync/retry/succeeded")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")
    header_parameters.update(kwargs.pop("headers", {}) or {})

    return HttpRequest(method="POST", url=url, headers=header_parameters, json=json, content=content, **kwargs)
