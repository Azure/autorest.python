# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from .._utils.model_base import Model as _Model, rest_field


class CommaDelimitedArrayProperty(_Model):
    """CommaDelimitedArrayProperty.

    :ivar value: Required.
    :vartype value: list[str]
    """

    value: list[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: list[str],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class NewlineDelimitedArrayProperty(_Model):
    """NewlineDelimitedArrayProperty.

    :ivar value: Required.
    :vartype value: list[str]
    """

    value: list[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: list[str],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PipeDelimitedArrayProperty(_Model):
    """PipeDelimitedArrayProperty.

    :ivar value: Required.
    :vartype value: list[str]
    """

    value: list[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: list[str],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SpaceDelimitedArrayProperty(_Model):
    """SpaceDelimitedArrayProperty.

    :ivar value: Required.
    :vartype value: list[str]
    """

    value: list[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: list[str],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
