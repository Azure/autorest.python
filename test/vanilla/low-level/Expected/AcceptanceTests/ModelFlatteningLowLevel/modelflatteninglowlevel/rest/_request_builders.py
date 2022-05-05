# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Dict, IO, List, Optional, Union, overload

from msrest import Serializer

from azure.core.rest import HttpRequest
from azure.core.utils import case_insensitive_dict

from .._vendor import _format_url_section

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

# fmt: off

@overload
def build_put_array_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as an Array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: External Resource as an Array to put. Default value is None.
    :paramtype json: list[JSON]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = [
                {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "tags": {
                        "str": "str"  # Optional. Dictionary of :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            ]
    """


@overload
def build_put_array_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as an Array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: External Resource as an Array to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put_array_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as an Array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: External Resource as an Array to put. Is either a list type or a IO type.
     Default value is None.
    :paramtype json: list[JSON] or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/model-flatten/array"

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


def build_get_array_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get External Resource as an Array.

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
    _url = "/model-flatten/array"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_put_wrapped_array_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """No need to have a route in Express server for this operation. Used to verify the type flattened
    is not removed if it's referenced in an array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: External Resource as an Array to put. Default value is None.
    :paramtype json: list[JSON]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = [
                {
                    "value": "str"  # Optional. the product value.
                }
            ]
    """


@overload
def build_put_wrapped_array_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """No need to have a route in Express server for this operation. Used to verify the type flattened
    is not removed if it's referenced in an array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: External Resource as an Array to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put_wrapped_array_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """No need to have a route in Express server for this operation. Used to verify the type flattened
    is not removed if it's referenced in an array.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: External Resource as an Array to put. Is either a list type or a IO type.
     Default value is None.
    :paramtype json: list[JSON] or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/model-flatten/wrappedarray"

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


def build_get_wrapped_array_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """No need to have a route in Express server for this operation. Used to verify the type flattened
    is not removed if it's referenced in an array.

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
    _url = "/model-flatten/wrappedarray"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_put_dictionary_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as a Dictionary.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: External Resource as a Dictionary to put. Default value is None.
    :paramtype json: dict[str, JSON]
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "str": {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "properties": {
                        "p.name": "str",  # Optional.
                        "provisioningState": "str",  # Optional.
                        "provisioningStateValues": "str",  # Optional. Known values
                          are: "Succeeded", "Failed", "canceled", "Accepted", "Creating",
                          "Created", "Updating", "Updated", "Deleting", "Deleted", and "OK".
                        "type": "str"  # Optional.
                    },
                    "tags": {
                        "str": "str"  # Optional. Dictionary of :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            }
    """


@overload
def build_put_dictionary_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as a Dictionary.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: External Resource as a Dictionary to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put_dictionary_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as a Dictionary.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: External Resource as a Dictionary to put. Is either a dict type or a IO type.
     Default value is None.
    :paramtype json: dict[str, JSON] or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/model-flatten/dictionary"

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


def build_get_dictionary_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get External Resource as a Dictionary.

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
    _url = "/model-flatten/dictionary"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_put_resource_collection_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as a ResourceCollection.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: External Resource as a ResourceCollection to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "arrayofresources": [
                    {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional.
                            "provisioningState": "str",  # Optional.
                            "provisioningStateValues": "str",  # Optional. Known
                              values are: "Succeeded", "Failed", "canceled", "Accepted",
                              "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
                              and "OK".
                            "type": "str"  # Optional.
                        },
                        "tags": {
                            "str": "str"  # Optional. Dictionary of
                              :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                ],
                "dictionaryofresources": {
                    "str": {
                        "id": "str",  # Optional. Resource Id.
                        "location": "str",  # Optional. Resource Location.
                        "name": "str",  # Optional. Resource Name.
                        "properties": {
                            "p.name": "str",  # Optional. Dictionary of
                              :code:`<FlattenedProduct>`.
                            "provisioningState": "str",  # Optional. Dictionary
                              of :code:`<FlattenedProduct>`.
                            "provisioningStateValues": "str",  # Optional. Known
                              values are: "Succeeded", "Failed", "canceled", "Accepted",
                              "Creating", "Created", "Updating", "Updated", "Deleting", "Deleted",
                              and "OK".
                            "type": "str"  # Optional. Dictionary of
                              :code:`<FlattenedProduct>`.
                        },
                        "tags": {
                            "str": "str"  # Optional. Dictionary of
                              :code:`<string>`.
                        },
                        "type": "str"  # Optional. Resource Type.
                    }
                },
                "productresource": {
                    "id": "str",  # Optional. Resource Id.
                    "location": "str",  # Optional. Resource Location.
                    "name": "str",  # Optional. Resource Name.
                    "properties": {
                        "p.name": "str",  # Optional. Flattened product.
                        "provisioningState": "str",  # Optional. Flattened product.
                        "provisioningStateValues": "str",  # Optional. Known values
                          are: "Succeeded", "Failed", "canceled", "Accepted", "Creating",
                          "Created", "Updating", "Updated", "Deleting", "Deleted", and "OK".
                        "type": "str"  # Optional. Flattened product.
                    },
                    "tags": {
                        "str": "str"  # Optional. Dictionary of :code:`<string>`.
                    },
                    "type": "str"  # Optional. Resource Type.
                }
            }
    """


@overload
def build_put_resource_collection_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as a ResourceCollection.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: External Resource as a ResourceCollection to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put_resource_collection_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put External Resource as a ResourceCollection.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: External Resource as a ResourceCollection to put. Is either a model type or a IO
     type. Default value is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/model-flatten/resourcecollection"

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


def build_get_resource_collection_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Get External Resource as a ResourceCollection.

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
    _url = "/model-flatten/resourcecollection"

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_headers,
        **kwargs
    )


@overload
def build_put_simple_product_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Simple body product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Unique identifier representing a specific
                  product for a given latitude & longitude. For example, uberX in San Francisco
                  will have a different product_id than uberX in Los Angeles. Required.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Required.
                    "max_product_display_name": "str",  # Display name of product.
                      Required.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }
    """


@overload
def build_put_simple_product_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Simple body product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put_simple_product_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Simple body product to put. Is either a model type or a IO type. Default value
     is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/model-flatten/customFlattening"

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


@overload
def build_post_flattened_simple_product_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Flattened Simple Product with client flattening true on the parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Simple body product to post. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Unique identifier representing a specific
                  product for a given latitude & longitude. For example, uberX in San Francisco
                  will have a different product_id than uberX in Los Angeles. Required.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Required.
                    "max_product_display_name": "str",  # Display name of product.
                      Required.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }
    """


@overload
def build_post_flattened_simple_product_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Flattened Simple Product with client flattening true on the parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Simple body product to post. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_post_flattened_simple_product_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Flattened Simple Product with client flattening true on the parameter.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Simple body product to post. Is either a model type or a IO type. Default value
     is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/model-flatten/customFlattening"

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


@overload
def build_put_simple_product_with_grouping_request(
    name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param name: Product name with value 'groupproduct'. Required.
    :type name: str
    :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Simple body product to put. Default value is None.
    :paramtype json: JSON
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your body input.
            json = {
                "base_product_description": "str",  # Optional. Description of product.
                "base_product_id": "str",  # Unique identifier representing a specific
                  product for a given latitude & longitude. For example, uberX in San Francisco
                  will have a different product_id than uberX in Los Angeles. Required.
                "details": {
                    "max_product_capacity": "Large",  # Default value is "Large".
                      Capacity of product. For example, 4 people. Required.
                    "max_product_display_name": "str",  # Display name of product.
                      Required.
                    "max_product_image": {
                        "@odata.value": "str",  # Optional. URL value.
                        "generic_value": "str"  # Optional. Generic URL value.
                    }
                }
            }
    """


@overload
def build_put_simple_product_with_grouping_request(
    name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param name: Product name with value 'groupproduct'. Required.
    :type name: str
    :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
     Default value is None.
    :paramtype content_type: str
    :keyword content: Simple body product to put. Default value is None.
    :paramtype content: IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """


def build_put_simple_product_with_grouping_request(
    name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Put Simple Product with client flattening true on the model.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param name: Product name with value 'groupproduct'. Required.
    :type name: str
    :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
     Default value is None.
    :paramtype content_type: str
    :keyword json: Simple body product to put. Is either a model type or a IO type. Default value
     is None.
    :paramtype json: JSON or IO
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest
    """

    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = "/model-flatten/customFlattening/parametergrouping/{name}/"
    path_format_arguments = {
        "name": _SERIALIZER.url("name", name, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

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
