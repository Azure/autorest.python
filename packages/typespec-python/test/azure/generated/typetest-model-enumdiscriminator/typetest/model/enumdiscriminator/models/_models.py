# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
None
# pylint: disable=useless-super-delegation

from typing import Any, Dict, Literal, Mapping, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field
from ._enums import DogKind, SnakeKind


class Snake(_model_base.Model):
    """Test fixed enum type for discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Cobra

    :ivar kind: discriminator property. Required. "cobra"
    :vartype kind: str or ~typetest.model.enumdiscriminator.models.SnakeKind
    :ivar length: Length of the snake. Required.
    :vartype length: int
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    kind: str = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])
    """discriminator property. Required. \"cobra\""""
    length: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Length of the snake. Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
        length: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Cobra(Snake, discriminator="cobra"):
    """Cobra model.

    :ivar length: Length of the snake. Required.
    :vartype length: int
    :ivar kind: discriminator property. Required. Species cobra
    :vartype kind: str or ~typetest.model.enumdiscriminator.models.COBRA
    """

    kind: Literal[SnakeKind.COBRA] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """discriminator property. Required. Species cobra"""

    @overload
    def __init__(
        self,
        *,
        length: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind=SnakeKind.COBRA, **kwargs)


class Dog(_model_base.Model):
    """Test extensible enum type for discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Golden

    :ivar kind: discriminator property. Required. "golden"
    :vartype kind: str or ~typetest.model.enumdiscriminator.models.DogKind
    :ivar weight: Weight of the dog. Required.
    :vartype weight: int
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    kind: str = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])
    """discriminator property. Required. \"golden\""""
    weight: int = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Weight of the dog. Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
        weight: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Golden(Dog, discriminator="golden"):
    """Golden dog model.

    :ivar weight: Weight of the dog. Required.
    :vartype weight: int
    :ivar kind: discriminator property. Required. Species golden
    :vartype kind: str or ~typetest.model.enumdiscriminator.models.GOLDEN
    """

    kind: Literal[DogKind.GOLDEN] = rest_discriminator(name="kind", visibility=["read", "create", "update", "delete", "query"])  # type: ignore
    """discriminator property. Required. Species golden"""

    @overload
    def __init__(
        self,
        *,
        weight: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind=DogKind.GOLDEN, **kwargs)
