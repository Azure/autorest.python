# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, Optional, TYPE_CHECKING, Union, overload

from azure.core.exceptions import ODataV4Format

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class ExportedUser(_model_base.Model):
    """The exported user data.


    :ivar name: The name of user. Required.
    :vartype name: str
    :ivar resource_uri: The exported URI. Required.
    :vartype resource_uri: str
    """

    name: str = rest_field()
    """The name of user. Required."""
    resource_uri: str = rest_field(name="resourceUri")
    """The exported URI. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        resource_uri: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class InnerError(_model_base.Model):
    """An object containing more specific information about the error. As per Microsoft One API
    guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :ivar code: One of a server-defined set of error codes.
    :vartype code: str
    :ivar innererror: Inner error.
    :vartype innererror: ~specs.azure.core.lro.standard.models.InnerError
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


class OperationStatusError(_model_base.Model):
    """Provides status details for long running operations.


    :ivar id: The unique ID of the operation. Required.
    :vartype id: str
    :ivar status: The status of the operation. Required. Known values are: "NotStarted", "Running",
     "Succeeded", "Failed", and "Canceled".
    :vartype status: str or ~specs.azure.core.lro.standard.models.OperationState
    :ivar error: Error object that describes the error when status is "Failed".
    :vartype error: ~azure.core.ODataV4Format
    """

    id: str = rest_field()
    """The unique ID of the operation. Required."""
    status: Union[str, "_models.OperationState"] = rest_field()
    """The status of the operation. Required. Known values are: \"NotStarted\", \"Running\",
     \"Succeeded\", \"Failed\", and \"Canceled\"."""
    error: Optional[ODataV4Format] = rest_field()
    """Error object that describes the error when status is \"Failed\"."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        status: Union[str, "_models.OperationState"],
        error: Optional[ODataV4Format] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OperationStatusExportedUserError(_model_base.Model):
    """Provides status details for long running operations.


    :ivar id: The unique ID of the operation. Required.
    :vartype id: str
    :ivar status: The status of the operation. Required. Known values are: "NotStarted", "Running",
     "Succeeded", "Failed", and "Canceled".
    :vartype status: str or ~specs.azure.core.lro.standard.models.OperationState
    :ivar error: Error object that describes the error when status is "Failed".
    :vartype error: ~azure.core.ODataV4Format
    :ivar result: The result of the operation.
    :vartype result: ~specs.azure.core.lro.standard.models.ExportedUser
    """

    id: str = rest_field()
    """The unique ID of the operation. Required."""
    status: Union[str, "_models.OperationState"] = rest_field()
    """The status of the operation. Required. Known values are: \"NotStarted\", \"Running\",
     \"Succeeded\", \"Failed\", and \"Canceled\"."""
    error: Optional[ODataV4Format] = rest_field()
    """Error object that describes the error when status is \"Failed\"."""
    result: Optional["_models.ExportedUser"] = rest_field()
    """The result of the operation."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        status: Union[str, "_models.OperationState"],
        error: Optional[ODataV4Format] = None,
        result: Optional["_models.ExportedUser"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ResourceOperationStatusUserExportedUserError(_model_base.Model):  # pylint: disable=name-too-long
    """Provides status details for long running operations.


    :ivar id: The unique ID of the operation. Required.
    :vartype id: str
    :ivar status: The status of the operation. Required. Known values are: "NotStarted", "Running",
     "Succeeded", "Failed", and "Canceled".
    :vartype status: str or ~specs.azure.core.lro.standard.models.OperationState
    :ivar error: Error object that describes the error when status is "Failed".
    :vartype error: ~azure.core.ODataV4Format
    :ivar result: The result of the operation.
    :vartype result: ~specs.azure.core.lro.standard.models.ExportedUser
    """

    id: str = rest_field()
    """The unique ID of the operation. Required."""
    status: Union[str, "_models.OperationState"] = rest_field()
    """The status of the operation. Required. Known values are: \"NotStarted\", \"Running\",
     \"Succeeded\", \"Failed\", and \"Canceled\"."""
    error: Optional[ODataV4Format] = rest_field()
    """Error object that describes the error when status is \"Failed\"."""
    result: Optional["_models.ExportedUser"] = rest_field()
    """The result of the operation."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        status: Union[str, "_models.OperationState"],
        error: Optional[ODataV4Format] = None,
        result: Optional["_models.ExportedUser"] = None,
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
    """Details about a user.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar name: The name of user. Required.
    :vartype name: str
    :ivar role: The role of user. Required.
    :vartype role: str
    """

    name: str = rest_field(visibility=["read"])
    """The name of user. Required."""
    role: str = rest_field()
    """The role of user. Required."""

    @overload
    def __init__(
        self,
        *,
        role: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
