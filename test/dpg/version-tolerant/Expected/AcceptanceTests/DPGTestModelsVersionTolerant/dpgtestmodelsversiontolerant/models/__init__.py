# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import Input
from ._models import LROProduct
from ._patch import Product
from ._models import ProductResult


from ._enums import (
    ProductReceived,
)

from ._patch import AddedModel
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AddedModel",
    "Input",
    "LROProduct",
    "Product",
    "ProductResult",
    "ProductReceived",
]

_patch_sdk()
