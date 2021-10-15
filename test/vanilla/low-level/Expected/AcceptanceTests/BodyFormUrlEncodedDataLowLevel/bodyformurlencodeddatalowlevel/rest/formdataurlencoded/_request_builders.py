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

from ..._vendor import _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional

_SERIALIZER = Serializer()

# fmt: off

def build_update_pet_with_form_request(
    pet_id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Updates a pet in the store with form data.

    Updates a pet in the store with form data.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    :param pet_id: ID of pet that needs to be updated.
    :type pet_id: int
    :keyword data: Pass in dictionary that contains form data to include in the body of the
     request. Can take a value of dog, or cat, or fish.
    :paramtype data: dict[str, any]
    :keyword content: Pass in binary content you want in the body of the request (typically bytes,
     a byte iterator, or stream input). Can take a value of dog, or cat, or fish.
    :paramtype content: any
    :return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's
     `send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to
     incorporate this response into your code flow.
    :rtype: ~azure.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # form-encoded input template you can fill out and use as your `data` input.
            data = {
                content: {},  # Optional. Pass in binary content you want in the body of the request (typically bytes, a byte iterator, or stream input). Can take a value of dog, or cat, or fish.
                data: {
                    "str": {}  # Optional. Pass in dictionary that contains form data to include in the body of the request. Can take a value of dog, or cat, or fish.
                },
                name: "str",  # Optional. Updated name of the pet.
                pet_age: 0,  # How many years is it old?.
                pet_food: "str",  # Can take a value of meat, or fish, or plant. Possible values are: "meat", "fish", and "plant".
                pet_type: "str",  # Can take a value of dog, or cat, or fish. Possible values are: "dog", "cat", and "fish".
                status: "str"  # Optional. Updated status of the pet.
            }
    """

    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/formsdataurlencoded/pet/add/{petId}')
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'int'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )
