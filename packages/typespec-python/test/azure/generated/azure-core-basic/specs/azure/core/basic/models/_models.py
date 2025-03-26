# coding=utf-8
None
# pylint: disable=useless-super-delegation

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class User(_model_base.Model):
    """Details about a user.

    :ivar id: The user's id. Required.
    :vartype id: int
    :ivar name: The user's name. Required.
    :vartype name: str
    :ivar orders: The user's order list.
    :vartype orders: list[~specs.azure.core.basic.models.UserOrder]
    :ivar etag: The entity tag for this resource. Required.
    :vartype etag: str
    """

    id: int = rest_field(visibility=["read"])
    """The user's id. Required."""
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The user's name. Required."""
    orders: Optional[List["_models.UserOrder"]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The user's order list."""
    etag: str = rest_field(visibility=["read"])
    """The entity tag for this resource. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        orders: Optional[List["_models.UserOrder"]] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UserList(_model_base.Model):
    """UserList.

    :ivar users: Required.
    :vartype users: list[~specs.azure.core.basic.models.User]
    """

    users: List["_models.User"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        users: List["_models.User"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UserOrder(_model_base.Model):
    """UserOrder for testing list with expand.

    :ivar id: The user's id. Required.
    :vartype id: int
    :ivar user_id: The user's id. Required.
    :vartype user_id: int
    :ivar detail: The user's order detail. Required.
    :vartype detail: str
    """

    id: int = rest_field(visibility=["read"])
    """The user's id. Required."""
    user_id: int = rest_field(name="userId", visibility=["read", "create", "update", "delete", "query"])
    """The user's id. Required."""
    detail: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The user's order detail. Required."""

    @overload
    def __init__(
        self,
        *,
        user_id: int,
        detail: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
