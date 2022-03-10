# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import (
    List as _List,
    Optional as _Optional,
)
from msrest.serialization import Model as _Model

class Input(_Model):
    """Input.

    All required parameters must be populated in order to send to Azure.

    :ivar hello: Required.
    :vartype hello: str
    """

    _validation = {
        "hello": {"required": True},
    }

    _attribute_map = {
        "hello": {"key": "hello", "type": "str"},
    }

    def __init__(self, *, hello: str, **kwargs):
        """
        :keyword hello: Required.
        :paramtype hello: str
        """
        super(Input, self).__init__(**kwargs)
        self.hello = hello


class Product(_Model):
    """Product.

    All required parameters must be populated in order to send to Azure.

    :ivar received: Required. Possible values include: "raw", "model".
    :vartype received: str or ~dpgcustomizationcustomizedversiontolerant.models.ProductReceived
    """

    _validation = {
        "received": {"required": True},
    }

    _attribute_map = {
        "received": {"key": "received", "type": "str"},
    }

    def __init__(self, *, received: str, **kwargs):
        """
        :keyword received: Required. Possible values include: "raw", "model".
        :paramtype received: str or ~dpgcustomizationcustomizedversiontolerant.models.ProductReceived
        """
        super(Product, self).__init__(**kwargs)
        self.received = received


class LROProduct(Product):
    """LROProduct.

    All required parameters must be populated in order to send to Azure.

    :ivar received: Required. Possible values include: "raw", "model".
    :vartype received: str or ~dpgcustomizationcustomizedversiontolerant.models.ProductReceived
    :ivar provisioning_state: Required.
    :vartype provisioning_state: str
    """

    _validation = {
        "received": {"required": True},
        "provisioning_state": {"required": True},
    }

    _attribute_map = {
        "received": {"key": "received", "type": "str"},
        "provisioning_state": {"key": "provisioningState", "type": "str"},
    }

    def __init__(self, *, received: str, provisioning_state: str, **kwargs):
        """
        :keyword received: Required. Possible values include: "raw", "model".
        :paramtype received: str or ~dpgcustomizationcustomizedversiontolerant.models.ProductReceived
        :keyword provisioning_state: Required.
        :paramtype provisioning_state: str
        """
        super(LROProduct, self).__init__(received=received, **kwargs)
        self.provisioning_state = provisioning_state


class ProductResult(_Model):
    """ProductResult.

    :ivar values:
    :vartype values: list[~dpgcustomizationcustomizedversiontolerant.models.Product]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        "values": {"key": "values", "type": "[Product]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, values: _Optional[_List["Product"]] = None, next_link: _Optional[str] = None, **kwargs):
        """
        :keyword values:
        :paramtype values: list[~dpgcustomizationcustomizedversiontolerant.models.Product]
        :keyword next_link:
        :paramtype next_link: str
        """
        super(ProductResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link
