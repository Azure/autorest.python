# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List
from ..models import Product, AddedModel
from ._operations import DPGClientOperationsMixin as DPGClientOperationsMixinGenerated


class DPGClientOperationsMixin(DPGClientOperationsMixinGenerated):
    def get_model(self, **kwargs) -> Product:
        response = super().get_model(**kwargs)

        # want to test mypy in generated code, so linking to models
        if not response.added_in_customization == "bonjour!":
            raise ValueError("Incorrect Product, not the customized one")
        return response

    def added_operation(self) -> AddedModel:
        return AddedModel()


__all__: List[str] = [
    "DPGClientOperationsMixin"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
