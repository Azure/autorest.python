﻿# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class Message(_model_base.Model):
    """Message.

    All required parameters must be populated in order to send to Azure.

    :ivar message: Required.
    :vartype message: str
    """

    message: str = rest_field()
    """Required. """

    @overload
    def __init__(
        self,
        *,
        message: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class PostInput(_model_base.Model):
    """PostInput.

    All required parameters must be populated in order to send to Azure.

    :ivar url: Required.
    :vartype url: str
    """

    url: str = rest_field()
    """Required. """

    @overload
    def __init__(
        self,
        *,
        url: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
