# coding=utf-8
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


class InputOutputRecord(_model_base.Model):
    """Record used both as operation parameter and return type.

    All required parameters must be populated in order to send to server.

    :ivar required_prop: Required.
    :vartype required_prop: str
    """

    required_prop: str = rest_field(name="requiredProp")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        required_prop: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class InputRecord(_model_base.Model):
    """Record used in operation parameters.

    All required parameters must be populated in order to send to server.

    :ivar required_prop: Required.
    :vartype required_prop: str
    """

    required_prop: str = rest_field(name="requiredProp")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        required_prop: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OutputRecord(_model_base.Model):
    """Record used in operation return type.

    All required parameters must be populated in order to send to server.

    :ivar required_prop: Required.
    :vartype required_prop: str
    """

    required_prop: str = rest_field(name="requiredProp")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        required_prop: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
