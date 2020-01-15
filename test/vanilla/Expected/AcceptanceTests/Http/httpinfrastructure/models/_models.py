# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
from msrest.serialization import Model

class MyExceptionException(HttpResponseError):
    """Server responded with exception of type: 'MyException'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(MyExceptionException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'MyException'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class MyException(Model):
    """MyException.

    :param status_code:
    :type status_code: str
    """
    _EXCEPTION_TYPE = MyExceptionException

    _attribute_map = {
        'status_code': {'key': 'statusCode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MyException, self).__init__(**kwargs)
        self.status_code = kwargs.get('status_code', None)

class BException(MyExceptionException):
    """Server responded with exception of type: 'B'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(BException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'B'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class B(MyException):
    """B.

    :param status_code:
    :type status_code: str
    :param text_status_code:
    :type text_status_code: str
    """
    _EXCEPTION_TYPE = BException

    _attribute_map = {
        'status_code': {'key': 'statusCode', 'type': 'str'},
        'text_status_code': {'key': 'textStatusCode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(B, self).__init__(**kwargs)
        self.text_status_code = kwargs.get('text_status_code', None)

class C(Model):
    """C.

    :param http_code:
    :type http_code: str
    """

    _attribute_map = {
        'http_code': {'key': 'httpCode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(C, self).__init__(**kwargs)
        self.http_code = kwargs.get('http_code', None)

class D(Model):
    """D.

    :param http_status_code:
    :type http_status_code: str
    """

    _attribute_map = {
        'http_status_code': {'key': 'httpStatusCode', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(D, self).__init__(**kwargs)
        self.http_status_code = kwargs.get('http_status_code', None)

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

    :param status:
    :type status: int
    :param message:
    :type message: str
    """
    _EXCEPTION_TYPE = ErrorException

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)

