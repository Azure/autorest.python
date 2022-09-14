# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class OutputModel(_model_base.Model):
    """Output model with readonly properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar required_readonly_string: Required string, illustrating a readonly reference type
     property. Required.
    :vartype required_readonly_string: str
    :ivar required_readonly_int: Required int, illustrating a readonly value type property.
     Required.
    :vartype required_readonly_int: int
    :ivar optional_readonly_string: Optional string, illustrating a readonly reference type
     property.
    :vartype optional_readonly_string: str
    :ivar optional_readonly_int: Optional int, illustrating a readonly value type property.
    :vartype optional_readonly_int: int
    :ivar required_readonly_model: Required readonly model. Required.
    :vartype required_readonly_model: ~readonlyproperties.models.ReadonlyModel
    :ivar optional_readonly_model: Optional readonly model.
    :vartype optional_readonly_model: ~readonlyproperties.models.ReadonlyModel
    :ivar required_readonly_string_list: Required readonly string collection. Required.
    :vartype required_readonly_string_list: list[str]
    :ivar required_readonly_int_list: Required readonly int collection. Required.
    :vartype required_readonly_int_list: list[int]
    :ivar optional_readonly_string_list: Optional readonly string collection.
    :vartype optional_readonly_string_list: list[str]
    :ivar optional_readonly_int_list: Optional readonly int collection.
    :vartype optional_readonly_int_list: list[int]
    """

    required_readonly_string: str = rest_field(name="requiredReadonlyString", readonly=True)
    """Required string, illustrating a readonly reference type property. Required. """
    required_readonly_int: int = rest_field(name="requiredReadonlyInt", readonly=True)
    """Required int, illustrating a readonly value type property. Required. """
    optional_readonly_string: Optional[str] = rest_field(name="optionalReadonlyString", readonly=True)
    """Optional string, illustrating a readonly reference type property. """
    optional_readonly_int: Optional[int] = rest_field(name="optionalReadonlyInt", readonly=True)
    """Optional int, illustrating a readonly value type property. """
    required_readonly_model: "ReadonlyModel" = rest_field(name="requiredReadonlyModel", readonly=True)
    """Required readonly model. Required. """
    optional_readonly_model: Optional["ReadonlyModel"] = rest_field(name="optionalReadonlyModel", readonly=True)
    """Optional readonly model. """
    required_readonly_string_list: List[str] = rest_field(name="requiredReadonlyStringList", readonly=True)
    """Required readonly string collection. Required. """
    required_readonly_int_list: List[int] = rest_field(name="requiredReadonlyIntList", readonly=True)
    """Required readonly int collection. Required. """
    optional_readonly_string_list: Optional[List[str]] = rest_field(name="optionalReadonlyStringList", readonly=True)
    """Optional readonly string collection. """
    optional_readonly_int_list: Optional[List[int]] = rest_field(name="optionalReadonlyIntList", readonly=True)
    """Optional readonly int collection. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ReadonlyModel(_model_base.Model):
    """Readonly model.

    All required parameters must be populated in order to send to Azure.

    :ivar required_string: Required string. Required.
    :vartype required_string: str
    """

    required_string: str = rest_field(name="requiredString")
    """Required string. Required. """

    @overload
    def __init__(
        self,
        *,
        required_string: str,
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


class RoundTripModel(_model_base.Model):
    """Round-trip model with readonly properties.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar required_readonly_string: Required string, illustrating a readonly reference type
     property. Required.
    :vartype required_readonly_string: str
    :ivar required_readonly_int: Required int, illustrating a readonly value type property.
     Required.
    :vartype required_readonly_int: int
    :ivar optional_readonly_string: Optional string, illustrating a readonly reference type
     property.
    :vartype optional_readonly_string: str
    :ivar optional_readonly_int: Optional int, illustrating a readonly value type property.
    :vartype optional_readonly_int: int
    :ivar required_readonly_model: Required readonly model. Required.
    :vartype required_readonly_model: ~readonlyproperties.models.ReadonlyModel
    :ivar optional_readonly_model: Optional readonly model.
    :vartype optional_readonly_model: ~readonlyproperties.models.ReadonlyModel
    :ivar required_readonly_string_list: Required readonly string collection. Required.
    :vartype required_readonly_string_list: list[str]
    :ivar required_readonly_int_list: Required readonly int collection. Required.
    :vartype required_readonly_int_list: list[int]
    :ivar optional_readonly_string_list: Optional readonly string collection.
    :vartype optional_readonly_string_list: list[str]
    :ivar optional_readonly_int_list: Optional readonly int collection.
    :vartype optional_readonly_int_list: list[int]
    """

    required_readonly_string: str = rest_field(name="requiredReadonlyString", readonly=True)
    """Required string, illustrating a readonly reference type property. Required. """
    required_readonly_int: int = rest_field(name="requiredReadonlyInt", readonly=True)
    """Required int, illustrating a readonly value type property. Required. """
    optional_readonly_string: Optional[str] = rest_field(name="optionalReadonlyString", readonly=True)
    """Optional string, illustrating a readonly reference type property. """
    optional_readonly_int: Optional[int] = rest_field(name="optionalReadonlyInt", readonly=True)
    """Optional int, illustrating a readonly value type property. """
    required_readonly_model: "ReadonlyModel" = rest_field(name="requiredReadonlyModel", readonly=True)
    """Required readonly model. Required. """
    optional_readonly_model: Optional["ReadonlyModel"] = rest_field(name="optionalReadonlyModel", readonly=True)
    """Optional readonly model. """
    required_readonly_string_list: List[str] = rest_field(name="requiredReadonlyStringList", readonly=True)
    """Required readonly string collection. Required. """
    required_readonly_int_list: List[int] = rest_field(name="requiredReadonlyIntList", readonly=True)
    """Required readonly int collection. Required. """
    optional_readonly_string_list: Optional[List[str]] = rest_field(name="optionalReadonlyStringList", readonly=True)
    """Optional readonly string collection. """
    optional_readonly_int_list: Optional[List[int]] = rest_field(name="optionalReadonlyIntList", readonly=True)
    """Optional readonly int collection. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
