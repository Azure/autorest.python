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

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)


class ErrorException(HttpOperationError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)
from msrest.serialization import Model


class RefColorConstant(Model):
    """RefColorConstant.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar color_constant: Required. Referenced Color Constant Description.
     Default value: "green-color" .
    :vartype color_constant: str
    :param field1: Sample string.
    :type field1: str
    """

    _validation = {
        'color_constant': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'color_constant': {'key': 'ColorConstant', 'type': 'str'},
        'field1': {'key': 'field1', 'type': 'str'},
    }

    color_constant = "green-color"

    def __init__(self, **kwargs):
        super(RefColorConstant, self).__init__(**kwargs)
        self.field1 = kwargs.get('field1', None)
