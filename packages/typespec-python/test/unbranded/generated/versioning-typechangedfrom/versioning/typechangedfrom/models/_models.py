# coding=utf-8

# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class TestModel(_model_base.Model):
    """TestModel.

    :ivar prop: Required.
    :vartype prop: str
    :ivar changed_prop: Required.
    :vartype changed_prop: str
    """

    prop: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    changed_prop: str = rest_field(name="changedProp", visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        prop: str,
        changed_prop: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
