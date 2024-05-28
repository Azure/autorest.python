# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, TYPE_CHECKING, Union, overload

from . import _model_base
from ._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import _types, models as _models


class ModelV1(_model_base.Model):
    """ModelV1.

    All required parameters must be populated in order to send to server.

    :ivar prop: Required.
    :vartype prop: str
    :ivar enum_prop: Required. Known values are: "enumMemberV1" and "enumMemberV2".
    :vartype enum_prop: str or ~versioning.added.models.EnumV1
    :ivar union_prop: Required. Is either a str type or a int type.
    :vartype union_prop: str or int
    """

    prop: str = rest_field()
    """Required."""
    enum_prop: Union[str, "_models.EnumV1"] = rest_field(name="enumProp")
    """Required. Known values are: \"enumMemberV1\" and \"enumMemberV2\"."""
    union_prop: "_types.UnionV1" = rest_field(name="unionProp")
    """Required. Is either a str type or a int type."""

    @overload
    def __init__(
        self,
        *,
        prop: str,
        enum_prop: Union[str, "_models.EnumV1"],
        union_prop: "_types.UnionV1",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ModelV2(_model_base.Model):
    """ModelV2.

    All required parameters must be populated in order to send to server.

    :ivar prop: Required.
    :vartype prop: str
    :ivar enum_prop: Required. "enumMember"
    :vartype enum_prop: str or ~versioning.added.models.EnumV2
    :ivar union_prop: Required. Is either a str type or a int type.
    :vartype union_prop: str or int
    """

    prop: str = rest_field()
    """Required."""
    enum_prop: Union[str, "_models.EnumV2"] = rest_field(name="enumProp")
    """Required. \"enumMember\""""
    union_prop: "_types.UnionV2" = rest_field(name="unionProp")
    """Required. Is either a str type or a int type."""

    @overload
    def __init__(
        self,
        *,
        prop: str,
        enum_prop: Union[str, "_models.EnumV2"],
        union_prop: "_types.UnionV2",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
