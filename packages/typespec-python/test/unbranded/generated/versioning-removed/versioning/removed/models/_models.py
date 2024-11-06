# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import _types, models as _models


class ModelV2(_model_base.Model):
    """ModelV2.


    :ivar prop: Required.
    :vartype prop: str
    :ivar enum_prop: Required. "enumMemberV2"
    :vartype enum_prop: str or ~versioning.removed.models.EnumV2
    :ivar union_prop: Required. Is either a str type or a float type.
    :vartype union_prop: str or float
    """

    prop: str = rest_field()
    """Required."""
    enum_prop: Union[str, "_models.EnumV2"] = rest_field(name="enumProp")
    """Required. \"enumMemberV2\""""
    union_prop: "_types.UnionV2" = rest_field(name="unionProp")
    """Required. Is either a str type or a float type."""

    @overload
    def __init__(
        self,
        *,
        prop: str,
        enum_prop: Union[str, "_models.EnumV2"],
        union_prop: "_types.UnionV2",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelV3(_model_base.Model):
    """ModelV3.


    :ivar id: Required.
    :vartype id: str
    :ivar enum_prop: Required. Known values are: "enumMemberV1" and "enumMemberV2Preview".
    :vartype enum_prop: str or ~versioning.removed.models.EnumV3
    """

    id: str = rest_field()
    """Required."""
    enum_prop: Union[str, "_models.EnumV3"] = rest_field(name="enumProp")
    """Required. Known values are: \"enumMemberV1\" and \"enumMemberV2Preview\"."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        enum_prop: Union[str, "_models.EnumV3"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
