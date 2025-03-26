# coding=utf-8
None
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, List, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class DefaultDurationProperty(_model_base.Model):
    """DefaultDurationProperty.

    :ivar value: Required.
    :vartype value: ~datetime.timedelta
    """

    value: datetime.timedelta = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: datetime.timedelta,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Float64SecondsDurationProperty(_model_base.Model):
    """Float64SecondsDurationProperty.

    :ivar value: Required.
    :vartype value: float
    """

    value: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: float,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FloatSecondsDurationArrayProperty(_model_base.Model):
    """FloatSecondsDurationArrayProperty.

    :ivar value: Required.
    :vartype value: list[float]
    """

    value: List[float] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: List[float],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FloatSecondsDurationProperty(_model_base.Model):
    """FloatSecondsDurationProperty.

    :ivar value: Required.
    :vartype value: float
    """

    value: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: float,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Int32SecondsDurationProperty(_model_base.Model):
    """Int32SecondsDurationProperty.

    :ivar value: Required.
    :vartype value: int
    """

    value: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
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


class ISO8601DurationProperty(_model_base.Model):
    """ISO8601DurationProperty.

    :ivar value: Required.
    :vartype value: ~datetime.timedelta
    """

    value: datetime.timedelta = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: datetime.timedelta,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
