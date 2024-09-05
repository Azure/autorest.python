# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, Optional, overload

from .. import _model_base
from .._model_base import rest_field


class TestModel(_model_base.Model):
    """TestModel.


    :ivar prop: Required.
    :vartype prop: str
    :ivar changed_prop:
    :vartype changed_prop: str
    """

    prop: str = rest_field()
    """Required."""
    changed_prop: Optional[str] = rest_field(name="changedProp")

    @overload
    def __init__(
        self,
        *,
        prop: str,
        changed_prop: Optional[str] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
