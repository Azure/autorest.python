# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, Optional, TYPE_CHECKING, overload

from .._utils.model_base import Model as _Model, rest_field

if TYPE_CHECKING:
    from .. import models as _models


class Element(_Model):
    """element.

    :ivar extension:
    :vartype extension: list[~typetest.model.recursive.models.Extension]
    """

    extension: Optional[list["_models.Extension"]] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )

    @overload
    def __init__(
        self,
        *,
        extension: Optional[list["_models.Extension"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Extension(Element):
    """extension.

    :ivar extension:
    :vartype extension: list[~typetest.model.recursive.models.Extension]
    :ivar level: Required.
    :vartype level: int
    """

    level: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        level: int,
        extension: Optional[list["_models.Extension"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
