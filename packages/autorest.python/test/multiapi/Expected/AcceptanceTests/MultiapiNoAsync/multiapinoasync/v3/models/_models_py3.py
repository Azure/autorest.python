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


class ModelThree(_serialization.Model):
    """Only exists in api version 3.0.0.

    :ivar optional_property:
    :vartype optional_property: str
    """

    _attribute_map = {
        "optional_property": {"key": "optionalProperty", "type": "str"},
    }

    def __init__(self, *, optional_property: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword optional_property:
        :paramtype optional_property: str
        """
        super().__init__(**kwargs)
        self.optional_property: Optional[str] = optional_property


class PagingResult(_serialization.Model):
    """PagingResult.

    :ivar values:
    :vartype values: list[~multiapinoasync.v3.models.ModelThree]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        "values": {"key": "values", "type": "[ModelThree]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, values: Optional[List["_models.ModelThree"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword values:
        :paramtype values: list[~multiapinoasync.v3.models.ModelThree]
        :keyword next_link:
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.values: Optional[List["_models.ModelThree"]] = values
        self.next_link: Optional[str] = next_link


class SourcePath(_serialization.Model):
    """Uri or local path to source data.

    :ivar source: File source path.
    :vartype source: str
    """

    _validation = {
        "source": {"max_length": 2048},
    }

    _attribute_map = {
        "source": {"key": "source", "type": "str"},
    }

    def __init__(self, *, source: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword source: File source path.
        :paramtype source: str
        """
        super().__init__(**kwargs)
        self.source: Optional[str] = source
