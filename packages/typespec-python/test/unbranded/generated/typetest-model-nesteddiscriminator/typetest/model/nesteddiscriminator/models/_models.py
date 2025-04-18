# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Dict, List, Literal, Mapping, Optional, TYPE_CHECKING, overload

from .._utils.model_base import Model as _Model, rest_discriminator, rest_field

if TYPE_CHECKING:
    from .. import models as _models


class Fish(_Model):
    """This is base model for polymorphic multiple levels inheritance with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Salmon, Shark

    :ivar kind: Discriminator property for Fish. Required. Default value is None.
    :vartype kind: str
    :ivar age: Required.
    :vartype age: int
    """

    __mapping__: Dict[str, _Model] = {}
    kind: str = rest_discriminator(name="kind")
    """Discriminator property for Fish. Required. Default value is None."""
    age: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
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


class Shark(Fish, discriminator="shark"):
    """The second level model in polymorphic multiple levels inheritance and it defines a new
    discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    GoblinShark, SawShark

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar sharktype: Required. Default value is None.
    :vartype sharktype: str
    """

    __mapping__: Dict[str, _Model] = {}
    kind: Literal["shark"] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"shark\"."""
    sharktype: str = rest_discriminator(name="sharktype", visibility=["read", "create", "update", "delete", "query"])
    """Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        age: int,
        sharktype: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="shark", **kwargs)


class GoblinShark(Shark, discriminator="goblin"):
    """The third level model GoblinShark in polymorphic multiple levels inheritance.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar sharktype: Required. Default value is "goblin".
    :vartype sharktype: str
    """

    __mapping__: Dict[str, _Model] = {}
    sharktype: Literal["goblin"] = rest_discriminator(name="sharktype", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"goblin\"."""

    @overload
    def __init__(
        self,
        *,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, sharktype="goblin", **kwargs)


class Salmon(Fish, discriminator="salmon"):
    """The second level model in polymorphic multiple levels inheritance which contains references to
    other polymorphic instances.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "salmon".
    :vartype kind: str
    :ivar friends:
    :vartype friends: list[~typetest.model.nesteddiscriminator.models.Fish]
    :ivar hate:
    :vartype hate: dict[str, ~typetest.model.nesteddiscriminator.models.Fish]
    :ivar partner:
    :vartype partner: ~typetest.model.nesteddiscriminator.models.Fish
    """

    kind: Literal["salmon"] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"salmon\"."""
    friends: Optional[List["_models.Fish"]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    hate: Optional[Dict[str, "_models.Fish"]] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    partner: Optional["_models.Fish"] = rest_field(visibility=["read", "create", "update", "delete", "query"])

    @overload
    def __init__(
        self,
        *,
        age: int,
        friends: Optional[List["_models.Fish"]] = None,
        hate: Optional[Dict[str, "_models.Fish"]] = None,
        partner: Optional["_models.Fish"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="salmon", **kwargs)


class SawShark(Shark, discriminator="saw"):
    """The third level model SawShark in polymorphic multiple levels inheritance.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar sharktype: Required. Default value is "saw".
    :vartype sharktype: str
    """

    __mapping__: Dict[str, _Model] = {}
    sharktype: Literal["saw"] = rest_discriminator(name="sharktype", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """Required. Default value is \"saw\"."""

    @overload
    def __init__(
        self,
        *,
        age: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, sharktype="saw", **kwargs)
