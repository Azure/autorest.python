# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Mapping, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import _types


class BaseModel(_model_base.Model):
    """This is a base model.

    All required parameters must be populated in order to send to Azure.

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


class Model1(BaseModel):
    """The first one of the unioned model type.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar prop1: Required.
    :vartype prop1: int
    """

    prop1: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        prop1: int,
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


class Model2(BaseModel):
    """The second one of the unioned model type.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar prop2: Required.
    :vartype prop2: int
    """

    prop2: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        prop2: int,
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


class ModelWithNamedUnionProperty(_model_base.Model):
    """ModelWithNamedUnionProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar named_union: Required. Is either a Model1 type or a Model2 type.
    :vartype named_union: ~typetest.union.models.Model1 or ~typetest.union.models.Model2
    """

    named_union: "_types.MyNamedUnion" = rest_field(name="namedUnion")
    """Required. Is either a Model1 type or a Model2 type."""

    @overload
    def __init__(
        self,
        *,
        named_union: "_types.MyNamedUnion",
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


class ModelWithNamedUnionPropertyInResponse(_model_base.Model):
    """ModelWithNamedUnionPropertyInResponse.

    All required parameters must be populated in order to send to Azure.

    :ivar named_union: Required. Is either a Model1 type or a Model2 type.
    :vartype named_union: ~typetest.union.models.Model1 or ~typetest.union.models.Model2
    """

    named_union: "_types.MyNamedUnion" = rest_field(name="namedUnion")
    """Required. Is either a Model1 type or a Model2 type."""

    @overload
    def __init__(
        self,
        *,
        named_union: "_types.MyNamedUnion",
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


class ModelWithSimpleUnionProperty(_model_base.Model):
    """ModelWithSimpleUnionProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar simple_union: Required. Is either a int type or a [int] type.
    :vartype simple_union: int or list[int]
    """

    simple_union: Union[int, List[int]] = rest_field(name="simpleUnion")
    """Required. Is either a int type or a [int] type."""

    @overload
    def __init__(
        self,
        *,
        simple_union: Union[int, List[int]],
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


class ModelWithSimpleUnionPropertyInResponse(_model_base.Model):
    """ModelWithSimpleUnionPropertyInResponse.

    All required parameters must be populated in order to send to Azure.

    :ivar simple_union: Required. Is either a str type or a [int] type.
    :vartype simple_union: str or list[int]
    """

    simple_union: Union[str, List[int]] = rest_field(name="simpleUnion")
    """Required. Is either a str type or a [int] type."""

    @overload
    def __init__(
        self,
        *,
        simple_union: Union[str, List[int]],
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
