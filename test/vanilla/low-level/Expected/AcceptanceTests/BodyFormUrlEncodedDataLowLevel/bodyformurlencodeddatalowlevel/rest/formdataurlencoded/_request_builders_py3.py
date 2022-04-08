# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import abc
from typing import Any, Optional

from msrest import Serializer

from azure.core.rest import HttpRequest

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


@abc.abstractmethod
def build_update_pet_with_form_request(*args, **kwargs) -> HttpRequest:
    """You need to write a custom operation for "build_update_pet_with_form_request". Please refer to
    https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    """

    raise NotImplementedError(
        "You need to write a custom operation for 'build_update_pet_with_form_request'. "
        "Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
    )


@abc.abstractmethod
def build_partial_constant_body_request(*args, **kwargs) -> HttpRequest:
    """You need to write a custom operation for "build_partial_constant_body_request". Please refer to
    https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.

    See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this request builder
    into your code flow.

    """

    raise NotImplementedError(
        "You need to write a custom operation for 'build_partial_constant_body_request'. "
        "Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
    )
