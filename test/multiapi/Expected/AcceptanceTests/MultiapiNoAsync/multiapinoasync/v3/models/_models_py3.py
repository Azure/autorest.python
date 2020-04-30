# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Error(msrest.serialization.Model):
    """Error.

    :param message:
    :type message: str
    :param status:
    :type status: int
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'status': {'key': 'status', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        status: Optional[int] = None,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.message = message
        self.status = status


class ModelThree(msrest.serialization.Model):
    """Only exists in api version 3.0.0.

    :param optional_property:
    :type optional_property: str
    """

    _attribute_map = {
        'optional_property': {'key': 'optionalProperty', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        optional_property: Optional[str] = None,
        **kwargs
    ):
        super(ModelThree, self).__init__(**kwargs)
        self.optional_property = optional_property


class PagingResult(msrest.serialization.Model):
    """PagingResult.

    :param next_link:
    :type next_link: str
    :param values:
    :type values: list[~multiapinoasync.v3.models.ModelThree]
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'values': {'key': 'values', 'type': '[ModelThree]'},
    }

    def __init__(
        self,
        *,
        next_link: Optional[str] = None,
        values: Optional[List["ModelThree"]] = None,
        **kwargs
    ):
        super(PagingResult, self).__init__(**kwargs)
        self.next_link = next_link
        self.values = values


class SourcePath(msrest.serialization.Model):
    """Uri or local path to source data.

    :param source: File source path.
    :type source: str
    """

    _validation = {
        'source': {'max_length': 2048, 'min_length': 0},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        source: Optional[str] = None,
        **kwargs
    ):
        super(SourcePath, self).__init__(**kwargs)
        self.source = source
