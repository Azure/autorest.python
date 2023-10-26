# coding=utf-8
# pylint: disable=too-many-lines


from typing import Any, List, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class Base64BytesProperty(_model_base.Model):
    """Base64BytesProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: bytes
    """

    value: bytes = rest_field(format="base64")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: bytes,
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


class Base64urlArrayBytesProperty(_model_base.Model):
    """Base64urlArrayBytesProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: list[bytes]
    """

    value: List[bytes] = rest_field(format="base64url")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: List[bytes],
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


class Base64urlBytesProperty(_model_base.Model):
    """Base64urlBytesProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: bytes
    """

    value: bytes = rest_field(format="base64url")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: bytes,
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


class DefaultBytesProperty(_model_base.Model):
    """DefaultBytesProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: bytes
    """

    value: bytes = rest_field(format="base64")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: bytes,
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
