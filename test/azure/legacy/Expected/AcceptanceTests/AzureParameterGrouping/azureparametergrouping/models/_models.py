# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
    """Error.

    :keyword status:
    :paramtype status: int
    :keyword message:
    :paramtype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get("status", None)
        self.message = kwargs.get("message", None)


class FirstParameterGroup(msrest.serialization.Model):
    """Parameter group.

    :keyword header_one:
    :paramtype header_one: str
    :keyword query_one: Query parameter with default.
    :paramtype query_one: int
    """

    _attribute_map = {
        "header_one": {"key": "header-one", "type": "str"},
        "query_one": {"key": "query-one", "type": "int"},
    }

    def __init__(self, **kwargs):
        super(FirstParameterGroup, self).__init__(**kwargs)
        self.header_one = kwargs.get("header_one", None)
        self.query_one = kwargs.get("query_one", 30)


class ParameterGroupingPostMultiParamGroupsSecondParamGroup(msrest.serialization.Model):
    """Parameter group.

    :keyword header_two:
    :paramtype header_two: str
    :keyword query_two: Query parameter with default.
    :paramtype query_two: int
    """

    _attribute_map = {
        "header_two": {"key": "header-two", "type": "str"},
        "query_two": {"key": "query-two", "type": "int"},
    }

    def __init__(self, **kwargs):
        super(ParameterGroupingPostMultiParamGroupsSecondParamGroup, self).__init__(**kwargs)
        self.header_two = kwargs.get("header_two", None)
        self.query_two = kwargs.get("query_two", 30)


class ParameterGroupingPostOptionalParameters(msrest.serialization.Model):
    """Parameter group.

    :keyword custom_header:
    :paramtype custom_header: str
    :keyword query: Query parameter with default.
    :paramtype query: int
    """

    _attribute_map = {
        "custom_header": {"key": "customHeader", "type": "str"},
        "query": {"key": "query", "type": "int"},
    }

    def __init__(self, **kwargs):
        super(ParameterGroupingPostOptionalParameters, self).__init__(**kwargs)
        self.custom_header = kwargs.get("custom_header", None)
        self.query = kwargs.get("query", 30)


class ParameterGroupingPostRequiredParameters(msrest.serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :keyword custom_header:
    :paramtype custom_header: str
    :keyword query: Query parameter with default.
    :paramtype query: int
    :keyword path: Required. Path parameter.
    :paramtype path: str
    :keyword body: Required.
    :paramtype body: int
    """

    _validation = {
        "path": {"required": True},
        "body": {"required": True},
    }

    _attribute_map = {
        "custom_header": {"key": "customHeader", "type": "str"},
        "query": {"key": "query", "type": "int"},
        "path": {"key": "path", "type": "str"},
        "body": {"key": "body", "type": "int"},
    }

    def __init__(self, **kwargs):
        super(ParameterGroupingPostRequiredParameters, self).__init__(**kwargs)
        self.custom_header = kwargs.get("custom_header", None)
        self.query = kwargs.get("query", 30)
        self.path = kwargs["path"]
        self.body = kwargs["body"]


class ParameterGroupingPostReservedWordsParameters(msrest.serialization.Model):
    """Parameter group.

    :keyword from_property: 'from' is a reserved word. Pass in 'bob' to pass.
    :paramtype from_property: str
    :keyword accept: 'accept' is a reserved word. Pass in 'yes' to pass.
    :paramtype accept: str
    """

    _attribute_map = {
        "from_property": {"key": "from", "type": "str"},
        "accept": {"key": "accept", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(ParameterGroupingPostReservedWordsParameters, self).__init__(**kwargs)
        self.from_property = kwargs.get("from_property", None)
        self.accept = kwargs.get("accept", None)
