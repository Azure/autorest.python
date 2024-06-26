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
from .._model_base import rest_field
from .._vendor import FileType

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class Address(_model_base.Model):
    """Address.

    All required parameters must be populated in order to send to server.

    :ivar city: Required.
    :vartype city: str
    """

    city: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        city: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class BinaryArrayPartsRequest(_model_base.Model):
    """BinaryArrayPartsRequest.

    All required parameters must be populated in order to send to server.

    :ivar id: Required.
    :vartype id: str
    :ivar pictures: Required.
    :vartype pictures: list[bytes]
    """

    id: str = rest_field()
    """Required."""
    pictures: List[FileType] = rest_field(is_multipart_file_input=True)
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        pictures: List[FileType],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ComplexPartsRequest(_model_base.Model):
    """ComplexPartsRequest.

    All required parameters must be populated in order to send to server.

    :ivar id: Required.
    :vartype id: str
    :ivar address: Required.
    :vartype address: ~payload.multipart.models.Address
    :ivar profile_image: Required.
    :vartype profile_image: bytes
    :ivar previous_addresses: Required.
    :vartype previous_addresses: list[~payload.multipart.models.Address]
    :ivar pictures: Required.
    :vartype pictures: list[bytes]
    """

    id: str = rest_field()
    """Required."""
    address: "_models.Address" = rest_field()
    """Required."""
    profile_image: FileType = rest_field(name="profileImage", is_multipart_file_input=True)
    """Required."""
    previous_addresses: List["_models.Address"] = rest_field(name="previousAddresses")
    """Required."""
    pictures: List[FileType] = rest_field(is_multipart_file_input=True)
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        address: "_models.Address",
        profile_image: FileType,
        previous_addresses: List["_models.Address"],
        pictures: List[FileType],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class JsonArrayPartsRequest(_model_base.Model):
    """JsonArrayPartsRequest.

    All required parameters must be populated in order to send to server.

    :ivar profile_image: Required.
    :vartype profile_image: bytes
    :ivar previous_addresses: Required.
    :vartype previous_addresses: list[~payload.multipart.models.Address]
    """

    profile_image: FileType = rest_field(name="profileImage", is_multipart_file_input=True)
    """Required."""
    previous_addresses: List["_models.Address"] = rest_field(name="previousAddresses")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        profile_image: FileType,
        previous_addresses: List["_models.Address"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class JsonPartRequest(_model_base.Model):
    """JsonPartRequest.

    All required parameters must be populated in order to send to server.

    :ivar address: Required.
    :vartype address: ~payload.multipart.models.Address
    :ivar profile_image: Required.
    :vartype profile_image: bytes
    """

    address: "_models.Address" = rest_field()
    """Required."""
    profile_image: FileType = rest_field(name="profileImage", is_multipart_file_input=True)
    """Required."""

    @overload
    def __init__(
        self,
        *,
        address: "_models.Address",
        profile_image: FileType,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class MultiBinaryPartsRequest(_model_base.Model):
    """MultiBinaryPartsRequest.

    All required parameters must be populated in order to send to server.

    :ivar profile_image: Required.
    :vartype profile_image: bytes
    :ivar picture:
    :vartype picture: bytes
    """

    profile_image: FileType = rest_field(name="profileImage", is_multipart_file_input=True)
    """Required."""
    picture: Optional[FileType] = rest_field(is_multipart_file_input=True)

    @overload
    def __init__(
        self,
        *,
        profile_image: FileType,
        picture: Optional[FileType] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class MultiPartRequest(_model_base.Model):
    """MultiPartRequest.

    All required parameters must be populated in order to send to server.

    :ivar id: Required.
    :vartype id: str
    :ivar profile_image: Required.
    :vartype profile_image: bytes
    """

    id: str = rest_field()
    """Required."""
    profile_image: FileType = rest_field(name="profileImage", is_multipart_file_input=True)
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        profile_image: FileType,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
