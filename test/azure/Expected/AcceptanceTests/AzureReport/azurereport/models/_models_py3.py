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
from azure.core.exceptions import ClientRequestError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


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


class ErrorException(ClientRequestError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

        model_name = 'Error'
        self.error = deserialize(model_name, response)
        if self.error is None:
            self.error = deserialize.dependencies[model_name]()
        super(ErrorException, self).__init__(response)
