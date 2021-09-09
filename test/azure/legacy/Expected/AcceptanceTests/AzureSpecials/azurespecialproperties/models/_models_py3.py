# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
    """Error.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar status:
    :vartype status: int
    :ivar constant_id:  Has constant value: 1.
    :vartype constant_id: int
    :ivar message:
    :vartype message: str
    """

    _validation = {
        "constant_id": {"required": True, "constant": True},
    }

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "constant_id": {"key": "constantId", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    constant_id = 1

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class HeaderCustomNamedRequestIdParamGroupingParameters(msrest.serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :ivar foo_client_request_id: Required. The fooRequestId.
    :vartype foo_client_request_id: str
    """

    _validation = {
        "foo_client_request_id": {"required": True},
    }

    _attribute_map = {
        "foo_client_request_id": {"key": "foo-client-request-id", "type": "str"},
    }

    def __init__(self, *, foo_client_request_id: str, **kwargs):
        """
        :keyword foo_client_request_id: Required. The fooRequestId.
        :paramtype foo_client_request_id: str
        """
        super(HeaderCustomNamedRequestIdParamGroupingParameters, self).__init__(**kwargs)
        self.foo_client_request_id = foo_client_request_id


class OdataFilter(msrest.serialization.Model):
    """OdataFilter.

    :ivar id:
    :vartype id: int
    :ivar name:
    :vartype name: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, *, id: Optional[int] = None, name: Optional[str] = None, **kwargs):
        """
        :keyword id:
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super(OdataFilter, self).__init__(**kwargs)
        self.id = id
        self.name = name
