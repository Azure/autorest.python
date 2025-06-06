# coding=utf-8
# pylint: disable=useless-super-delegation

import datetime
import decimal
from typing import Any, Dict, List, Literal, Mapping, TYPE_CHECKING, Union, overload

from .._utils.model_base import Model as _Model, rest_field
from ._enums import ExtendedEnum

if TYPE_CHECKING:
    from .. import models as _models


class BooleanLiteralProperty(_Model):
    """Model with a boolean literal property.

    :ivar property: Property. Required. Default value is True.
    :vartype property: bool
    """

    property: Literal[True] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required. Default value is True."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.property: Literal[True] = True


class BooleanProperty(_Model):
    """Model with a boolean property.

    :ivar property: Property. Required.
    :vartype property: bool
    """

    property: bool = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: bool,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class BytesProperty(_Model):
    """Model with a bytes property.

    :ivar property: Property. Required.
    :vartype property: bytes
    """

    property: bytes = rest_field(visibility=["read", "create", "update", "delete", "query"], format="base64")
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: bytes,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CollectionsIntProperty(_Model):
    """Model with collection int properties.

    :ivar property: Property. Required.
    :vartype property: list[int]
    """

    property: List[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: List[int],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CollectionsModelProperty(_Model):
    """Model with collection model properties.

    :ivar property: Property. Required.
    :vartype property: list[~typetest.property.valuetypes.models.InnerModel]
    """

    property: List["_models.InnerModel"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: List["_models.InnerModel"],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class CollectionsStringProperty(_Model):
    """Model with collection string properties.

    :ivar property: Property. Required.
    :vartype property: list[str]
    """

    property: List[str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: List[str],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DatetimeProperty(_Model):
    """Model with a datetime property.

    :ivar property: Property. Required.
    :vartype property: ~datetime.datetime
    """

    property: datetime.datetime = rest_field(
        visibility=["read", "create", "update", "delete", "query"], format="rfc3339"
    )
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: datetime.datetime,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Decimal128Property(_Model):
    """Model with a decimal128 property.

    :ivar property: Property. Required.
    :vartype property: ~decimal.Decimal
    """

    property: decimal.Decimal = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: decimal.Decimal,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DecimalProperty(_Model):
    """Model with a decimal property.

    :ivar property: Property. Required.
    :vartype property: ~decimal.Decimal
    """

    property: decimal.Decimal = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: decimal.Decimal,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DictionaryStringProperty(_Model):
    """Model with dictionary string properties.

    :ivar property: Property. Required.
    :vartype property: dict[str, str]
    """

    property: Dict[str, str] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Dict[str, str],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class DurationProperty(_Model):
    """Model with a duration property.

    :ivar property: Property. Required.
    :vartype property: ~datetime.timedelta
    """

    property: datetime.timedelta = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: datetime.timedelta,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class EnumProperty(_Model):
    """Model with enum properties.

    :ivar property: Property. Required. Known values are: "ValueOne" and "ValueTwo".
    :vartype property: str or ~typetest.property.valuetypes.models.FixedInnerEnum
    """

    property: Union[str, "_models.FixedInnerEnum"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Property. Required. Known values are: \"ValueOne\" and \"ValueTwo\"."""

    @overload
    def __init__(
        self,
        *,
        property: Union[str, "_models.FixedInnerEnum"],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ExtensibleEnumProperty(_Model):
    """Model with extensible enum properties.

    :ivar property: Property. Required. Known values are: "ValueOne" and "ValueTwo".
    :vartype property: str or ~typetest.property.valuetypes.models.InnerEnum
    """

    property: Union[str, "_models.InnerEnum"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required. Known values are: \"ValueOne\" and \"ValueTwo\"."""

    @overload
    def __init__(
        self,
        *,
        property: Union[str, "_models.InnerEnum"],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class FloatLiteralProperty(_Model):
    """Model with a float literal property.

    :ivar property: Property. Required. Default value is 43.125.
    :vartype property: float
    """

    property: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required. Default value is 43.125."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.property: float = 43.125


class FloatProperty(_Model):
    """Model with a float property.

    :ivar property: Property. Required.
    :vartype property: float
    """

    property: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: float,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class InnerModel(_Model):
    """Inner model. Will be a property type for ModelWithModelProperties.

    :ivar property: Required string property. Required.
    :vartype property: str
    """

    property: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required string property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class IntLiteralProperty(_Model):
    """Model with a int literal property.

    :ivar property: Property. Required. Default value is 42.
    :vartype property: int
    """

    property: Literal[42] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required. Default value is 42."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.property: Literal[42] = 42


class IntProperty(_Model):
    """Model with a int property.

    :ivar property: Property. Required.
    :vartype property: int
    """

    property: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: int,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ModelProperty(_Model):
    """Model with model properties.

    :ivar property: Property. Required.
    :vartype property: ~typetest.property.valuetypes.models.InnerModel
    """

    property: "_models.InnerModel" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: "_models.InnerModel",  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class NeverProperty(_Model):
    """Model with a property never. (This property should not be included)."""


class StringLiteralProperty(_Model):
    """Model with a string literal property.

    :ivar property: Property. Required. Default value is "hello".
    :vartype property: str
    """

    property: Literal["hello"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required. Default value is \"hello\"."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.property: Literal["hello"] = "hello"


class StringProperty(_Model):
    """Model with a string property.

    :ivar property: Property. Required.
    :vartype property: str
    """

    property: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: str,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnionEnumValueProperty(_Model):
    """Template type for testing models with specific properties. Pass in the type of the property you
    are looking for.

    :ivar property: Property. Required.
    :vartype property: str or ~typetest.property.valuetypes.models.ENUM_VALUE2
    """

    property: Literal[ExtendedEnum.ENUM_VALUE2] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Literal[ExtendedEnum.ENUM_VALUE2],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnionFloatLiteralProperty(_Model):
    """Model with a union of float literal as property.

    :ivar property: Property. Required. Is one of the following types: float
    :vartype property: float or float
    """

    property: float = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required. Is one of the following types: float"""

    @overload
    def __init__(
        self,
        *,
        property: float,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnionIntLiteralProperty(_Model):
    """Model with a union of int literal as property.

    :ivar property: Property. Required. Is either a Literal[42] type or a Literal[43] type.
    :vartype property: int or int
    """

    property: Literal[42, 43] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required. Is either a Literal[42] type or a Literal[43] type."""

    @overload
    def __init__(
        self,
        *,
        property: Literal[42, 43],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnionStringLiteralProperty(_Model):
    """Model with a union of string literal as property.

    :ivar property: Property. Required. Is either a Literal["hello"] type or a Literal["world"]
     type.
    :vartype property: str or str
    """

    property: Literal["hello", "world"] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required. Is either a Literal[\"hello\"] type or a Literal[\"world\"] type."""

    @overload
    def __init__(
        self,
        *,
        property: Literal["hello", "world"],  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnknownArrayProperty(_Model):
    """Model with a property unknown, and the data is an array.

    :ivar property: Property. Required.
    :vartype property: any
    """

    property: Any = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Any,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnknownDictProperty(_Model):
    """Model with a property unknown, and the data is a dictionnary.

    :ivar property: Property. Required.
    :vartype property: any
    """

    property: Any = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Any,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnknownIntProperty(_Model):
    """Model with a property unknown, and the data is a int32.

    :ivar property: Property. Required.
    :vartype property: any
    """

    property: Any = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Any,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class UnknownStringProperty(_Model):
    """Model with a property unknown, and the data is a string.

    :ivar property: Property. Required.
    :vartype property: any
    """

    property: Any = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Property. Required."""

    @overload
    def __init__(
        self,
        *,
        property: Any,  # pylint: disable=redefined-builtin
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
