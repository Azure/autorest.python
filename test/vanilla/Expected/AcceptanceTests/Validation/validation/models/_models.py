# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

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
        'const_property': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'const_property': {'key': 'constProperty', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
    }

    const_property = "constant"

    def __init__(
        self,
        **kwargs
    ):
        super(ChildProduct, self).__init__(**kwargs)
        self.count = kwargs.get('count', None)


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
        'const_property': {'required': True, 'constant': True},
        'const_property2': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'const_property': {'key': 'constProperty', 'type': 'str'},
        'const_property2': {'key': 'constProperty2', 'type': 'str'},
    }

    const_property = "constant"
    const_property2 = "constant2"

    def __init__(
        self,
        **kwargs
    ):
        super(ConstantProduct, self).__init__(**kwargs)


class Error(msrest.serialization.Model):
    """Error.

    :param code:
    :type code: int
    :param fields:
    :type fields: str
    :param message:
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'fields': {'key': 'fields', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.fields = kwargs.get('fields', None)
        self.message = kwargs.get('message', None)


class Product(msrest.serialization.Model):
    """The product documentation.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param capacity: Non required int betwen 0 and 100 exclusive.
    :type capacity: int
    :param child: Required. The product documentation.
    :type child: ~validation.models.ChildProduct
    :param const_child: Required. The product documentation.
    :type const_child: ~validation.models.ConstantProduct
    :ivar const_int: Required. Constant int. Default value: "0".
    :vartype const_int: int
    :ivar const_string: Required. Constant string. Default value: "constant".
    :vartype const_string: str
    :ivar const_string_as_enum: Constant string as Enum. Default value: "constant_string_as_enum".
    :vartype const_string_as_enum: str
    :param display_names: Non required array of unique items from 0 to 6 elements.
    :type display_names: list[str]
    :param image: Image URL representing the product.
    :type image: str
    """

    _validation = {
        'capacity': {'maximum_ex': 100, 'minimum_ex': 0},
        'child': {'required': True},
        'const_child': {'required': True},
        'const_int': {'required': True, 'constant': True},
        'const_string': {'required': True, 'constant': True},
        'const_string_as_enum': {'constant': True},
        'display_names': {'max_items': 6, 'min_items': 0, 'unique': True},
        'image': {'pattern': r'http://\w+'},
    }

    _attribute_map = {
        'capacity': {'key': 'capacity', 'type': 'int'},
        'child': {'key': 'child', 'type': 'ChildProduct'},
        'const_child': {'key': 'constChild', 'type': 'ConstantProduct'},
        'const_int': {'key': 'constInt', 'type': 'int'},
        'const_string': {'key': 'constString', 'type': 'str'},
        'const_string_as_enum': {'key': 'constStringAsEnum', 'type': 'str'},
        'display_names': {'key': 'display_names', 'type': '[str]'},
        'image': {'key': 'image', 'type': 'str'},
    }

    const_int = 0
    const_string = "constant"
    const_string_as_enum = "constant_string_as_enum"

    def __init__(
        self,
        **kwargs
    ):
        super(Product, self).__init__(**kwargs)
        self.capacity = kwargs.get('capacity', None)
        self.child = kwargs['child']
        self.const_child = kwargs['const_child']
        self.display_names = kwargs.get('display_names', None)
        self.image = kwargs.get('image', None)
