# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, TYPE_CHECKING

from ... import _serialization

if TYPE_CHECKING:
    from .. import models as _models


class Error(_serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.status: Optional[int] = status
        self.message: Optional[str] = message


class PagingResult(_serialization.Model):
    """PagingResult.

    :ivar values:
    :vartype values: list[~multiapidataplane.v1.models.Product]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        "values": {"key": "values", "type": "[Product]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, values: Optional[List["_models.Product"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword values:
        :paramtype values: list[~multiapidataplane.v1.models.Product]
        :keyword next_link:
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.values: Optional[List["_models.Product"]] = values
        self.next_link: Optional[str] = next_link


class Product(_serialization.Model):
    """Product.

    :ivar id:
    :vartype id: int
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
    }

    def __init__(self, *, id: Optional[int] = None, **kwargs: Any) -> None:  # pylint: disable=redefined-builtin
        """
        :keyword id:
        :paramtype id: int
        """
        super().__init__(**kwargs)
        self.id: Optional[int] = id


class TestLroAndPagingOptions(_serialization.Model):
    """Parameter group.

    :ivar maxresults: Sets the maximum number of items to return in the response.
    :vartype maxresults: int
    :ivar timeout: Sets the maximum time that the server can spend processing the request, in
     seconds. The default is 30 seconds.
    :vartype timeout: int
    """

    _attribute_map = {
        "maxresults": {"key": "maxresults", "type": "int"},
        "timeout": {"key": "timeout", "type": "int"},
    }

    def __init__(self, *, maxresults: Optional[int] = None, timeout: int = 30, **kwargs: Any) -> None:
        """
        :keyword maxresults: Sets the maximum number of items to return in the response.
        :paramtype maxresults: int
        :keyword timeout: Sets the maximum time that the server can spend processing the request, in
         seconds. The default is 30 seconds.
        :paramtype timeout: int
        """
        super().__init__(**kwargs)
        self.maxresults: Optional[int] = maxresults
        self.timeout: int = timeout
