# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Dict, List, Literal, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field

if TYPE_CHECKING:
    from .. import models as _models


class Bird(_model_base.Model):
    """This is base model for polymorphic single level inheritance with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Eagle, Goose, SeaGull, Sparrow


    :ivar kind: Required. Default value is None.
    :vartype kind: str
    :ivar wingspan: Required.
    :vartype wingspan: int
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    kind: str = rest_discriminator(name="kind")
    """Required. Default value is None."""
    wingspan: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
        wingspan: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Dinosaur(_model_base.Model):
    """Define a base class in the legacy way. Discriminator property is not explicitly defined in the
    model.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    TRex


    :ivar kind: Discriminator property for Dinosaur. Required. Default value is None.
    :vartype kind: str
    :ivar size: Required.
    :vartype size: int
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    kind: str = rest_discriminator(name="kind")
    """Discriminator property for Dinosaur. Required. Default value is None."""
    size: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        kind: str,
        size: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class Eagle(Bird, discriminator="eagle"):
    """The second level model in polymorphic single levels inheritance which contains references to
    other polymorphic instances.


    :ivar wingspan: Required.
    :vartype wingspan: int
    :ivar kind: Required. Default value is "eagle".
    :vartype kind: str
    :ivar friends:
    :vartype friends: list[~typetest.model.singlediscriminator.models.Bird]
    :ivar hate:
    :vartype hate: dict[str, ~typetest.model.singlediscriminator.models.Bird]
    :ivar partner:
    :vartype partner: ~typetest.model.singlediscriminator.models.Bird
    """

    kind: Literal["eagle"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"eagle\"."""
    friends: Optional[List["_models.Bird"]] = rest_field()
    hate: Optional[Dict[str, "_models.Bird"]] = rest_field()
    partner: Optional["_models.Bird"] = rest_field()

    @overload
    def __init__(
        self,
        *,
        wingspan: int,
        friends: Optional[List["_models.Bird"]] = None,
        hate: Optional[Dict[str, "_models.Bird"]] = None,
        partner: Optional["_models.Bird"] = None,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="eagle", **kwargs)


class Goose(Bird, discriminator="goose"):
    """The second level model in polymorphic single level inheritance.


    :ivar wingspan: Required.
    :vartype wingspan: int
    :ivar kind: Required. Default value is "goose".
    :vartype kind: str
    """

    kind: Literal["goose"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"goose\"."""

    @overload
    def __init__(
        self,
        *,
        wingspan: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="goose", **kwargs)


class SeaGull(Bird, discriminator="seagull"):
    """The second level model in polymorphic single level inheritance.


    :ivar wingspan: Required.
    :vartype wingspan: int
    :ivar kind: Required. Default value is "seagull".
    :vartype kind: str
    """

    kind: Literal["seagull"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"seagull\"."""

    @overload
    def __init__(
        self,
        *,
        wingspan: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="seagull", **kwargs)


class Sparrow(Bird, discriminator="sparrow"):
    """The second level model in polymorphic single level inheritance.


    :ivar wingspan: Required.
    :vartype wingspan: int
    :ivar kind: Required. Default value is "sparrow".
    :vartype kind: str
    """

    kind: Literal["sparrow"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"sparrow\"."""

    @overload
    def __init__(
        self,
        *,
        wingspan: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="sparrow", **kwargs)


class TRex(Dinosaur, discriminator="t-rex"):
    """The second level legacy model in polymorphic single level inheritance.


    :ivar size: Required.
    :vartype size: int
    :ivar kind: Required. Default value is "t-rex".
    :vartype kind: str
    """

    kind: Literal["t-rex"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"t-rex\"."""

    @overload
    def __init__(
        self,
        *,
        size: int,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, kind="t-rex", **kwargs)
