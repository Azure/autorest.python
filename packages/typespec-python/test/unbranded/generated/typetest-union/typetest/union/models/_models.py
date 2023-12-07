# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Mapping, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import _types, models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class Cat(_model_base.Model):
    """Cat.

    All required parameters must be populated in order to send to server.

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
    ):
        ...

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

    All required parameters must be populated in order to send to server.

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
    ):
        ...

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

    All required parameters must be populated in order to send to server.

    :ivar lr: This should be receive/send the left variant. Required. Is either a Union[str,
     "_models.LR"] type or a Union[str, "_models.UD"] type.
    :vartype lr: str or ~typetest.union.models.LR or str or ~typetest.union.models.UD
    :ivar ud: This should be receive/send the up variant. Required. Is either a Union[str,
     "_models.UD"] type or a Union[str, "_models.UD"] type.
    :vartype ud: str or ~typetest.union.models.UD or str or ~typetest.union.models.UD
    """

    lr: Union[str, "_models.LR", str, "_models.UD"] = rest_field()
    """This should be receive/send the left variant. Required. Is either a Union[str, \"_models.LR\"]
     type or a Union[str, \"_models.UD\"] type."""
    ud: Union[str, "_models.UD", str, "_models.UD"] = rest_field()
    """This should be receive/send the up variant. Required. Is either a Union[str, \"_models.UD\"]
     type or a Union[str, \"_models.UD\"] type."""

    @overload
    def __init__(
        self,
        *,
        lr: Union[str, "_models.LR", str, "_models.UD"],
        ud: Union[str, "_models.UD", str, "_models.UD"],
    ):
        ...

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

    All required parameters must be populated in order to send to server.

    :ivar prop: Required. Is one of the following types: Literal["a"], Literal["b"], Literal["c"]
    :vartype prop: str or str or str
    """

    prop: Union[Literal["a"], Literal["b"], Literal["c"]] = rest_field()
    """Required. Is one of the following types: Literal[\"a\"], Literal[\"b\"], Literal[\"c\"]"""

    @overload
    def __init__(
        self,
        *,
        prop: Union[Literal["a"], Literal["b"], Literal["c"]],
    ):
        ...

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

    All required parameters must be populated in order to send to server.

    :ivar prop: Required. Is one of the following types: str, Literal["b"], Literal["c"]
    :vartype prop: str or str or str
    """

    prop: Union[str, Literal["b"], Literal["c"]] = rest_field()
    """Required. Is one of the following types: str, Literal[\"b\"], Literal[\"c\"]"""

    @overload
    def __init__(
        self,
        *,
        prop: Union[str, Literal["b"], Literal["c"]],
    ):
        ...

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

    All required parameters must be populated in order to send to server.

    :ivar prop: Required. Is one of the following types: str, Literal["b"], Literal["c"]
    :vartype prop: str or str or str
    """

    prop: "_types.StringExtensibleNamedUnion" = rest_field()
    """Required. Is one of the following types: str, Literal[\"b\"], Literal[\"c\"]"""

    @overload
    def __init__(
        self,
        *,
        prop: "_types.StringExtensibleNamedUnion",
    ):
        ...

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

    All required parameters must be populated in order to send to server.

    :ivar prop: Required. Is one of the following types: Literal[1], Literal[2], Literal[3]
    :vartype prop: int or int or int
    """

    prop: Union[Literal[1], Literal[2], Literal[3]] = rest_field()
    """Required. Is one of the following types: Literal[1], Literal[2], Literal[3]"""

    @overload
    def __init__(
        self,
        *,
        prop: Union[Literal[1], Literal[2], Literal[3]],
    ):
        ...

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

    All required parameters must be populated in order to send to server.

    :ivar prop: Required. Is one of the following types: float, float, float
    :vartype prop: float or float or float
    """

    prop: Union[float, float, float] = rest_field()
    """Required. Is one of the following types: float, float, float"""

    @overload
    def __init__(
        self,
        *,
        prop: Union[float, float, float],
    ):
        ...

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

    All required parameters must be populated in order to send to server.

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
    ):
        ...

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

    All required parameters must be populated in order to send to server.

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
    ):
        ...

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

    All required parameters must be populated in order to send to server.

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
    ):
        ...

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

    All required parameters must be populated in order to send to server.

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
    ):
        ...

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

    All required parameters must be populated in order to send to server.

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
    ):
        ...

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

    All required parameters must be populated in order to send to server.

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

    string_literal: Union[Literal["a"], Literal[2], float, Literal[True]] = rest_field(name="stringLiteral")
    """This should be receive/send the \"a\" variant. Required. Is one of the following types:
     Literal[\"a\"], Literal[2], float, Literal[True]"""
    int_literal: Union[Literal["a"], Literal[2], float, Literal[True]] = rest_field(name="intLiteral")
    """This should be receive/send the 2 variant. Required. Is one of the following types:
     Literal[\"a\"], Literal[2], float, Literal[True]"""
    float_literal: Union[Literal["a"], Literal[2], float, Literal[True]] = rest_field(name="floatLiteral")
    """This should be receive/send the 3.3 variant. Required. Is one of the following types:
     Literal[\"a\"], Literal[2], float, Literal[True]"""
    boolean_literal: Union[Literal["a"], Literal[2], float, Literal[True]] = rest_field(name="booleanLiteral")
    """This should be receive/send the true variant. Required. Is one of the following types:
     Literal[\"a\"], Literal[2], float, Literal[True]"""

    @overload
    def __init__(
        self,
        *,
        string_literal: Union[Literal["a"], Literal[2], float, Literal[True]],
        int_literal: Union[Literal["a"], Literal[2], float, Literal[True]],
        float_literal: Union[Literal["a"], Literal[2], float, Literal[True]],
        boolean_literal: Union[Literal["a"], Literal[2], float, Literal[True]],
    ):
        ...

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

    All required parameters must be populated in order to send to server.

    :ivar model: This should be receive/send the Cat variant. Required. Is one of the following
     types: Cat, Literal["a"], int, bool
    :vartype model: ~typetest.union.models.Cat or str or int or bool
    :ivar literal: This should be receive/send the "a" variant. Required. Is one of the following
     types: Cat, Literal["a"], int, bool
    :vartype literal: ~typetest.union.models.Cat or str or int or bool
    :ivar int: This should be receive/send the int variant. Required. Is one of the following
     types: Cat, Literal["a"], int, bool
    :vartype int: ~typetest.union.models.Cat or str or int or bool
    :ivar boolean: This should be receive/send the boolean variant. Required. Is one of the
     following types: Cat, Literal["a"], int, bool
    :vartype boolean: ~typetest.union.models.Cat or str or int or bool
    """

    model: Union["_models.Cat", Literal["a"], int, bool] = rest_field()
    """This should be receive/send the Cat variant. Required. Is one of the following types: Cat,
     Literal[\"a\"], int, bool"""
    literal: Union["_models.Cat", Literal["a"], int, bool] = rest_field()
    """This should be receive/send the \"a\" variant. Required. Is one of the following types: Cat,
     Literal[\"a\"], int, bool"""
    int: Union["_models.Cat", Literal["a"], int, bool] = rest_field()
    """This should be receive/send the int variant. Required. Is one of the following types: Cat,
     Literal[\"a\"], int, bool"""
    boolean: Union["_models.Cat", Literal["a"], int, bool] = rest_field()
    """This should be receive/send the boolean variant. Required. Is one of the following types: Cat,
     Literal[\"a\"], int, bool"""

    @overload
    def __init__(
        self,
        *,
        model: Union["_models.Cat", Literal["a"], int, bool],
        literal: Union["_models.Cat", Literal["a"], int, bool],
        int: Union["_models.Cat", Literal["a"], int, bool],
        boolean: Union["_models.Cat", Literal["a"], int, bool],
    ):
        ...

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

    All required parameters must be populated in order to send to server.

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
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
