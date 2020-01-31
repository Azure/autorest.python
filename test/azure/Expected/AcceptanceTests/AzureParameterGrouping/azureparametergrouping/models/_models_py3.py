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

    def __init__(
        self,
        *,
        status: Optional[int] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class FirstParameterGroup(Model):
    """Parameter group.

    :param header_one:
    :type header_one: str
    :param query_one: Query parameter with default.
    :type query_one: int
    """

    _attribute_map = {
        'header_one': {'key': 'header-one', 'type': 'str'},
        'query_one': {'key': 'query-one', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        header_one: Optional[str] = None,
        query_one: Optional[int] = 30,
        **kwargs
    ):
        super(FirstParameterGroup, self).__init__(**kwargs)
        self.header_one = header_one
        self.query_one = query_one


class ParameterGroupingPostMultiParamGroupsSecondParamGroup(Model):
    """Parameter group.

    :param header_two:
    :type header_two: str
    :param query_two: Query parameter with default.
    :type query_two: int
    """

    _attribute_map = {
        'header_two': {'key': 'header-two', 'type': 'str'},
        'query_two': {'key': 'query-two', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        header_two: Optional[str] = None,
        query_two: Optional[int] = 30,
        **kwargs
    ):
        super(ParameterGroupingPostMultiParamGroupsSecondParamGroup, self).__init__(**kwargs)
        self.header_two = header_two
        self.query_two = query_two


class ParameterGroupingPostOptionalParameters(Model):
    """Parameter group.

    :param custom_header:
    :type custom_header: str
    :param query: Query parameter with default.
    :type query: int
    """

    _attribute_map = {
        'custom_header': {'key': 'customHeader', 'type': 'str'},
        'query': {'key': 'query', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        custom_header: Optional[str] = None,
        query: Optional[int] = 30,
        **kwargs
    ):
        super(ParameterGroupingPostOptionalParameters, self).__init__(**kwargs)
        self.custom_header = custom_header
        self.query = query


class ParameterGroupingPostRequiredParameters(Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :param custom_header:
    :type custom_header: str
    :param query: Query parameter with default.
    :type query: int
    :param path: Required. Path parameter.
    :type path: str
    :param body: Required.
    :type body: int
    """

    _validation = {
        'path': {'required': True},
        'body': {'required': True},
    }

    _attribute_map = {
        'custom_header': {'key': 'customHeader', 'type': 'str'},
        'query': {'key': 'query', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
        'body': {'key': 'body', 'type': 'int'},
    }

    def __init__(
        self,
        path: str,
        body: int,
        *,
        custom_header: Optional[str] = None,
        query: Optional[int] = 30,
        **kwargs
    ):
        super(ParameterGroupingPostRequiredParameters, self).__init__(**kwargs)
        self.custom_header = custom_header
        self.query = query
        self.path = path
        self.body = body
