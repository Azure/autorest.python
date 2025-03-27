# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, Optional, overload

from .. import _model_base
from .._model_base import rest_field


class SafeintAsStringProperty(_model_base.Model):
    """SafeintAsStringProperty.

    :ivar value: Required.
    :vartype value: int
    """

    value: int = rest_field(visibility=["read", "create", "update", "delete", "query"], format="str")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Uint32AsStringProperty(_model_base.Model):
    """Uint32AsStringProperty.

    :ivar value:
    :vartype value: int
    """

    value: Optional[int] = rest_field(visibility=["read", "create", "update", "delete", "query"], format="str")

    @overload
    def __init__(
        self,
        *,
        value: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Uint8AsStringProperty(_model_base.Model):
    """Uint8AsStringProperty.

    :ivar value: Required.
    :vartype value: int
    """

    value: int = rest_field(visibility=["read", "create", "update", "delete", "query"], format="str")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
