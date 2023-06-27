# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


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


class RequiredAndOptionalProperty(_model_base.Model):
    """Model with required and optional properties.

    All required parameters must be populated in order to send to Azure.

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
