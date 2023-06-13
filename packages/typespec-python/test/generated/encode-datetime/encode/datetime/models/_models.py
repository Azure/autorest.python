# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class DatetimeProperty(_model_base.Model):
    """DatetimeProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar default: Required.
    :vartype default: ~datetime.datetime
    :ivar rfc3339: Required.
    :vartype rfc3339: ~datetime.datetime
    :ivar rfc7231: Required.
    :vartype rfc7231: ~datetime.datetime
    :ivar unix_timestamp: Required.
    :vartype unix_timestamp: int
    :ivar rfc3339_array: Required.
    :vartype rfc3339_array: list[~datetime.datetime]
    """

    default: datetime.datetime = rest_field()
    """Required."""
    rfc3339: datetime.datetime = rest_field()
    """Required."""
    rfc7231: datetime.datetime = rest_field()
    """Required."""
    unix_timestamp: int = rest_field(name="unixTimestamp")
    """Required."""
    rfc3339_array: List[datetime.datetime] = rest_field(name="rfc3339Array")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        default: datetime.datetime,
        rfc3339: datetime.datetime,
        rfc7231: datetime.datetime,
        unix_timestamp: int,
        rfc3339_array: List[datetime.datetime],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
