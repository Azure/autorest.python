# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Literal, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class BooleanLiteralProperty(_model_base.Model):
    """Model with boolean literal property.

    :ivar property: Property. Default value is True.
    :vartype property: bool
    """

    property: Optional[Literal[True]] = rest_field()
    """Property. Default value is True."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[Literal[True]] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class BytesProperty(_model_base.Model):
    """Template type for testing models with optional property. Pass in the type of the property you
    are looking for.

    :ivar property: Property.
    :vartype property: bytes
    """

    property: Optional[bytes] = rest_field(format="base64")
    """Property."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[bytes] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsByteProperty(_model_base.Model):
    """Model with collection bytes properties.

    :ivar property: Property.
    :vartype property: list[bytes]
    """

    property: Optional[List[bytes]] = rest_field(format="base64")
    """Property."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[List[bytes]] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsModelProperty(_model_base.Model):
    """Model with collection models properties.

    :ivar property: Property.
    :vartype property: list[~typetest.property.optional.models.StringProperty]
    """

    property: Optional[List["_models.StringProperty"]] = rest_field()
    """Property."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[List["_models.StringProperty"]] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DatetimeProperty(_model_base.Model):
    """Model with a datetime property.

    :ivar property: Property.
    :vartype property: ~datetime.datetime
    """

    property: Optional[datetime.datetime] = rest_field(format="rfc3339")
    """Property."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[datetime.datetime] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DurationProperty(_model_base.Model):
    """Model with a duration property.

    :ivar property: Property.
    :vartype property: ~datetime.timedelta
    """

    property: Optional[datetime.timedelta] = rest_field()
    """Property."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[datetime.timedelta] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FloatLiteralProperty(_model_base.Model):
    """Model with float literal property.

    :ivar property: Property. Default value is 1.25.
    :vartype property: float
    """

    property: Optional[float] = rest_field()
    """Property. Default value is 1.25."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[float] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class IntLiteralProperty(_model_base.Model):
    """Model with int literal property.

    :ivar property: Property. Default value is 1.
    :vartype property: int
    """

    property: Optional[Literal[1]] = rest_field()
    """Property. Default value is 1."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[Literal[1]] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class PlainDateProperty(_model_base.Model):
    """Model with a plainDate property.

    :ivar property: Property.
    :vartype property: ~datetime.date
    """

    property: Optional[datetime.date] = rest_field()
    """Property."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[datetime.date] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class PlainTimeProperty(_model_base.Model):
    """Model with a plainTime property.

    :ivar property: Property.
    :vartype property: ~datetime.time
    """

    property: Optional[datetime.time] = rest_field()
    """Property."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[datetime.time] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class RequiredAndOptionalProperty(_model_base.Model):
    """Model with required and optional properties.


    :ivar optional_property: optional string property.
    :vartype optional_property: str
    :ivar required_property: required int property. Required.
    :vartype required_property: int
    """

    optional_property: Optional[str] = rest_field(name="optionalProperty")
    """optional string property."""
    required_property: int = rest_field(name="requiredProperty")
    """required int property. Required."""

    @overload
    def __init__(
        self,
        *,
        required_property: int,
        optional_property: Optional[str] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class StringLiteralProperty(_model_base.Model):
    """Model with string literal property.

    :ivar property: Property. Default value is "hello".
    :vartype property: str
    """

    property: Optional[Literal["hello"]] = rest_field()
    """Property. Default value is \"hello\"."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[Literal["hello"]] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class StringProperty(_model_base.Model):
    """Template type for testing models with optional property. Pass in the type of the property you
    are looking for.

    :ivar property: Property.
    :vartype property: str
    """

    property: Optional[str] = rest_field()
    """Property."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[str] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnionFloatLiteralProperty(_model_base.Model):
    """Model with union of float literal property.

    :ivar property: Property. Is either a float type or a float type.
    :vartype property: float or float
    """

    property: Optional[float] = rest_field()
    """Property. Is either a float type or a float type."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[float] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnionIntLiteralProperty(_model_base.Model):
    """Model with union of int literal property.

    :ivar property: Property. Is either a Literal[1] type or a Literal[2] type.
    :vartype property: int or int
    """

    property: Optional[Literal[1, 2]] = rest_field()
    """Property. Is either a Literal[1] type or a Literal[2] type."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[Literal[1, 2]] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UnionStringLiteralProperty(_model_base.Model):
    """Model with union of string literal property.

    :ivar property: Property. Is either a Literal["hello"] type or a Literal["world"] type.
    :vartype property: str or str
    """

    property: Optional[Literal["hello", "world"]] = rest_field()
    """Property. Is either a Literal[\"hello\"] type or a Literal[\"world\"] type."""

    @overload
    def __init__(
        self,
        *,
        property: Optional[Literal["hello", "world"]] = None,  # pylint: disable=redefined-builtin
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
