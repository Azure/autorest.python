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


class ClientModel(_model_base.Model):
    """ClientModel.

    All required parameters must be populated in order to send to server.

    :ivar default_name: Pass in true. Required.
    :vartype default_name: bool
    """

    default_name: bool = rest_field(name="defaultName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        default_name: bool,
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


class ClientNameAndJsonEncodedNameModel(_model_base.Model):
    """ClientNameAndJsonEncodedNameModel.

    All required parameters must be populated in order to send to server.

    :ivar client_name: Pass in true. Required.
    :vartype client_name: bool
    """

    client_name: bool = rest_field(name="wireName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        client_name: bool,
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


class ClientNameModel(_model_base.Model):
    """ClientNameModel.

    All required parameters must be populated in order to send to server.

    :ivar client_name: Pass in true. Required.
    :vartype client_name: bool
    """

    client_name: bool = rest_field(name="defaultName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        client_name: bool,
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


class LanguageClientNameModel(_model_base.Model):
    """LanguageClientNameModel.

    All required parameters must be populated in order to send to server.

    :ivar python_name: Pass in true. Required.
    :vartype python_name: bool
    """

    python_name: bool = rest_field(name="defaultName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        python_name: bool,
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


class PythonModel(_model_base.Model):
    """PythonModel.

    All required parameters must be populated in order to send to server.

    :ivar default_name: Pass in true. Required.
    :vartype default_name: bool
    """

    default_name: bool = rest_field(name="defaultName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        default_name: bool,
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
