# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, Dict, Mapping, Optional, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports


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


class ExtendsUnknownAdditionalPropertiesDerived(ExtendsUnknownAdditionalProperties):
    """The model extends from a type that extends from Record:code:`<unknown>`.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    index: int = rest_field()
    """The index property. Required."""
    age: Optional[float] = rest_field()
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
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


class ExtendsUnknownAdditionalPropertiesDiscriminated(_model_base.Model):
    """The model extends from Record:code:`<unknown>` with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    ExtendsUnknownAdditionalPropertiesDiscriminatedDerived

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: The discriminator. Required. Default value is None.
    :vartype kind: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    name: str = rest_field()
    """The name property. Required."""
    kind: Literal[None] = rest_discriminator(name="kind")
    """The discriminator. Required. Default value is None."""

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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal[None] = None


class ExtendsUnknownAdditionalPropertiesDiscriminatedDerived(
    ExtendsUnknownAdditionalPropertiesDiscriminated, discriminator="derived"
):
    """The derived discriminated type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: Required. Default value is "derived".
    :vartype kind: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    kind: Literal["derived"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"derived\"."""
    index: int = rest_field()
    """The index property. Required."""
    age: Optional[float] = rest_field()
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["derived"] = "derived"


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


class IsUnknownAdditionalPropertiesDerived(IsUnknownAdditionalProperties):
    """The model extends from a type that is Record:code:`<unknown>` type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    index: int = rest_field()
    """The index property. Required."""
    age: Optional[float] = rest_field()
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
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


class IsUnknownAdditionalPropertiesDiscriminated(_model_base.Model):
    """The model is Record:code:`<unknown>` with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    IsUnknownAdditionalPropertiesDiscriminatedDerived

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: The discriminator. Required. Default value is None.
    :vartype kind: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    name: str = rest_field()
    """The name property. Required."""
    kind: Literal[None] = rest_discriminator(name="kind")
    """The discriminator. Required. Default value is None."""

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

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal[None] = None


class IsUnknownAdditionalPropertiesDiscriminatedDerived(
    IsUnknownAdditionalPropertiesDiscriminated, discriminator="derived"
):
    """The derived discriminated type.

    All required parameters must be populated in order to send to server.

    :ivar name: The name property. Required.
    :vartype name: str
    :ivar kind: Required. Default value is "derived".
    :vartype kind: str
    :ivar index: The index property. Required.
    :vartype index: int
    :ivar age: The age property.
    :vartype age: float
    """

    kind: Literal["derived"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"derived\"."""
    index: int = rest_field()
    """The index property. Required."""
    age: Optional[float] = rest_field()
    """The age property."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        index: int,
        age: Optional[float] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal["derived"] = "derived"
