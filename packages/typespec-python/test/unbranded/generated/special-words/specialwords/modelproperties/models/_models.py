# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from ... import _model_base
from ..._model_base import rest_field


class SameAsModel(_model_base.Model):
    """SameAsModel.

    All required parameters must be populated in order to send to server.

    :ivar same_as_model: Required.
    :vartype same_as_model: str
    """

    same_as_model: str = rest_field(name="SameAsModel")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        same_as_model: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)