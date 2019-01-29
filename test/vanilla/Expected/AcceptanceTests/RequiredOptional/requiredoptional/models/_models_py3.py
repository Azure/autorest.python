# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


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


class ErrorException(HttpOperationError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)
from msrest.serialization import Model


class IntWrapper(Model):
    """IntWrapper.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: int
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'int'},
    }

    def __init__(self, *, value: int, **kwargs) -> None:
        super(IntWrapper, self).__init__(**kwargs)
        self.value = value
from msrest.serialization import Model


class IntOptionalWrapper(Model):
    """IntOptionalWrapper.

    :param value:
    :type value: int
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'int'},
    }

    def __init__(self, *, value: int=None, **kwargs) -> None:
        super(IntOptionalWrapper, self).__init__(**kwargs)
        self.value = value
from msrest.serialization import Model


class StringWrapper(Model):
    """StringWrapper.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: str
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, value: str, **kwargs) -> None:
        super(StringWrapper, self).__init__(**kwargs)
        self.value = value
from msrest.serialization import Model


class StringOptionalWrapper(Model):
    """StringOptionalWrapper.

    :param value:
    :type value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, *, value: str=None, **kwargs) -> None:
        super(StringOptionalWrapper, self).__init__(**kwargs)
        self.value = value
from msrest.serialization import Model


class ArrayWrapper(Model):
    """ArrayWrapper.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: list[str]
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(self, *, value, **kwargs) -> None:
        super(ArrayWrapper, self).__init__(**kwargs)
        self.value = value
from msrest.serialization import Model


class ArrayOptionalWrapper(Model):
    """ArrayOptionalWrapper.

    :param value:
    :type value: list[str]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(ArrayOptionalWrapper, self).__init__(**kwargs)
        self.value = value
from msrest.serialization import Model


class Product(Model):
    """Product.

    All required parameters must be populated in order to send to Azure.

    :param id: Required.
    :type id: int
    :param name:
    :type name: str
    """

    _validation = {
        'id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, id: int, name: str=None, **kwargs) -> None:
        super(Product, self).__init__(**kwargs)
        self.id = id
        self.name = name
from msrest.serialization import Model


class ClassWrapper(Model):
    """ClassWrapper.

    All required parameters must be populated in order to send to Azure.

    :param value: Required.
    :type value: ~requiredoptional.models.Product
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'Product'},
    }

    def __init__(self, *, value, **kwargs) -> None:
        super(ClassWrapper, self).__init__(**kwargs)
        self.value = value
from msrest.serialization import Model


class ClassOptionalWrapper(Model):
    """ClassOptionalWrapper.

    :param value:
    :type value: ~requiredoptional.models.Product
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'Product'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(ClassOptionalWrapper, self).__init__(**kwargs)
        self.value = value
