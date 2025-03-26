# coding=utf-8
None
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class Pet(_model_base.Model):
    """Pet.

    :ivar id: Required.
    :vartype id: str
    :ivar name: Required.
    :vartype name: str
    """

    id: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
