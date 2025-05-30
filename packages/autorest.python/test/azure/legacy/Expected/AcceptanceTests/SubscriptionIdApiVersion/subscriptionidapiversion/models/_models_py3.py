# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from .._utils import serialization as _serialization


class Error(_serialization.Model):
    """Error.

    :ivar code:
    :vartype code: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, code: Optional[int] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword code:
        :paramtype code: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message


class SampleResourceGroup(_serialization.Model):
    """SampleResourceGroup.

    :ivar name: resource group name 'testgroup101'.
    :vartype name: str
    :ivar location: resource group location 'West US'.
    :vartype location: str
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, name: Optional[str] = None, location: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword name: resource group name 'testgroup101'.
        :paramtype name: str
        :keyword location: resource group location 'West US'.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.location = location
