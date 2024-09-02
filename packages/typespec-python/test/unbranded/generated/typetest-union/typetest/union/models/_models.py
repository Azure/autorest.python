# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Literal, Mapping, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Cat(_model_base.Model):
    """Cat.


    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Dog(_model_base.Model):
    """Dog.


    :ivar bark: Required.
    :vartype bark: str
    """

    bark: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        bark: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class EnumsOnlyCases(_model_base.Model):
    """EnumsOnlyCases.


    :ivar lr: This should be receive/send the left variant. Required. Is one of the following
     types: Literal["left"], Literal["right"], Literal["up"], Literal["down"]
    :vartype lr: str or str or str or str
    :ivar ud: This should be receive/send the up variant. Required. Is either a Literal["up"] type
     or a Literal["down"] type.
    :vartype ud: str or str
    """

    lr: Literal["left", "right", "up", "down"] = rest_field()
    """This should be receive/send the left variant. Required. Is one of the following types:
     Literal[\"left\"], Literal[\"right\"], Literal[\"up\"], Literal[\"down\"]"""
    ud: Literal["up", "down"] = rest_field()
    """This should be receive/send the up variant. Required. Is either a Literal[\"up\"] type or a
     Literal[\"down\"] type."""

    @overload
    def __init__(
        self,
        *,
        lr: Literal["left", "right", "up", "down"],
        ud: Literal["up", "down"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse(_model_base.Model):
    """GetResponse.


    :ivar prop: Required.
    :vartype prop: ~typetest.union.models.MixedTypesCases
    """

    prop: "_models.MixedTypesCases" = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        prop: "_models.MixedTypesCases",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse1(_model_base.Model):
    """GetResponse1.


    :ivar prop: Required.
    :vartype prop: ~typetest.union.models.MixedLiteralsCases
    """

    prop: "_models.MixedLiteralsCases" = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        prop: "_models.MixedLiteralsCases",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse2(_model_base.Model):
    """GetResponse2.


    :ivar prop: Required.
    :vartype prop: ~typetest.union.models.StringAndArrayCases
    """

    prop: "_models.StringAndArrayCases" = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        prop: "_models.StringAndArrayCases",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse3(_model_base.Model):
    """GetResponse3.


    :ivar prop: Required.
    :vartype prop: ~typetest.union.models.EnumsOnlyCases
    """

    prop: "_models.EnumsOnlyCases" = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        prop: "_models.EnumsOnlyCases",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse4(_model_base.Model):
    """GetResponse4.


    :ivar prop: Required. Is either a Cat type or a Dog type.
    :vartype prop: ~typetest.union.models.Cat or ~typetest.union.models.Dog
    """

    prop: Union["_models.Cat", "_models.Dog"] = rest_field()
    """Required. Is either a Cat type or a Dog type."""

    @overload
    def __init__(
        self,
        *,
        prop: Union["_models.Cat", "_models.Dog"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse5(_model_base.Model):
    """GetResponse5.


    :ivar prop: Required. Is one of the following types: float, float, float
    :vartype prop: float or float or float
    """

    prop: float = rest_field()
    """Required. Is one of the following types: float, float, float"""

    @overload
    def __init__(
        self,
        *,
        prop: float,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse6(_model_base.Model):
    """GetResponse6.


    :ivar prop: Required. Is one of the following types: Literal[1], Literal[2], Literal[3]
    :vartype prop: int or int or int
    """

    prop: Literal[1, 2, 3] = rest_field()
    """Required. Is one of the following types: Literal[1], Literal[2], Literal[3]"""

    @overload
    def __init__(
        self,
        *,
        prop: Literal[1, 2, 3],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse7(_model_base.Model):
    """GetResponse7.


    :ivar prop: Required. Known values are: "b" and "c".
    :vartype prop: str or ~typetest.union.models.StringExtensibleNamedUnion
    """

    prop: Union[str, "_models.StringExtensibleNamedUnion"] = rest_field()
    """Required. Known values are: \"b\" and \"c\"."""

    @overload
    def __init__(
        self,
        *,
        prop: Union[str, "_models.StringExtensibleNamedUnion"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse8(_model_base.Model):
    """GetResponse8.


    :ivar prop: Required. Is one of the following types: Literal["b"], Literal["c"], str
    :vartype prop: str or str or str
    """

    prop: Union[Literal["b"], Literal["c"], str] = rest_field()
    """Required. Is one of the following types: Literal[\"b\"], Literal[\"c\"], str"""

    @overload
    def __init__(
        self,
        *,
        prop: Union[Literal["b"], Literal["c"], str],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GetResponse9(_model_base.Model):
    """GetResponse9.


    :ivar prop: Required. Is one of the following types: Literal["a"], Literal["b"], Literal["c"]
    :vartype prop: str or str or str
    """

    prop: Literal["a", "b", "c"] = rest_field()
    """Required. Is one of the following types: Literal[\"a\"], Literal[\"b\"], Literal[\"c\"]"""

    @overload
    def __init__(
        self,
        *,
        prop: Literal["a", "b", "c"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class MixedLiteralsCases(_model_base.Model):
    """MixedLiteralsCases.


    :ivar string_literal: This should be receive/send the "a" variant. Required. Is one of the
     following types: Literal["a"], Literal[2], float, Literal[True]
    :vartype string_literal: str or int or float or bool
    :ivar int_literal: This should be receive/send the 2 variant. Required. Is one of the following
     types: Literal["a"], Literal[2], float, Literal[True]
    :vartype int_literal: str or int or float or bool
    :ivar float_literal: This should be receive/send the 3.3 variant. Required. Is one of the
     following types: Literal["a"], Literal[2], float, Literal[True]
    :vartype float_literal: str or int or float or bool
    :ivar boolean_literal: This should be receive/send the true variant. Required. Is one of the
     following types: Literal["a"], Literal[2], float, Literal[True]
    :vartype boolean_literal: str or int or float or bool
    """

    string_literal: Literal["a", 2, True] = rest_field(name="stringLiteral")
    """This should be receive/send the \"a\" variant. Required. Is one of the following types:
     Literal[\"a\"], Literal[2], float, Literal[True]"""
    int_literal: Literal["a", 2, True] = rest_field(name="intLiteral")
    """This should be receive/send the 2 variant. Required. Is one of the following types:
     Literal[\"a\"], Literal[2], float, Literal[True]"""
    float_literal: Literal["a", 2, True] = rest_field(name="floatLiteral")
    """This should be receive/send the 3.3 variant. Required. Is one of the following types:
     Literal[\"a\"], Literal[2], float, Literal[True]"""
    boolean_literal: Literal["a", 2, True] = rest_field(name="booleanLiteral")
    """This should be receive/send the true variant. Required. Is one of the following types:
     Literal[\"a\"], Literal[2], float, Literal[True]"""

    @overload
    def __init__(
        self,
        *,
        string_literal: Literal["a", 2, True],
        int_literal: Literal["a", 2, True],
        float_literal: Literal["a", 2, True],
        boolean_literal: Literal["a", 2, True],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class MixedTypesCases(_model_base.Model):
    """MixedTypesCases.


    :ivar model: This should be receive/send the Cat variant. Required. Is one of the following
     types: Cat, Literal["a"], int, bool
    :vartype model: ~typetest.union.models.Cat or str or int or bool
    :ivar literal: This should be receive/send the "a" variant. Required. Is one of the following
     types: Cat, Literal["a"], int, bool
    :vartype literal: ~typetest.union.models.Cat or str or int or bool
    :ivar int_property: This should be receive/send the int variant. Required. Is one of the
     following types: Cat, Literal["a"], int, bool
    :vartype int_property: ~typetest.union.models.Cat or str or int or bool
    :ivar boolean: This should be receive/send the boolean variant. Required. Is one of the
     following types: Cat, Literal["a"], int, bool
    :vartype boolean: ~typetest.union.models.Cat or str or int or bool
    :ivar array: This should be receive/send 4 element with Cat, "a", int, and boolean. Required.
    :vartype array: list[~typetest.union.models.Cat or str or int or bool]
    """

    model: Union["_models.Cat", Literal["a"], int, bool] = rest_field()
    """This should be receive/send the Cat variant. Required. Is one of the following types: Cat,
     Literal[\"a\"], int, bool"""
    literal: Union["_models.Cat", Literal["a"], int, bool] = rest_field()
    """This should be receive/send the \"a\" variant. Required. Is one of the following types: Cat,
     Literal[\"a\"], int, bool"""
    int_property: Union["_models.Cat", Literal["a"], int, bool] = rest_field(name="int")
    """This should be receive/send the int variant. Required. Is one of the following types: Cat,
     Literal[\"a\"], int, bool"""
    boolean: Union["_models.Cat", Literal["a"], int, bool] = rest_field()
    """This should be receive/send the boolean variant. Required. Is one of the following types: Cat,
     Literal[\"a\"], int, bool"""
    array: List[Union["_models.Cat", Literal["a"], int, bool]] = rest_field()
    """This should be receive/send 4 element with Cat, \"a\", int, and boolean. Required."""

    @overload
    def __init__(
        self,
        *,
        model: Union["_models.Cat", Literal["a"], int, bool],
        literal: Union["_models.Cat", Literal["a"], int, bool],
        int_property: Union["_models.Cat", Literal["a"], int, bool],
        boolean: Union["_models.Cat", Literal["a"], int, bool],
        array: List[Union["_models.Cat", Literal["a"], int, bool]],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class StringAndArrayCases(_model_base.Model):
    """StringAndArrayCases.


    :ivar string: This should be receive/send the string variant. Required. Is either a str type or
     a [str] type.
    :vartype string: str or list[str]
    :ivar array: This should be receive/send the array variant. Required. Is either a str type or a
     [str] type.
    :vartype array: str or list[str]
    """

    string: Union[str, List[str]] = rest_field()
    """This should be receive/send the string variant. Required. Is either a str type or a [str] type."""
    array: Union[str, List[str]] = rest_field()
    """This should be receive/send the array variant. Required. Is either a str type or a [str] type."""

    @overload
    def __init__(
        self,
        *,
        string: Union[str, List[str]],
        array: Union[str, List[str]],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
