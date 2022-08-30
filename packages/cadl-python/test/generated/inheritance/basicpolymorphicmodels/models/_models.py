# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class BaseClass(_model_base.Model):
    """Example base type.

    All required parameters must be populated in order to send to Azure.

    :ivar base_class_property: An example property. Required.
    :vartype base_class_property: str
    """

    base_class_property: str = rest_field(name="baseClassProperty")
    """An example property. Required. """

    @overload
    def __init__(
        self,
        *,
        base_class_property: str,
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


class BaseClassWithDiscriminator(BaseClass):
    """Example base class that has a discriminator property.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    DerivedFromBaseClassWithDiscriminatorA, DerivedFromBaseClassWithDiscriminatorB

    All required parameters must be populated in order to send to Azure.

    :ivar base_class_property: An example property. Required.
    :vartype base_class_property: str
    :ivar discriminator_property: Required. Default value is "B".
    :vartype discriminator_property: str
    """

    __mapping__ = {}
    discriminator_property: str = rest_discriminator(name="discriminatorProperty")
    """Required. Default value is \"B\"."""

    @overload
    def __init__(
        self,
        *,
        base_class_property: str,
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


class DerivedFromBaseClassWithDiscriminatorA(BaseClassWithDiscriminator, discriminator="A"):
    """DerivedFromBaseClassWithDiscriminatorA.

    All required parameters must be populated in order to send to Azure.

    :ivar base_class_property: An example property. Required.
    :vartype base_class_property: str
    :ivar discriminator_property: Required. Default value is "A".
    :vartype discriminator_property: str
    """

    @overload
    def __init__(
        self,
        *,
        base_class_property: str,
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
        self.discriminator_property = "A"  # type: str


class DerivedFromBaseClassWithDiscriminatorB(BaseClassWithDiscriminator, discriminator="B"):
    """DerivedFromBaseClassWithDiscriminatorB.

    All required parameters must be populated in order to send to Azure.

    :ivar base_class_property: An example property. Required.
    :vartype base_class_property: str
    :ivar discriminator_property: Required. Default value is "B".
    :vartype discriminator_property: str
    """

    @overload
    def __init__(
        self,
        *,
        base_class_property: str,
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
        self.discriminator_property = "B"  # type: str


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
    :vartype details: list[~basicpolymorphicmodels.models.Error]
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~basicpolymorphicmodels.models.InnerError
    """

    code: str = rest_field(name="code")
    """One of a server-defined set of error codes. Required. """
    message: str = rest_field(name="message")
    """A human-readable representation of the error. Required. """
    target: Optional[str] = rest_field(name="target")
    """The target of the error. """
    details: List["Error"] = rest_field(name="details")
    """An array of details about specific errors that led to this reported error. Required. """
    innererror: Optional["InnerError"] = rest_field(name="innererror")
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
    :vartype error: ~basicpolymorphicmodels.models.Error
    """

    error: "Error" = rest_field(name="error")
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
    :vartype innererror: ~basicpolymorphicmodels.models.InnerError
    """

    code: str = rest_field(name="code")
    """One of a server-defined set of error codes. Required. """
    innererror: Optional["InnerError"] = rest_field(name="innererror")
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


class ModelWithPolymorphicProperty(_model_base.Model):
    """Illustrates case where a basic model has polymorphic properties.

    All required parameters must be populated in order to send to Azure.

    :ivar polymorphic_property: Example polymorphic type property. Required.
    :vartype polymorphic_property: ~basicpolymorphicmodels.models.BaseClassWithDiscriminator
    """

    polymorphic_property: "BaseClassWithDiscriminator" = rest_field(name="polymorphicProperty")
    """Example polymorphic type property. Required. """

    @overload
    def __init__(
        self,
        *,
        polymorphic_property: "_models.BaseClassWithDiscriminator",
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
