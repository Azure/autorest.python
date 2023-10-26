# coding=utf-8
# pylint: disable=too-many-lines


import sys
from typing import Any, Dict, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_discriminator, rest_field

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Fish(_model_base.Model):
    """This is base model for polymorphic multiple levels inheritance with a discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Salmon, Shark

    All required parameters must be populated in order to send to Azure.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is None.
    :vartype kind: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    age: int = rest_field()
    """Required."""
    kind: Literal[None] = rest_discriminator(name="kind")
    """Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        age: int,
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


class Shark(Fish, discriminator="shark"):
    """The second level model in polymorphic multiple levels inheritance and it defines a new
    discriminator.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    GoblinShark, SawShark

    All required parameters must be populated in order to send to Azure.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar sharktype: Required. Default value is None.
    :vartype sharktype: str
    """

    __mapping__: Dict[str, _model_base.Model] = {}
    kind: Literal["shark"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"shark\"."""
    sharktype: Literal[None] = rest_discriminator(name="sharktype")
    """Required. Default value is None."""

    @overload
    def __init__(
        self,
        *,
        age: int,
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
        self.kind: Literal["shark"] = "shark"
        self.sharktype: Literal[None] = None


class GoblinShark(Shark, discriminator="goblin"):
    """The third level model GoblinShark in polymorphic multiple levels inheritance.

    All required parameters must be populated in order to send to Azure.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar sharktype: Required. Default value is "goblin".
    :vartype sharktype: str
    """

    sharktype: Literal["goblin"] = rest_discriminator(name="sharktype")  # type: ignore
    """Required. Default value is \"goblin\"."""

    @overload
    def __init__(
        self,
        *,
        age: int,
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
        self.sharktype: Literal["goblin"] = "goblin"


class Salmon(Fish, discriminator="salmon"):
    """The second level model in polymorphic multiple levels inheritance which contains references to
    other polymorphic instances.

    All required parameters must be populated in order to send to Azure.

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

    kind: Literal["salmon"] = rest_discriminator(name="kind")  # type: ignore
    """Required. Default value is \"salmon\"."""
    friends: Optional[List["_models.Fish"]] = rest_field()
    hate: Optional[Dict[str, "_models.Fish"]] = rest_field()
    partner: Optional["_models.Fish"] = rest_field()

    @overload
    def __init__(
        self,
        *,
        age: int,
        friends: Optional[List["_models.Fish"]] = None,
        hate: Optional[Dict[str, "_models.Fish"]] = None,
        partner: Optional["_models.Fish"] = None,
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
        self.kind: Literal["salmon"] = "salmon"


class SawShark(Shark, discriminator="saw"):
    """The third level model SawShark in polymorphic multiple levels inheritance.

    All required parameters must be populated in order to send to Azure.

    :ivar age: Required.
    :vartype age: int
    :ivar kind: Required. Default value is "shark".
    :vartype kind: str
    :ivar sharktype: Required. Default value is "saw".
    :vartype sharktype: str
    """

    sharktype: Literal["saw"] = rest_discriminator(name="sharktype")  # type: ignore
    """Required. Default value is \"saw\"."""

    @overload
    def __init__(
        self,
        *,
        age: int,
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
        self.sharktype: Literal["saw"] = "saw"
