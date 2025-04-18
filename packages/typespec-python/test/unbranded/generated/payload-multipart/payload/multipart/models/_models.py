# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .._utils.model_base import Model as _Model, rest_field
from .._utils.utils import FileType

if TYPE_CHECKING:
    from .. import models as _models


class Address(_Model):
    """Address.

    :ivar city: Required.
    :vartype city: str
    """

    city: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        city: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class BinaryArrayPartsRequest(_Model):
    """BinaryArrayPartsRequest.

    :ivar id: Required.
    :vartype id: str
    :ivar pictures: Required.
    :vartype pictures: list[~payload.multipart._utils.utils.FileType]
    """

    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    pictures: List[FileType] = rest_field(
        visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        pictures: List[FileType],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ComplexHttpPartsModelRequest(_Model):
    """ComplexHttpPartsModelRequest.

    :ivar id: Required.
    :vartype id: str
    :ivar address: Required.
    :vartype address: ~payload.multipart.models.Address
    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._utils.utils.FileType
    :ivar previous_addresses: Required.
    :vartype previous_addresses: list[~payload.multipart.models.Address]
    :ivar pictures: Required.
    :vartype pictures: list[~payload.multipart._utils.utils.FileType]
    """

    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    address: "_models.Address" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""
    previous_addresses: List["_models.Address"] = rest_field(
        name="previousAddresses", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required."""
    pictures: List[FileType] = rest_field(
        visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
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
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ComplexPartsRequest(_Model):
    """ComplexPartsRequest.

    :ivar id: Required.
    :vartype id: str
    :ivar address: Required.
    :vartype address: ~payload.multipart.models.Address
    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._utils.utils.FileType
    :ivar pictures: Required.
    :vartype pictures: list[~payload.multipart._utils.utils.FileType]
    """

    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    address: "_models.Address" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""
    pictures: List[FileType] = rest_field(
        visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        address: "_models.Address",
        profile_image: FileType,
        pictures: List[FileType],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FileWithHttpPartOptionalContentTypeRequest(_Model):  # pylint: disable=name-too-long
    """FileWithHttpPartOptionalContentTypeRequest.

    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._utils.utils.FileType
    """

    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        profile_image: FileType,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FileWithHttpPartRequiredContentTypeRequest(_Model):  # pylint: disable=name-too-long
    """FileWithHttpPartRequiredContentTypeRequest.

    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._utils.utils.FileType
    """

    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        profile_image: FileType,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FileWithHttpPartSpecificContentTypeRequest(_Model):  # pylint: disable=name-too-long
    """FileWithHttpPartSpecificContentTypeRequest.

    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._utils.utils.FileType
    """

    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        profile_image: FileType,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class JsonPartRequest(_Model):
    """JsonPartRequest.

    :ivar address: Required.
    :vartype address: ~payload.multipart.models.Address
    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._utils.utils.FileType
    """

    address: "_models.Address" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        address: "_models.Address",
        profile_image: FileType,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class MultiBinaryPartsRequest(_Model):
    """MultiBinaryPartsRequest.

    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._utils.utils.FileType
    :ivar picture:
    :vartype picture: ~payload.multipart._utils.utils.FileType
    """

    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""
    picture: Optional[FileType] = rest_field(
        visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )

    @overload
    def __init__(
        self,
        *,
        profile_image: FileType,
        picture: Optional[FileType] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class MultiPartRequest(_Model):
    """MultiPartRequest.

    :ivar id: Required.
    :vartype id: str
    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._utils.utils.FileType
    """

    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        profile_image: FileType,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
