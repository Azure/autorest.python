# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, Dict, Mapping, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field
from ._enums import DogKind, SnakeKind

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports


class Snake(_model_base.Model):
    """Test fixed enum type for discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Cobra

    All required parameters must be populated in order to send to server.

    :ivar kind: discriminator property. Required. "cobra"
    :vartype kind: str or ~typetest.model.enumdiscriminator.models.SnakeKind
    :ivar length: Length of the snake. Required.
    :vartype length: int
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    kind: Literal[None] = rest_discriminator(name="kind")
    """discriminator property. Required. \"cobra\""""
    length: int = rest_field()
    """Length of the snake. Required."""

    @overload
    def __init__(
        self,
        *,
        length: int,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal[None] = None


class Cobra(Snake, discriminator="cobra"):
    """Cobra model.

    All required parameters must be populated in order to send to server.

    :ivar length: Length of the snake. Required.
    :vartype length: int
    :ivar kind: discriminator property. Required. Species cobra
    :vartype kind: str or ~typetest.model.enumdiscriminator.models.COBRA
    """

    kind: Literal[SnakeKind.COBRA] = rest_discriminator(name="kind")  # type: ignore
    """discriminator property. Required. Species cobra"""

    @overload
    def __init__(
        self,
        *,
        length: int,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal[SnakeKind.COBRA] = SnakeKind.COBRA


class Dog(_model_base.Model):
    """Test extensible enum type for discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Golden

    All required parameters must be populated in order to send to server.

    :ivar kind: discriminator property. Required. "golden"
    :vartype kind: str or ~typetest.model.enumdiscriminator.models.DogKind
    :ivar weight: Weight of the dog. Required.
    :vartype weight: int
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    kind: Literal[None] = rest_discriminator(name="kind")
    """discriminator property. Required. \"golden\""""
    weight: int = rest_field()
    """Weight of the dog. Required."""

    @overload
    def __init__(
        self,
        *,
        weight: int,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal[None] = None


class Golden(Dog, discriminator="golden"):
    """Golden dog model.

    All required parameters must be populated in order to send to server.

    :ivar weight: Weight of the dog. Required.
    :vartype weight: int
    :ivar kind: discriminator property. Required. Species golden
    :vartype kind: str or ~typetest.model.enumdiscriminator.models.GOLDEN
    """

    kind: Literal[DogKind.GOLDEN] = rest_discriminator(name="kind")  # type: ignore
    """discriminator property. Required. Species golden"""

    @overload
    def __init__(
        self,
        *,
        weight: int,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.kind: Literal[DogKind.GOLDEN] = DogKind.GOLDEN
