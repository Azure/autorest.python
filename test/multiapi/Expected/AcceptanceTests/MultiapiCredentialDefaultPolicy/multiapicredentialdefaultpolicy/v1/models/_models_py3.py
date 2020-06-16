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

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

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


class PagingResult(msrest.serialization.Model):
    """PagingResult.

    :param values:
    :type values: list[~multiapicredentialdefaultpolicy.v1.models.Product]
    :param next_link:
    :type next_link: str
    """

    _attribute_map = {
        'values': {'key': 'values', 'type': '[Product]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        values: Optional[List["Product"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PagingResult, self).__init__(**kwargs)
        self.values = values
        self.next_link = next_link


class Product(msrest.serialization.Model):
    """Product.

    :param id:
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,
        **kwargs
    ):
        super(Product, self).__init__(**kwargs)
        self.id = id


class TestLroAndPagingOptions(msrest.serialization.Model):
    """Parameter group.

    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :type timeout: int
    """

    _attribute_map = {
        'maxresults': {'key': 'maxresults', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        maxresults: Optional[int] = None,
        timeout: Optional[int] = 30,
        **kwargs
    ):
        super(TestLroAndPagingOptions, self).__init__(**kwargs)
        self.maxresults = maxresults
        self.timeout = timeout
