# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, TYPE_CHECKING

import msrest.serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from . import Product, ProductProperties
    import __init__ as _models


class Error(msrest.serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class Product(msrest.serialization.Model):
    """Product.

    :ivar properties:
    :vartype properties: ~custombaseurlpaging.models.ProductProperties
    """

    _attribute_map = {
        "properties": {"key": "properties", "type": "ProductProperties"},
    }

    def __init__(self, *, properties: Optional["_models.ProductProperties"] = None, **kwargs):
        """
        :keyword properties:
        :paramtype properties: ~custombaseurlpaging.models.ProductProperties
        """
        super(Product, self).__init__(**kwargs)
        self.properties = properties


class ProductProperties(msrest.serialization.Model):
    """ProductProperties.

    :ivar id:
    :vartype id: int
    :ivar name:
    :vartype name: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, *, id: Optional[int] = None, name: Optional[str] = None, **kwargs):
        """
        :keyword id:
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super(ProductProperties, self).__init__(**kwargs)
        self.id = id
        self.name = name


class ProductResult(msrest.serialization.Model):
    """ProductResult.

    :ivar values:
    :vartype values: list[~custombaseurlpaging.models.Product]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        "values": {"key": "values", "type": "[Product]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, values: Optional[List["_models.Product"]] = None, next_link: Optional[str] = None, **kwargs):
        """
        :keyword values:
        :paramtype values: list[~custombaseurlpaging.models.Product]
        :keyword next_link:
        :paramtype next_link: str
        """
        super(ProductResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link
