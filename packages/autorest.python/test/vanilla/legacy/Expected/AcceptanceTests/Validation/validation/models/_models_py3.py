# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import List, Optional, TYPE_CHECKING

import msrest.serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports


class ChildProduct(msrest.serialization.Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar const_property: Constant string. Required. Default value is "constant".
    :vartype const_property: str
    :ivar count: Count.
    :vartype count: int
    """

    _validation = {
        "const_property": {"required": True, "constant": True},
    }

    _attribute_map = {
        "const_property": {"key": "constProperty", "type": "str"},
        "count": {"key": "count", "type": "int"},
    }

    const_property = "constant"

    def __init__(self, *, count: Optional[int] = None, **kwargs):
        """
        :keyword count: Count.
        :paramtype count: int
        """
        super().__init__(**kwargs)
        self.count = count


class ConstantProduct(msrest.serialization.Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar const_property: Constant string. Required. Default value is "constant".
    :vartype const_property: str
    :ivar const_property2: Constant string2. Required. Default value is "constant2".
    :vartype const_property2: str
    """

    _validation = {
        "const_property": {"required": True, "constant": True},
        "const_property2": {"required": True, "constant": True},
    }

    _attribute_map = {
        "const_property": {"key": "constProperty", "type": "str"},
        "const_property2": {"key": "constProperty2", "type": "str"},
    }

    const_property = "constant"
    const_property2 = "constant2"

    def __init__(self, **kwargs):
        """ """
        super().__init__(**kwargs)


class Error(msrest.serialization.Model):
    """Error.

    :ivar code:
    :vartype code: int
    :ivar message:
    :vartype message: str
    :ivar fields:
    :vartype fields: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "int"},
        "message": {"key": "message", "type": "str"},
        "fields": {"key": "fields", "type": "str"},
    }

    def __init__(
        self, *, code: Optional[int] = None, message: Optional[str] = None, fields: Optional[str] = None, **kwargs
    ):
        """
        :keyword code:
        :paramtype code: int
        :keyword message:
        :paramtype message: str
        :keyword fields:
        :paramtype fields: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
        self.fields = fields


class Product(msrest.serialization.Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar display_names: Non required array of unique items from 0 to 6 elements.
    :vartype display_names: list[str]
    :ivar capacity: Non required int betwen 0 and 100 exclusive.
    :vartype capacity: int
    :ivar image: Image URL representing the product.
    :vartype image: str
    :ivar child: The product documentation. Required.
    :vartype child: ~validation.models.ChildProduct
    :ivar const_child: The product documentation. Required.
    :vartype const_child: ~validation.models.ConstantProduct
    :ivar const_int: Constant int. Required. Default value is 0.
    :vartype const_int: int
    :ivar const_string: Constant string. Required. Default value is "constant".
    :vartype const_string: str
    :ivar const_string_as_enum: Constant string as Enum. Default value is
     "constant_string_as_enum".
    :vartype const_string_as_enum: str
    """

    _validation = {
        "display_names": {"max_items": 6, "min_items": 0, "unique": True},
        "capacity": {"maximum_ex": 100, "minimum_ex": 0},
        "image": {"pattern": r"http://\w+"},
        "child": {"required": True},
        "const_child": {"required": True},
        "const_int": {"required": True, "constant": True},
        "const_string": {"required": True, "constant": True},
    }

    _attribute_map = {
        "display_names": {"key": "display_names", "type": "[str]"},
        "capacity": {"key": "capacity", "type": "int"},
        "image": {"key": "image", "type": "str"},
        "child": {"key": "child", "type": "ChildProduct"},
        "const_child": {"key": "constChild", "type": "ConstantProduct"},
        "const_int": {"key": "constInt", "type": "int"},
        "const_string": {"key": "constString", "type": "str"},
        "const_string_as_enum": {"key": "constStringAsEnum", "type": "str"},
    }

    const_int = 0
    const_string = "constant"

    def __init__(
        self,
        *,
        child: "_models.ChildProduct",
        const_child: "_models.ConstantProduct",
        display_names: Optional[List[str]] = None,
        capacity: Optional[int] = None,
        image: Optional[str] = None,
        const_string_as_enum: Optional[Literal["constant_string_as_enum"]] = None,
        **kwargs
    ):
        """
        :keyword display_names: Non required array of unique items from 0 to 6 elements.
        :paramtype display_names: list[str]
        :keyword capacity: Non required int betwen 0 and 100 exclusive.
        :paramtype capacity: int
        :keyword image: Image URL representing the product.
        :paramtype image: str
        :keyword child: The product documentation. Required.
        :paramtype child: ~validation.models.ChildProduct
        :keyword const_child: The product documentation. Required.
        :paramtype const_child: ~validation.models.ConstantProduct
        :keyword const_string_as_enum: Constant string as Enum. Default value is
         "constant_string_as_enum".
        :paramtype const_string_as_enum: str
        """
        super().__init__(**kwargs)
        self.display_names = display_names
        self.capacity = capacity
        self.image = image
        self.child = child
        self.const_child = const_child
        self.const_string_as_enum = const_string_as_enum
