# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, Optional, TYPE_CHECKING, overload

from .._utils.model_base import Model as _Model, rest_field

if TYPE_CHECKING:
    from .. import models as _models


class ModelWithArrayOfModel(_Model):
    """Contains an array of models.

    :ivar items_property: Required.
    :vartype items_property: ~payload.xml.models.SimpleModel
    """

    items_property: list["_models.SimpleModel"] = rest_field(
        name="items",
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "SimpleModel", "name": "items", "text": False, "unwrapped": False},
        original_tsp_name=items,
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithArrayOfModel", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        items_property: list["_models.SimpleModel"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithAttributes(_Model):
    """Contains fields that are XML attributes.

    :ivar id1: Required.
    :vartype id1: int
    :ivar id2: Required.
    :vartype id2: str
    :ivar enabled: Required.
    :vartype enabled: bool
    """

    id1: int = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": True, "name": "id1", "text": False, "unwrapped": False},
    )
    """Required."""
    id2: str = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": True, "name": "id2", "text": False, "unwrapped": False},
    )
    """Required."""
    enabled: bool = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "enabled", "text": False, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithAttributes", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        id1: int,
        id2: str,
        enabled: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithDictionary(_Model):
    """Contains a dictionary of key value pairs.

    :ivar metadata: Required.
    :vartype metadata: dict[str, str]
    """

    metadata: dict[str, str] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "metadata", "text": False, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithDictionary", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        metadata: dict[str, str],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithEmptyArray(_Model):
    """Contains an array of models that's supposed to be sent/received as an empty XML element.

    :ivar items_property: Required.
    :vartype items_property: ~payload.xml.models.SimpleModel
    """

    items_property: list["_models.SimpleModel"] = rest_field(
        name="items",
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "SimpleModel", "name": "items", "text": False, "unwrapped": False},
        original_tsp_name=items,
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithEmptyArray", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        items_property: list["_models.SimpleModel"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithEncodedNames(_Model):
    """Uses encodedName instead of Xml.Name which is functionally equivalent.

    :ivar model_data: Required.
    :vartype model_data: ~payload.xml.models.SimpleModel
    :ivar colors: Required.
    :vartype colors: list[str]
    """

    model_data: "_models.SimpleModel" = rest_field(
        name="modelData",
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "SimpleModelData", "text": False, "unwrapped": False},
    )
    """Required."""
    colors: list[str] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "string", "name": "PossibleColors", "text": False, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithEncodedNamesSrc", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        model_data: "_models.SimpleModel",
        colors: list[str],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithOptionalField(_Model):
    """Contains an optional field.

    :ivar item: Required.
    :vartype item: str
    :ivar value:
    :vartype value: int
    """

    item: str = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "item", "text": False, "unwrapped": False},
    )
    """Required."""
    value: Optional[int] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "value", "text": False, "unwrapped": False},
    )

    _xml = {"attribute": False, "name": "ModelWithOptionalField", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        item: str,
        value: Optional[int] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithRenamedArrays(_Model):
    """Contains fields of wrapped and unwrapped arrays of primitive types that have different XML
    representations.

    :ivar colors: Required.
    :vartype colors: list[str]
    :ivar counts: Required.
    :vartype counts: list[int]
    """

    colors: list[str] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "Colors", "name": "Colors", "text": False, "unwrapped": True},
    )
    """Required."""
    counts: list[int] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "int32", "name": "Counts", "text": False, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithRenamedArrays", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        colors: list[str],
        counts: list[int],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithRenamedFields(_Model):
    """Contains fields of the same type that have different XML representation.

    :ivar input_data: Required.
    :vartype input_data: ~payload.xml.models.SimpleModel
    :ivar output_data: Required.
    :vartype output_data: ~payload.xml.models.SimpleModel
    """

    input_data: "_models.SimpleModel" = rest_field(
        name="inputData",
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "InputData", "text": False, "unwrapped": False},
    )
    """Required."""
    output_data: "_models.SimpleModel" = rest_field(
        name="outputData",
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "OutputData", "text": False, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithRenamedFieldsSrc", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        input_data: "_models.SimpleModel",
        output_data: "_models.SimpleModel",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithSimpleArrays(_Model):
    """Contains fields of arrays of primitive types.

    :ivar colors: Required.
    :vartype colors: list[str]
    :ivar counts: Required.
    :vartype counts: list[int]
    """

    colors: list[str] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "string", "name": "colors", "text": False, "unwrapped": False},
    )
    """Required."""
    counts: list[int] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "int32", "name": "counts", "text": False, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithSimpleArrays", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        colors: list[str],
        counts: list[int],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithText(_Model):
    """Contains an attribute and text.

    :ivar language: Required.
    :vartype language: str
    :ivar content: Required.
    :vartype content: str
    """

    language: str = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": True, "name": "language", "text": False, "unwrapped": False},
    )
    """Required."""
    content: str = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "content", "text": True, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithText", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        language: str,
        content: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelWithUnwrappedArray(_Model):
    """Contains fields of wrapped and unwrapped arrays of primitive types.

    :ivar colors: Required.
    :vartype colors: list[str]
    :ivar counts: Required.
    :vartype counts: list[int]
    """

    colors: list[str] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "colors", "name": "colors", "text": False, "unwrapped": True},
    )
    """Required."""
    counts: list[int] = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "itemsName": "int32", "name": "counts", "text": False, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "ModelWithUnwrappedArray", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        colors: list[str],
        counts: list[int],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class SimpleModel(_Model):
    """Contains fields of primitive types.

    :ivar name: Required.
    :vartype name: str
    :ivar age: Required.
    :vartype age: int
    """

    name: str = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "name", "text": False, "unwrapped": False},
    )
    """Required."""
    age: int = rest_field(
        visibility=["read", "create", "update", "delete", "query"],
        xml={"attribute": False, "name": "age", "text": False, "unwrapped": False},
    )
    """Required."""

    _xml = {"attribute": False, "name": "SimpleModel", "text": False, "unwrapped": False}

    @overload
    def __init__(
        self,
        *,
        name: str,
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
