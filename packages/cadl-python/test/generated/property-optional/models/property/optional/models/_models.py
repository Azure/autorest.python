# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
import sys
from typing import Any, List, Mapping, Optional, overload

from .. import _model_base
from .._model_base import rest_field

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class BytesProperty(_model_base.Model):
    """Template type for testing models with optional property. Pass in the type of the property you
    are looking for.

    :ivar property: Property.
    :vartype property: bytes
    """

    property: Optional[bytes] = rest_field()
    """Property. """

    @overload
    def __init__(
        self,
        *,
        property: Optional[bytes] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CollectionsByteProperty(_model_base.Model):
    """Model with collection bytes properties.

    :ivar property: Property.
    :vartype property: list[bytes]
    """

    property: Optional[List[bytes]] = rest_field()
    """Property. """

    @overload
    def __init__(
        self,
        *,
        property: Optional[List[bytes]] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CollectionsModelProperty(_model_base.Model):
    """Model with collection models properties.

    :ivar property: Property.
    :vartype property: list[~models.property.optional.models.StringProperty]
    """

    property: Optional[List["_models.StringProperty"]] = rest_field()
    """Property. """

    @overload
    def __init__(
        self,
        *,
        property: Optional[List["_models.StringProperty"]] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DatetimeProperty(_model_base.Model):
    """Model with a datetime property.

    :ivar property: Property.
    :vartype property: ~datetime.datetime
    """

    property: Optional[datetime.datetime] = rest_field()
    """Property. """

    @overload
    def __init__(
        self,
        *,
        property: Optional[datetime.datetime] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DurationProperty(_model_base.Model):
    """Model with a duration property.

    :ivar property: Property.
    :vartype property: ~datetime.timedelta
    """

    property: Optional[datetime.timedelta] = rest_field()
    """Property. """

    @overload
    def __init__(
        self,
        *,
        property: Optional[datetime.timedelta] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
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
    """optional string property. """
    required_property: int = rest_field(name="requiredProperty")
    """required int property. Required. """

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
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StringProperty(_model_base.Model):
    """Template type for testing models with optional property. Pass in the type of the property you
    are looking for.

    :ivar property: Property.
    :vartype property: str
    """

    property: Optional[str] = rest_field()
    """Property. """

    @overload
    def __init__(
        self,
        *,
        property: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
