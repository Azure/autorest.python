# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class ExportedUser(_model_base.Model):
    """The exported user data.

    :ivar name: The name of user. Required.
    :vartype name: str
    :ivar resource_uri: The exported URI. Required.
    :vartype resource_uri: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The name of user. Required."""
    resource_uri: str = rest_field(name="resourceUri", visibility=["read", "create", "update", "delete", "query"])
    """The exported URI. Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        resource_uri: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class User(_model_base.Model):
    """Details about a user.

    :ivar name: The name of user. Required.
    :vartype name: str
    :ivar role: The role of user. Required.
    :vartype role: str
    """

    name: str = rest_field(visibility=["read"])
    """The name of user. Required."""
    role: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """The role of user. Required."""

    @overload
    def __init__(
        self,
        *,
        role: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
