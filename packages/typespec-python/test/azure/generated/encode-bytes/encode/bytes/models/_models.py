# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, List, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class Base64BytesProperty(_model_base.Model):
    """Base64BytesProperty.

    :ivar value: Required.
    :vartype value: bytes
    """

    value: bytes = rest_field(visibility=["read", "create", "update", "delete", "query"], format="base64")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: bytes,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Base64urlArrayBytesProperty(_model_base.Model):
    """Base64urlArrayBytesProperty.

    :ivar value: Required.
    :vartype value: list[bytes]
    """

    value: List[bytes] = rest_field(visibility=["read", "create", "update", "delete", "query"], format="base64url")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: List[bytes],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Base64urlBytesProperty(_model_base.Model):
    """Base64urlBytesProperty.

    :ivar value: Required.
    :vartype value: bytes
    """

    value: bytes = rest_field(visibility=["read", "create", "update", "delete", "query"], format="base64url")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: bytes,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DefaultBytesProperty(_model_base.Model):
    """DefaultBytesProperty.

    :ivar value: Required.
    :vartype value: bytes
    """

    value: bytes = rest_field(visibility=["read", "create", "update", "delete", "query"], format="base64")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: bytes,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
