# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Element(_model_base.Model):
    """element.

    :ivar extension:
    :vartype extension: list[~type.model.inheritance.recursive.models.Extension]
    """

    extension: Optional[List["_models.Extension"]] = rest_field()

    @overload
    def __init__(
        self,
        *,
        extension: Optional[List["_models.Extension"]] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Extension(Element):
    """extension.

    All required parameters must be populated in order to send to server.

    :ivar extension:
    :vartype extension: list[~type.model.inheritance.recursive.models.Extension]
    :ivar level: Required.
    :vartype level: int
    """

    level: int = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        level: int,
        extension: Optional[List["_models.Extension"]] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
