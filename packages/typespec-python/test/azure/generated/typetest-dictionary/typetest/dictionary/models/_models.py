# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Dict, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class InnerModel(_model_base.Model):
    """Dictionary inner model.

    :ivar property: Required string property. Required.
    :vartype property: str
    :ivar children:
    :vartype children: dict[str, ~typetest.dictionary.models.InnerModel]
    """

    property: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required string property. Required."""
    children: Optional[Dict[str, "_models.InnerModel"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
        children: Optional[Dict[str, "_models.InnerModel"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
