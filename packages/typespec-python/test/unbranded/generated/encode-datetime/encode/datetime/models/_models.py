# coding=utf-8
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, List, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class DefaultDatetimeProperty(_model_base.Model):
    """DefaultDatetimeProperty.

    :ivar value: Required.
    :vartype value: ~datetime.datetime
    """

    value: datetime.datetime = rest_field(visibility=["read", "create", "update", "delete", "query"], format="rfc3339")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: datetime.datetime,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Rfc3339DatetimeProperty(_model_base.Model):
    """Rfc3339DatetimeProperty.

    :ivar value: Required.
    :vartype value: ~datetime.datetime
    """

    value: datetime.datetime = rest_field(visibility=["read", "create", "update", "delete", "query"], format="rfc3339")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: datetime.datetime,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Rfc7231DatetimeProperty(_model_base.Model):
    """Rfc7231DatetimeProperty.

    :ivar value: Required.
    :vartype value: ~datetime.datetime
    """

    value: datetime.datetime = rest_field(visibility=["read", "create", "update", "delete", "query"], format="rfc7231")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: datetime.datetime,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnixTimestampArrayDatetimeProperty(_model_base.Model):
    """UnixTimestampArrayDatetimeProperty.

    :ivar value: Required.
    :vartype value: list[~datetime.datetime]
    """

    value: List[datetime.datetime] = rest_field(
        visibility=["read", "create", "update", "delete", "query"], format="unix-timestamp"
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: List[datetime.datetime],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnixTimestampDatetimeProperty(_model_base.Model):
    """UnixTimestampDatetimeProperty.

    :ivar value: Required.
    :vartype value: ~datetime.datetime
    """

    value: datetime.datetime = rest_field(
        visibility=["read", "create", "update", "delete", "query"], format="unix-timestamp"
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        value: datetime.datetime,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
