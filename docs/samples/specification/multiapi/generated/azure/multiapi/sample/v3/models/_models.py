# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError

from .. import _serialization


class Error(_serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super(Error, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.message = kwargs.get('message', None)


class ModelThree(_serialization.Model):
    """Only exists in api version 3.0.0.

    :ivar optional_property:
    :vartype optional_property: str
    """

    _attribute_map = {
        'optional_property': {'key': 'optionalProperty', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword optional_property:
        :paramtype optional_property: str
        """
        super(ModelThree, self).__init__(**kwargs)
        self.optional_property = kwargs.get('optional_property', None)


class PagingResult(_serialization.Model):
    """PagingResult.

    :ivar values:
    :vartype values: list[~azure.multiapi.sample.v3.models.ModelThree]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[ModelThree]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword values:
        :paramtype values: list[~azure.multiapi.sample.v3.models.ModelThree]
        :keyword next_link:
        :paramtype next_link: str
        """
        super(PagingResult, self).__init__(**kwargs)
        self.values = kwargs.get('values', None)
        self.next_link = kwargs.get('next_link', None)


class SourcePath(_serialization.Model):
    """Uri or local path to source data.

    :ivar source: File source path.
    :vartype source: str
    """

    _validation = {
        'source': {'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword source: File source path.
        :paramtype source: str
        """
        super(SourcePath, self).__init__(**kwargs)
        self.source = kwargs.get('source', None)
