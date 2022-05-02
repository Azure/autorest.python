# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


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

    def __init__(self, **kwargs):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get("status", None)
        self.message = kwargs.get("message", None)


class Product(msrest.serialization.Model):
    """Product.

    :ivar integer:
    :vartype integer: int
    :ivar string:
    :vartype string: str
    """

    _attribute_map = {
        "integer": {"key": "integer", "type": "int"},
        "string": {"key": "string", "type": "str"},
    }

    def __init__(self, **kwargs):
        """
        :keyword integer:
        :paramtype integer: int
        :keyword string:
        :paramtype string: str
        """
        super(Product, self).__init__(**kwargs)
        self.integer = kwargs.get("integer", None)
        self.string = kwargs.get("string", None)
