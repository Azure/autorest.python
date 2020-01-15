# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List

from msrest.serialization import Model

class Error(Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, status: int=None, message: str=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message

class Product(Model):
    """Product.

    :param properties:
    :type properties: ~custombaseurlpaging.models.ProductProperties
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'ProductProperties'},
    }

    def __init__(self, *, properties: "ProductProperties"=None, **kwargs) -> None:
        super(Product, self).__init__(**kwargs)
        self.properties = properties

class ProductProperties(Model):
    """ProductProperties.

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, name: str=None, **kwargs) -> None:
        super(ProductProperties, self).__init__(**kwargs)
        self.id = id
        self.name = name

class ProductResult(Model):
    """ProductResult.

    :param values:
    :type values: list[~custombaseurlpaging.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, *, values: List["Product"]=None, next_link: str=None, **kwargs) -> None:
        super(ProductResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link

