# coding=utf-8
# pylint: disable=too-many-lines


from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class User(_model_base.Model):
    """User model.

    All required parameters must be populated in order to send to Azure.

    :ivar name: User name. Required.
    :vartype name: str
    """

    name: str = rest_field()
    """User name. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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
