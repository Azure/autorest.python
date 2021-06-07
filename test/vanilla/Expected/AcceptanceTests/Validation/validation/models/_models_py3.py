# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ChildProduct(msrest.serialization.Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar const_property: Required. Constant string. Default value: "constant".
    :vartype const_property: str
    :param count: Count.
    :type count: int
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
        super(ChildProduct, self).__init__(**kwargs)
        self.count = count


class ConstantProduct(msrest.serialization.Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar const_property: Required. Constant string. Default value: "constant".
    :vartype const_property: str
    :ivar const_property2: Required. Constant string2. Default value: "constant2".
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
        super(ConstantProduct, self).__init__(**kwargs)


class Error(msrest.serialization.Model):
    """Error.

    :param code:
    :type code: int
    :param message:
    :type message: str
    :param fields:
    :type fields: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "int"},
        "message": {"key": "message", "type": "str"},
        "fields": {"key": "fields", "type": "str"},
    }

    def __init__(
        self, *, code: Optional[int] = None, message: Optional[str] = None, fields: Optional[str] = None, **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.fields = fields


class Product(msrest.serialization.Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param display_names: Non required array of unique items from 0 to 6 elements.
    :type display_names: list[str]
    :param capacity: Non required int betwen 0 and 100 exclusive.
    :type capacity: int
    :param image: Image URL representing the product.
    :type image: str
    :param child: Required. The product documentation.
    :type child: ~validation.models.ChildProduct
    :param const_child: Required. The product documentation.
    :type const_child: ~validation.models.ConstantProduct
    :ivar const_int: Required. Constant int. Default value: "0".
    :vartype const_int: int
    :ivar const_string: Required. Constant string. Default value: "constant".
    :vartype const_string: str
    :param const_string_as_enum: Constant string as Enum.
    :type const_string_as_enum: str
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
        child: "ChildProduct",
        const_child: "ConstantProduct",
        display_names: Optional[List[str]] = None,
        capacity: Optional[int] = None,
        image: Optional[str] = None,
        const_string_as_enum: Optional[str] = None,
        **kwargs
    ):
        super(Product, self).__init__(**kwargs)
        self.display_names = display_names
        self.capacity = capacity
        self.image = image
        self.child = child
        self.const_child = const_child
        self.const_string_as_enum = const_string_as_enum
