# coding=utf-8
# pylint: disable=too-many-lines


import datetime
from typing import Any, List, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class DefaultDurationProperty(_model_base.Model):
    """DefaultDurationProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: ~datetime.timedelta
    """

    value: datetime.timedelta = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: datetime.timedelta,
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


class FloatSecondsDurationArrayProperty(_model_base.Model):
    """FloatSecondsDurationArrayProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: list[float]
    """

    value: List[float] = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: List[float],
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


class FloatSecondsDurationProperty(_model_base.Model):
    """FloatSecondsDurationProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: float
    """

    value: float = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: float,
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


class Int32SecondsDurationProperty(_model_base.Model):
    """Int32SecondsDurationProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: int
    """

    value: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: int,
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


class ISO8601DurationProperty(_model_base.Model):
    """ISO8601DurationProperty.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Required.
    :vartype value: ~datetime.timedelta
    """

    value: datetime.timedelta = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: datetime.timedelta,
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
