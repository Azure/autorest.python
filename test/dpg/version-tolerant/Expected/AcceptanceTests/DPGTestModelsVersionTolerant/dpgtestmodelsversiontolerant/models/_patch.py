# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List
from ._models import Product as ProductGenerated


class Product(ProductGenerated):
    @property
    def added_in_customization(self):
        return "bonjour!"


class AddedModel:
    @property
    def added_model_property(self):
        return "Added!"


__all__: List[str] = [
    "Product",
    "AddedModel",
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
