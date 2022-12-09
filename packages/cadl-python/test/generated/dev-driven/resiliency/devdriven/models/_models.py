# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class CustomPageProduct(_model_base.Model):
    """Paged collection of Product items.

    All required parameters must be populated in order to send to Azure.

    :ivar value: The Product items on this page. Required.
    :vartype value: list[~resiliency.devdriven.models.Product]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    value: List["_models.Product"] = rest_field()
    """The Product items on this page. Required. """
    next_link: Optional[str] = rest_field(name="nextLink")
    """The link to the next page of items. """

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Input(_model_base.Model):
    """Input to LRO call.

    All required parameters must be populated in order to send to Azure.

    :ivar hello: property on the input. Required.
    :vartype hello: str
    """

    hello: str = rest_field()
    """property on the input. Required. """

    @overload
    def __init__(
        self,
        *,
        hello: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Product(_model_base.Model):
    """Product resource.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar key: key of product. Required.
    :vartype key: str
    :ivar received: received mode. Required. Known values are: "raw" and "model".
    :vartype received: str or ~resiliency.devdriven.models.Mode
    """

    key: str = rest_field(readonly=True)
    """key of product. Required. """
    received: Union[str, "_models.Mode"] = rest_field()
    """received mode. Required. Known values are: \"raw\" and \"model\"."""

    @overload
    def __init__(
        self,
        *,
        received: Union[str, "_models.Mode"],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class LroProduct(Product):
    """Final response from LRO call.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar key: key of product. Required.
    :vartype key: str
    :ivar received: received mode. Required. Known values are: "raw" and "model".
    :vartype received: str or ~resiliency.devdriven.models.Mode
    :ivar provisioning_state: Provisioning state returned by the service. Required.
    :vartype provisioning_state: str
    """

    provisioning_state: str = rest_field(name="provisioningState")
    """Provisioning state returned by the service. Required. """

    @overload
    def __init__(
        self,
        *,
        received: Union[str, "_models.Mode"],
        provisioning_state: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """
        ...

    def __init__(self, *args, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
