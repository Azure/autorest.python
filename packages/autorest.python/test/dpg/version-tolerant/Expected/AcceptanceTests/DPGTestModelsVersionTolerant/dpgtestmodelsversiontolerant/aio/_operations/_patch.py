# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List, Any
from ...models import Product
from ._operations import _DPGClientOperationsMixin as _DPGClientOperationsMixinGenerated


class _DPGClientOperationsMixin(_DPGClientOperationsMixinGenerated):
    async def get_model(self, mode: str, **kwargs: Any) -> Product:
        product = await super().get_model(mode, **kwargs)
        if product.added_in_customization != "bonjour!":
            raise ValueError("Should have added customization")
        return product

    @staticmethod
    def added_method() -> str:
        return "Added!"


__all__: List[str] = [
    "_DPGClientOperationsMixin"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
