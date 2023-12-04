# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class ExtendsFloatAdditionalProperties(_model_base.Model):
    """The model extends from Record:code:`<float32>` type.

    All required parameters must be populated in order to send to server.

    :ivar id: The id property. Required.
    :vartype id: float
    """

    id: float = rest_field()
    """The id property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
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


class ExtendsModelAdditionalProperties(_model_base.Model):
    """The model extends from Record:code:`<ModelForRecord>` type."""


class ExtendsModelArrayAdditionalProperties(_model_base.Model):
    """The model extends from Record<ModelForRecord[]> type."""


class ExtendsStringAdditionalProperties(_model_base.Model):
    """The model extends from Record:code:`<string>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """The name property. Required."""

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


class ExtendsUnknownAdditionalProperties(_model_base.Model):
    """The model extends from Record:code:`<unknown>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """The name property. Required."""

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


class IsFloatAdditionalProperties(_model_base.Model):
    """The model is from Record:code:`<float32>` type.

    All required parameters must be populated in order to send to server.

    :ivar id: The id property. Required.
    :vartype id: float
    """

    id: float = rest_field()
    """The id property. Required."""

    @overload
    def __init__(
        self,
        *,
        id: float,  # pylint: disable=redefined-builtin
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


class IsModelAdditionalProperties(_model_base.Model):
    """The model is from Record:code:`<ModelForRecord>` type."""


class IsModelArrayAdditionalProperties(_model_base.Model):
    """The model is from Record<ModelForRecord[]> type."""


class IsStringAdditionalProperties(_model_base.Model):
    """The model is from Record:code:`<string>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """The name property. Required."""

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


class IsUnknownAdditionalProperties(_model_base.Model):
    """The model is from Record:code:`<unknown>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """The name property. Required."""

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
