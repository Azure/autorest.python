# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from ..._utils.model_base import Model as _Model, rest_field

if TYPE_CHECKING:
    from ... import models as _models2


class NestedLinkResponseNestedItems(_Model):
    """NestedLinkResponseNestedItems.

    :ivar pets: Required.
    :vartype pets: list[~payload.pageable.models.Pet]
    """

    pets: List["_models2.Pet"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        pets: List["_models2.Pet"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class NestedLinkResponseNestedNext(_Model):
    """NestedLinkResponseNestedNext.

    :ivar next:
    :vartype next: str
    """

    next: Optional[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])

    @overload
    def __init__(
        self,
        *,
        next: Optional[str] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
