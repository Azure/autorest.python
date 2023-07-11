# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class InternalIncludeModel(_model_base.Model):
    """This is a model only used by internal operation. Also, it is decorated with @include. It should
    be generated and exported.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    :ivar nested: Required.
    :vartype nested: ~_specs_.azure.clientgenerator.core.internal.models.NestedIncludeModel
    """

    name: str = rest_field()
    """Required."""
    nested: "_models._models.NestedIncludeModel" = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
        nested: "_models._models.NestedIncludeModel",
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


class InternalModel(_model_base.Model):
    """This is a model only used by internal operation. It should be generated but not exported.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""


class NestedIncludeModel(_model_base.Model):
    """This is a model referred by model decorated with @include. It should be generated and exported.

    All required parameters must be populated in order to send to Azure.

    :ivar comment: Required.
    :vartype comment: str
    """

    comment: str = rest_field()
    """Required."""


class PublicModel(_model_base.Model):
    """This is a model only used by public operation. It should be generated and exported.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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


class SharedModel(_model_base.Model):
    """This is a model used by both public and internal operation. It should be generated and
    exported.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required.
    :vartype name: str
    """

    name: str = rest_field()
    """Required."""

    @overload
    def __init__(
        self,
        *,
        name: str,
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
