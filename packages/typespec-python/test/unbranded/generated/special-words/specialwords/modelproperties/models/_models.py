# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from ..._utils.model_base import Model as _Model, rest_field


class SameAsModel(_Model):
    """SameAsModel.

    :ivar same_as_model: Required.
    :vartype same_as_model: str
    """

    same_as_model: str = rest_field(name="SameAsModel", visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        same_as_model: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
