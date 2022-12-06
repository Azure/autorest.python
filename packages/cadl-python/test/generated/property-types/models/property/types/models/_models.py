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
from typing import Any, Dict, List, Mapping, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class BooleanProperty(_model_base.Model):
    """Model with a boolean property.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: bool
    """

    property: bool = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: bool,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class BytesProperty(_model_base.Model):
    """Model with a bytes property.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: bytes
    """

    property: bytes = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: bytes,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsIntProperty(_model_base.Model):
    """Model with collection int properties.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: list[int]
    """

    property: List[int] = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: List[int],  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsModelProperty(_model_base.Model):
    """Model with collection model properties.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: list[~models.property.types.models.InnerModel]
    """

    property: List["_models.InnerModel"] = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: List["_models.InnerModel"],  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CollectionsStringProperty(_model_base.Model):
    """Model with collection string properties.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: list[str]
    """

    property: List[str] = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: List[str],  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DatetimeProperty(_model_base.Model):
    """Model with a datetime property.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: ~datetime.datetime
    """

    property: datetime.datetime = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: datetime.datetime,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DictionaryStringProperty(_model_base.Model):
    """Model with dictionary string properties.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: dict[str, str]
    """

    property: Dict[str, str] = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: Dict[str, str],  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DurationProperty(_model_base.Model):
    """Model with a duration property.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: ~datetime.timedelta
    """

    property: datetime.timedelta = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: datetime.timedelta,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class EnumProperty(_model_base.Model):
    """Model with enum properties.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required. Known values are: "ValueOne" and "ValueTwo".
    :vartype property: str or ~models.property.types.models.InnerEnum
    """

    property: Union[str, "_models.InnerEnum"] = rest_field()
    """Property. Required. Known values are: \"ValueOne\" and \"ValueTwo\"."""

    @overload
    def __init__(
        self,
        *,
        property: Union[str, "_models.InnerEnum"],  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ExtensibleEnumProperty(_model_base.Model):
    """Model with extensible enum properties.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required. Known values are: "ValueOne" and "ValueTwo".
    :vartype property: str or ~models.property.types.models.InnerExtensibleEnum
    """

    property: Union[str, "_models.InnerExtensibleEnum"] = rest_field()
    """Property. Required. Known values are: \"ValueOne\" and \"ValueTwo\"."""

    @overload
    def __init__(
        self,
        *,
        property: Union[str, "_models.InnerExtensibleEnum"],  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class FloatProperty(_model_base.Model):
    """Model with a float property.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: float
    """

    property: float = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: float,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class InnerModel(_model_base.Model):
    """Inner model. Will be a property type for ModelWithModelProperties.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Required string property. Required.
    :vartype property: str
    """

    property: str = rest_field()
    """Required string property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class IntProperty(_model_base.Model):
    """Model with a int property.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: int
    """

    property: int = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: int,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ModelProperty(_model_base.Model):
    """Model with model properties.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: ~models.property.types.models.InnerModel
    """

    property: "_models.InnerModel" = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: "_models.InnerModel",  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class NeverProperty(_model_base.Model):
    """Model with a property never. (This property should not be included)."""

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class StringProperty(_model_base.Model):
    """Model with a string property.

    All required parameters must be populated in order to send to Azure.

    :ivar property: Property. Required.
    :vartype property: str
    """

    property: str = rest_field()
    """Property. Required. """

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
