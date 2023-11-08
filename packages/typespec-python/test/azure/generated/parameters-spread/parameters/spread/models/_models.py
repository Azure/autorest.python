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


class BodyParameter(_model_base.Model):
    """This is a simple model.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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


class GeneratedName1(_model_base.Model):
    """GeneratedName1.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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


class GeneratedName2(_model_base.Model):
    """GeneratedName2.

    All required parameters must be populated in order to send to server.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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


class GeneratedName3(_model_base.Model):
    """GeneratedName3.

    All required parameters must be populated in order to send to server.

    :ivar prop1: Required.
    :vartype prop1: str
    :ivar prop2: Required.
    :vartype prop2: str
    :ivar prop3: Required.
    :vartype prop3: str
    :ivar prop4: Required.
    :vartype prop4: str
    :ivar prop5: Required.
    :vartype prop5: str
    :ivar prop6: Required.
    :vartype prop6: str
    """

    prop1: str = rest_field()
    """Required."""
    prop2: str = rest_field()
    """Required."""
    prop3: str = rest_field()
    """Required."""
    prop4: str = rest_field()
    """Required."""
    prop5: str = rest_field()
    """Required."""
    prop6: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        prop1: str,
        prop2: str,
        prop3: str,
        prop4: str,
        prop5: str,
        prop6: str,
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
