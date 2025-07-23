# coding=utf-8

"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List

from ._operations import _ApiKeyClientOperationsMixin as Generated

class _ApiKeyClientOperationsMixin(Generated):
    """This class is a mixin that adds custom operations to the ApiKeyClient."""

    def patch_added_operation(self, **kwargs):
        """An example of a custom operation added to the ApiKeyClient."""
        # Implement your custom operation logic here
        pass

__all__: List[str] = ["_ApiKeyClientOperationsMixin"]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
