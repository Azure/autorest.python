# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
from msrest.serialization import Model


class ErrorException(HttpResponseError):
    """Server responded with exception of type: 'Error'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(ErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'Error'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class Error(Model):
    """

    :param code:
    :type code: int
    :param message:
    :type message: str
    """
    _EXCEPTION_TYPE = ErrorException

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class SampleResourceGroup(Model):
    """

    :param name: resource group name 'testgroup101'.
    :type name: str
    :param location: resource group location 'West US'.
    :type location: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SampleResourceGroup, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.location = kwargs.get('location', None)
