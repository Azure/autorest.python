# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class CustomPageProduct(_model_base.Model):
    """Paged collection of Product items.

    All required parameters must be populated in order to send to Azure.

    :ivar value: The Product items on this page. Required.
    :vartype value: list[~resiliency.devdriven.models.Product]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    value: List["_models.Product"] = rest_field()
    """The Product items on this page. Required. """
    next_link: Optional[str] = rest_field(name="nextLink")
    """The link to the next page of items. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Error(_model_base.Model):
    """The error object.

    All required parameters must be populated in order to send to Azure.

    :ivar code: One of a server-defined set of error codes. Required.
    :vartype code: str
    :ivar message: A human-readable representation of the error. Required.
    :vartype message: str
    :ivar target: The target of the error.
    :vartype target: str
    :ivar details: An array of details about specific errors that led to this reported error.
     Required.
    :vartype details: list[~resiliency.devdriven.models.Error]
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~resiliency.devdriven.models.InnerError
    """

    code: str = rest_field()
    """One of a server-defined set of error codes. Required. """
    message: str = rest_field()
    """A human-readable representation of the error. Required. """
    target: Optional[str] = rest_field()
    """The target of the error. """
    details: List["_models.Error"] = rest_field()
    """An array of details about specific errors that led to this reported error. Required. """
    innererror: Optional["_models.InnerError"] = rest_field()
    """An object containing more specific information than the current object about the error. """

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
        details: List["_models.Error"],
        target: Optional[str] = None,
        innererror: Optional["_models.InnerError"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ErrorResponse(_model_base.Model):
    """A response containing error details.

    All required parameters must be populated in order to send to Azure.

    :ivar error: The error object. Required.
    :vartype error: ~resiliency.devdriven.models.Error
    """

    error: "_models.Error" = rest_field()
    """The error object. Required. """

    @overload
    def __init__(
        self,
        *,
        error: "_models.Error",
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InnerError(_model_base.Model):
    """An object containing more specific information about the error. As per Microsoft One API guidelines - https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :ivar code: One of a server-defined set of error codes. Required.
    :vartype code: str
    :ivar innererror: Inner error.
    :vartype innererror: ~resiliency.devdriven.models.InnerError
    """

    code: str = rest_field()
    """One of a server-defined set of error codes. Required. """
    innererror: Optional["_models.InnerError"] = rest_field()
    """Inner error. """

    @overload
    def __init__(
        self,
        *,
        code: str,
        innererror: Optional["_models.InnerError"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Input(_model_base.Model):
    """Input.

    All required parameters must be populated in order to send to Azure.

    :ivar hello: Required.
    :vartype hello: str
    """

    hello: str = rest_field()
    """Required. """

    @overload
    def __init__(
        self,
        *,
        hello: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Product(_model_base.Model):
    """Product.

    All required parameters must be populated in order to send to Azure.

    :ivar key: Required.
    :vartype key: str
    :ivar received: Required. Known values are: "raw" and "model".
    :vartype received: str or ~resiliency.devdriven.models.Mode
    """

    key: str = rest_field()
    """Required. """
    received: Union[str, "_models.Mode"] = rest_field()
    """Required. Known values are: \"raw\" and \"model\"."""

    @overload
    def __init__(
        self,
        *,
        key: str,
        received: Union[str, "_models.Mode"],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LROProduct(Product):
    """LROProduct.

    All required parameters must be populated in order to send to Azure.

    :ivar key: Required.
    :vartype key: str
    :ivar received: Required. Known values are: "raw" and "model".
    :vartype received: str or ~resiliency.devdriven.models.Mode
    :ivar provisioning_state: Required.
    :vartype provisioning_state: str
    """

    provisioning_state: str = rest_field(name="provisioningState")
    """Required. """

    @overload
    def __init__(
        self,
        *,
        key: str,
        received: Union[str, "_models.Mode"],
        provisioning_state: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
