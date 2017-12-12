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

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param status:
    :type status: int
    :ivar constant_id:  Default value: 1 .
    :vartype constant_id: int
    :param message:
    :type message: str
    """

    _validation = {
        'constant_id': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'constant_id': {'key': 'constantId', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    constant_id = 1

    def __init__(self, status=None, message=None):
        super(Model, self).__init__()
        self.status = status
        self.message = message


class ErrorException(HttpOperationError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)
