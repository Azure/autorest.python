# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

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
    """Error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param status:
    :type status: int
    :ivar constant_id: Required.  Default value: "1".
    :vartype constant_id: float
    :param message:
    :type message: str
    """
    _EXCEPTION_TYPE = ErrorException

    _validation = {
        'constant_id': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'constant_id': {'key': 'constantId', 'type': 'float'},
        'message': {'key': 'message', 'type': 'str'},
    }

    constant_id = 1

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class OdataFilter(Model):
    """OdataFilter.

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, id: Optional[int] = None, name: Optional[str] = None, **kwargs) -> None:
        super(OdataFilter, self).__init__(**kwargs)
        self.id = id
        self.name = name
