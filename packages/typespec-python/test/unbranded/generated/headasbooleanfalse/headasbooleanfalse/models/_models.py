# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Dict, List, Mapping, Optional, overload

from .._utils.model_base import Model as _Model, rest_field


class ReadOnlyModel(_Model):
    """RoundTrip model with readonly optional properties.

    :ivar optional_nullable_int_list: Optional readonly nullable int list.
    :vartype optional_nullable_int_list: list[int]
    :ivar optional_string_record: Optional readonly string dictionary.
    :vartype optional_string_record: dict[str, str]
    """

    optional_nullable_int_list: Optional[List[int]] = rest_field(name="optionalNullableIntList", visibility=["read"])
    """Optional readonly nullable int list."""
    optional_string_record: Optional[Dict[str, str]] = rest_field(name="optionalStringRecord", visibility=["read"])
    """Optional readonly string dictionary."""


class VisibilityModel(_Model):
    """Output model with visibility properties.

    :ivar read_prop: Required string, illustrating a readonly property. Required.
    :vartype read_prop: str
    :ivar query_prop: Required int32, illustrating a query property. Required.
    :vartype query_prop: int
    :ivar create_prop: Required string[], illustrating a create property. Required.
    :vartype create_prop: list[str]
    :ivar update_prop: Required int32[], illustrating a update property. Required.
    :vartype update_prop: list[int]
    :ivar delete_prop: Required bool, illustrating a delete property. Required.
    :vartype delete_prop: bool
    """

    read_prop: str = rest_field(name="readProp", visibility=["read"])
    """Required string, illustrating a readonly property. Required."""
    query_prop: int = rest_field(name="queryProp", visibility=["query"])
    """Required int32, illustrating a query property. Required."""
    create_prop: List[str] = rest_field(name="createProp", visibility=["create"])
    """Required string[], illustrating a create property. Required."""
    update_prop: List[int] = rest_field(name="updateProp", visibility=["update"])
    """Required int32[], illustrating a update property. Required."""
    delete_prop: bool = rest_field(name="deleteProp", visibility=["delete"])
    """Required bool, illustrating a delete property. Required."""

    @overload
    def __init__(
        self,
        *,
        query_prop: int,
        create_prop: List[str],
        update_prop: List[int],
        delete_prop: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
