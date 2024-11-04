# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class InnerError(_model_base.Model):
    """An object containing more specific information about the error. As per Microsoft One API
    guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :ivar code: One of a server-defined set of error codes.
    :vartype code: str
    :ivar innererror: Inner error.
    :vartype innererror: ~specs.azure.core.traits.models.InnerError
    """

    code: Optional[str] = rest_field()
    """One of a server-defined set of error codes."""
    innererror: Optional["_models.InnerError"] = rest_field()
    """Inner error."""

    @overload
    def __init__(
        self,
        *,
        code: Optional[str] = None,
        innererror: Optional["_models.InnerError"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class User(_model_base.Model):
    """Sample Model.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


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
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
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
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UserActionResponse(_model_base.Model):
    """User action response.


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
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
