# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Dict, Literal, Mapping, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field

if TYPE_CHECKING:
    from .. import models as _models


class AbstractModel(_model_base.Model):
    """Used in internal operations, should be generated but not exported.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    RealModel

    :ivar kind: Discriminator property for AbstractModel. Required. Default value is None.
    :vartype kind: str
    :ivar name: Required.
    :vartype name: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    kind: str = rest_discriminator(name="kind")
    """Discriminator property for AbstractModel. Required. Default value is None."""
    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class BaseModel(_model_base.Model):
    """Used in internal operations, should be generated but not exported.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class InnerModel(_model_base.Model):
    """Used in internal operations, should be generated but not exported.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class InternalDecoratorModelInInternal(_model_base.Model):
    """Used in an internal operation, should be generated but not exported.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class NoDecoratorModelInInternal(_model_base.Model):
    """Used in an internal operation, should be generated but not exported.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class NoDecoratorModelInPublic(_model_base.Model):
    """Used in a public operation, should be generated and exported.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OuterModel(BaseModel):
    """Used in internal operations, should be generated but not exported.

    :ivar name: Required.
    :vartype name: str
    :ivar inner: Required.
    :vartype inner: ~specs.azure.clientgenerator.core.access.models._models.InnerModel
    """

    inner: "_models._models.InnerModel" = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        inner: "_models._models.InnerModel",
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PublicDecoratorModelInInternal(_model_base.Model):
    """Used in an internal operation but with public decorator, should be generated and exported.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PublicDecoratorModelInPublic(_model_base.Model):
    """Used in a public operation, should be generated and exported.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class RealModel(AbstractModel, discriminator="real"):
    """Used in internal operations, should be generated but not exported.

    :ivar name: Required.
    :vartype name: str
    :ivar kind: Required. Default value is "real".
    :vartype kind: str
    """

    kind: Literal["real"] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"real\"."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="real", **kwargs)


class SharedModel(_model_base.Model):
    """Used by both public and internal operation. It should be generated and exported.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
