# pyright: reportUnnecessaryTypeIgnoreComment=false
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List
from ._client import DPGClient as DPGClientGenerated


class DPGClient(DPGClientGenerated):
    @staticmethod
    def added_method() -> (
        str
    ):  # pylint: disable=client-method-should-not-use-static-method
        return super().added_method()  # type: ignore


__all__: List[str] = [
    "DPGClient"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
