# coding=utf-8
None
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    from .. import models as _models


class InputModel(_model_base.Model):
    """Usage override to roundtrip.

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


class OrphanModel(_model_base.Model):
    """Not used anywhere, but access is override to public so still need to be generated and exported
    with serialization.

    :ivar model_name: Required.
    :vartype model_name: str
    :ivar description: Required.
    :vartype description: str
    """

    model_name: str = rest_field(name="modelName", visibility=["read", "create", "update", "delete", "query"])
    """Required."""
    description: str = rest_field(name="desc", visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        model_name: str,
        description: str,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class OutputModel(_model_base.Model):
    """Usage override to roundtrip.

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


class ResultModel(_model_base.Model):
    """ResultModel.

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


class RoundTripModel(_model_base.Model):
    """RoundTripModel.

    :ivar result: Required.
    :vartype result: ~specs.azure.clientgenerator.core.usage.models.ResultModel
    """

    result: "_models.ResultModel" = rest_field(visibility=["read"])
    """Required."""
