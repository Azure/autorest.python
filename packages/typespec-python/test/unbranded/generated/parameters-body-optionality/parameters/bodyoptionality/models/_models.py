# coding=utf-8
# pylint: disable=too-many-lines


from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class BodyModel(_model_base.Model):
    """BodyModel.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

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
