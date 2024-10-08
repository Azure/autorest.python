# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Literal, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class Float32Type(_model_base.Model):
    """Float32Type.


    :ivar values_property: An array of numeric values. Required.
    :vartype values_property: list[float]
    :ivar value: Required.
    :vartype value: float
    """

    values_property: List[float] = rest_field(name="values")
    """An array of numeric values. Required."""
    value: float = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        values_property: List[float],
        value: float,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Float32ValuesType(Float32Type):
    """An instantiated type representing float32 values type.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar values_property: An array of numeric values. Required.
    :vartype values_property: list[float]
    :ivar value: Required.
    :vartype value: float
    :ivar kind: The Kind of the Float32ValuesType. Required. Default value is "Float32Values".
    :vartype kind: str
    """

    kind: Literal["Float32Values"] = rest_field()
    """The Kind of the Float32ValuesType. Required. Default value is \"Float32Values\"."""

    @overload
    def __init__(
        self,
        *,
        values_property: List[float],
        value: float,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["Float32Values"] = "Float32Values"


class Int32Type(_model_base.Model):
    """Int32Type.


    :ivar values_property: An array of numeric values. Required.
    :vartype values_property: list[int]
    :ivar value: Required.
    :vartype value: int
    """

    values_property: List[int] = rest_field(name="values")
    """An array of numeric values. Required."""
    value: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        values_property: List[int],
        value: int,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Int32ValuesType(Int32Type):
    """An instantiated type representing int32 values type.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar values_property: An array of numeric values. Required.
    :vartype values_property: list[int]
    :ivar value: Required.
    :vartype value: int
    :ivar kind: The Kind of the Int32ValuesType. Required. Default value is "Int32Values".
    :vartype kind: str
    """

    kind: Literal["Int32Values"] = rest_field()
    """The Kind of the Int32ValuesType. Required. Default value is \"Int32Values\"."""

    @overload
    def __init__(
        self,
        *,
        values_property: List[int],
        value: int,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["Int32Values"] = "Int32Values"
