# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class ChildFlattenModel(_model_base.Model):
    """This is the child model to be flattened. And it has flattened property as well.

    :ivar summary: Required.
    :vartype summary: str
    :ivar properties: Required.
    :vartype properties: ~specs.azure.clientgenerator.core.flattenproperty.models.ChildModel
    """

    summary: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    properties: "_models.ChildModel" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    __flattened_items = ["description", "age"]

    @overload
    def __init__(
        self,
        *,
        summary: str,
        properties: "_models.ChildModel",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        _flattened_input = {k: kwargs.pop(k) for k in kwargs.keys() & self.__flattened_items}
        super().__init__(*args, **kwargs)
        for k, v in _flattened_input.items():
            setattr(self, k, v)

    def __getattr__(self, name: str) -> Any:
        if name in self.__flattened_items:
            if self.properties is None:
                return None
            return getattr(self.properties, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.__flattened_items:
            if self.properties is None:
                self.properties = self._attr_to_rest_field["properties"]._class_type()
            setattr(self.properties, key, value)
        else:
            super().__setattr__(key, value)


class ChildModel(_model_base.Model):
    """This is the child model to be flattened.

    :ivar description: Required.
    :vartype description: str
    :ivar age: Required.
    :vartype age: int
    """

    description: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    age: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        description: str,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FlattenModel(_model_base.Model):
    """This is the model with one level of flattening.

    :ivar name: Required.
    :vartype name: str
    :ivar properties: Required.
    :vartype properties: ~specs.azure.clientgenerator.core.flattenproperty.models.ChildModel
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    properties: "_models.ChildModel" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    __flattened_items = ["description", "age"]

    @overload
    def __init__(
        self,
        *,
        name: str,
        properties: "_models.ChildModel",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        _flattened_input = {k: kwargs.pop(k) for k in kwargs.keys() & self.__flattened_items}
        super().__init__(*args, **kwargs)
        for k, v in _flattened_input.items():
            setattr(self, k, v)

    def __getattr__(self, name: str) -> Any:
        if name in self.__flattened_items:
            if self.properties is None:
                return None
            return getattr(self.properties, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __setattr__(self, key: str, value: Any) -> None:
        if key in self.__flattened_items:
            if self.properties is None:
                self.properties = self._attr_to_rest_field["properties"]._class_type()
            setattr(self.properties, key, value)
        else:
            super().__setattr__(key, value)


class NestedFlattenModel(_model_base.Model):
    """This is the model with two levels of flattening.

    :ivar name: Required.
    :vartype name: str
    :ivar properties: Required.
    :vartype properties: ~specs.azure.clientgenerator.core.flattenproperty.models.ChildFlattenModel
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    properties: "_models.ChildFlattenModel" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        properties: "_models.ChildFlattenModel",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
