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
from azure.core import HttpResponseError


class Error(Model):
    """Error.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param status:
    :type status: int
    :ivar constant_id: Required.  Default value: 1 .
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

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)


class ErrorException(HttpResponseError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

      model_name = 'Error'
      self.error = deserialize(model_name, response)
      if self.error is None:
          self.error = deserialize.dependencies[model_name]()
      super(ErrorException, self).__init__(response=response)


class HeaderCustomNamedRequestIdParamGroupingParameters(Model):
    """Additional parameters for custom_named_request_id_param_grouping operation.

    All required parameters must be populated in order to send to Azure.

    :param foo_client_request_id: Required. The fooRequestId
    :type foo_client_request_id: str
    """

    _validation = {
        'foo_client_request_id': {'required': True},
    }

    _attribute_map = {
        'foo_client_request_id': {'key': '', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(HeaderCustomNamedRequestIdParamGroupingParameters, self).__init__(**kwargs)
        self.foo_client_request_id = kwargs.get('foo_client_request_id', None)


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

    def __init__(self, **kwargs):
        super(OdataFilter, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
