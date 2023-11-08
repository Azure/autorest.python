# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List, overload, Optional, Mapping, Any
from .. import _model_base
from .._model_base import rest_field

class TestProperties(_model_base.Model):
    name: Optional[str] = rest_field()

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Test(_model_base.Model):
    properties: Optional["TestProperties"] = rest_field()
    id: Optional[str] = rest_field()

    @overload
    def __init__(
        self,
        *,
        properties: Optional["TestProperties"] = None,
        id: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        ...

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


__all__: List[str] = [
    "Test",
    "TestProperties",
]  # Add all objects you want publicly available to users at this package level



def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
