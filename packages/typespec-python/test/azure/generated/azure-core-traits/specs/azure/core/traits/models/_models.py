# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, Optional, overload

from .. import _model_base
from .._model_base import rest_field


class User(_model_base.Model):
    """Sample Model.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: The user's id. Required.
    :vartype id: int
    :ivar name: The user's name.
    :vartype name: str
    """

    id: int = rest_field(visibility=["read"])
    """The user's id. Required."""
    name: Optional[str] = rest_field()
    """The user's name."""

    @overload
    def __init__(
        self,
        *,
        name: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        Warning: we don't make deepcopy for mapping so if you change value of mapping after init,
        value of the model will be changed, too.

        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UserActionParam(_model_base.Model):
    """User action param.

    All required parameters must be populated in order to send to server.

    :ivar user_action_value: User action value. Required.
    :vartype user_action_value: str
    """

    user_action_value: str = rest_field(name="userActionValue")
    """User action value. Required."""

    @overload
    def __init__(
        self,
        *,
        user_action_value: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        Warning: we don't make deepcopy for mapping so if you change value of mapping after init,
        value of the model will be changed, too.

        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class UserActionResponse(_model_base.Model):
    """User action response.

    All required parameters must be populated in order to send to server.

    :ivar user_action_result: User action result. Required.
    :vartype user_action_result: str
    """

    user_action_result: str = rest_field(name="userActionResult")
    """User action result. Required."""

    @overload
    def __init__(
        self,
        *,
        user_action_result: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        Warning: we don't make deepcopy for mapping so if you change value of mapping after init,
        value of the model will be changed, too.

        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
