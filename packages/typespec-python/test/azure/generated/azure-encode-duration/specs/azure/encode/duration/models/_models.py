# coding=utf-8
# pylint: disable=useless-super-delegation

import datetime
from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class DurationModel(_model_base.Model):
    """DurationModel.

    :ivar input: Required.
    :vartype input: ~datetime.timedelta
    """

    input: datetime.timedelta = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        input: datetime.timedelta,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
