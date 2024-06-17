# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Error(_model_base.Model):
    """The error object.


    :ivar code: One of a server-defined set of error codes. Required.
    :vartype code: str
    :ivar message: A human-readable representation of the error. Required.
    :vartype message: str
    :ivar target: The target of the error.
    :vartype target: str
    :ivar details: An array of details about specific errors that led to this reported error.
    :vartype details: list[~azurecore.lro.rpc.models.Error]
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~azurecore.lro.rpc.models.InnerError
    """

    code: str = rest_field()
    """One of a server-defined set of error codes. Required."""
    message: str = rest_field()
    """A human-readable representation of the error. Required."""
    target: Optional[str] = rest_field()
    """The target of the error."""
    details: Optional[List["_models.Error"]] = rest_field()
    """An array of details about specific errors that led to this reported error."""
    innererror: Optional["_models.InnerError"] = rest_field()
    """An object containing more specific information than the current object about the error."""

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        details: Optional[List["_models.Error"]] = None,
        innererror: Optional["_models.InnerError"] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GenerationOptions(_model_base.Model):
    """Options for the generation.

    All required parameters must be populated in order to send to server.

    :ivar prompt: Prompt. Required.
    :vartype prompt: str
    """

    prompt: str = rest_field()
    """Prompt. Required."""

    @overload
    def __init__(
        self,
        *,
        prompt: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GenerationResponse(_model_base.Model):
    """Provides status details for long running operations.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar id: The unique ID of the operation. Required.
    :vartype id: str
    :ivar status: The status of the operation. Required. Known values are: "NotStarted", "Running",
     "Succeeded", "Failed", and "Canceled".
    :vartype status: str or ~azurecore.lro.rpc.models.OperationState
    :ivar error: Error object that describes the error when status is "Failed".
    :vartype error: ~azurecore.lro.rpc.models.Error
    :ivar result: The result of the operation.
    :vartype result: ~azurecore.lro.rpc.models.GenerationResult
    """

    id: str = rest_field(visibility=["read"])
    """The unique ID of the operation. Required."""
    status: Union[str, "_models.OperationState"] = rest_field()
    """The status of the operation. Required. Known values are: \"NotStarted\", \"Running\",
     \"Succeeded\", \"Failed\", and \"Canceled\"."""
    error: Optional["_models.Error"] = rest_field()
    """Error object that describes the error when status is \"Failed\"."""
    result: Optional["_models.GenerationResult"] = rest_field()
    """The result of the operation."""

    @overload
    def __init__(
        self,
        *,
        status: Union[str, "_models.OperationState"],
        error: Optional["_models.Error"] = None,
        result: Optional["_models.GenerationResult"] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GenerationResult(_model_base.Model):
    """Result of the generation.


    :ivar data: The data. Required.
    :vartype data: str
    """

    data: str = rest_field()
    """The data. Required."""

    @overload
    def __init__(
        self,
        *,
        data: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class InnerError(_model_base.Model):
    """An object containing more specific information about the error. As per Microsoft One API
    guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :ivar code: One of a server-defined set of error codes.
    :vartype code: str
    :ivar innererror: Inner error.
    :vartype innererror: ~azurecore.lro.rpc.models.InnerError
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
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
