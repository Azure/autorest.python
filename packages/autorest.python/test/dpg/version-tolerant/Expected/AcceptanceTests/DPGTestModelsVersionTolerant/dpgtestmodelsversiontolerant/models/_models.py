# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Input(_serialization.Model):
    """Input.

    All required parameters must be populated in order to send to Azure.

    :ivar hello: Required.
    :vartype hello: str
    """

    _validation = {
        "hello": {"required": True},
    }

    _attribute_map = {
        "hello": {"key": "hello", "type": "str"},
    }

    def __init__(self, *, hello: str, **kwargs: Any) -> None:
        """
        :keyword hello: Required.
        :paramtype hello: str
        """
        super().__init__(**kwargs)
        self.hello = hello


class Product(_serialization.Model):
    """Product.

    All required parameters must be populated in order to send to Azure.

    :ivar received: Required. Known values are: "raw" and "model".
    :vartype received: str or ~dpgtestmodelsversiontolerant.models.ProductReceived
    """

    _validation = {
        "received": {"required": True},
    }

    _attribute_map = {
        "received": {"key": "received", "type": "str"},
    }

    def __init__(self, *, received: Union[str, "_models.ProductReceived"], **kwargs: Any) -> None:
        """
        :keyword received: Required. Known values are: "raw" and "model".
        :paramtype received: str or ~dpgtestmodelsversiontolerant.models.ProductReceived
        """
        super().__init__(**kwargs)
        self.received = received


class LROProduct(Product):
    """LROProduct.

    All required parameters must be populated in order to send to Azure.

    :ivar received: Required. Known values are: "raw" and "model".
    :vartype received: str or ~dpgtestmodelsversiontolerant.models.ProductReceived
    :ivar provisioning_state: Required.
    :vartype provisioning_state: str
    """

    _validation = {
        "received": {"required": True},
        "provisioning_state": {"required": True},
    }

    _attribute_map = {
        "received": {"key": "received", "type": "str"},
        "provisioning_state": {"key": "provisioningState", "type": "str"},
    }

    def __init__(
        self, *, received: Union[str, "_models.ProductReceived"], provisioning_state: str, **kwargs: Any
    ) -> None:
        """
        :keyword received: Required. Known values are: "raw" and "model".
        :paramtype received: str or ~dpgtestmodelsversiontolerant.models.ProductReceived
        :keyword provisioning_state: Required.
        :paramtype provisioning_state: str
        """
        super().__init__(received=received, **kwargs)
        self.provisioning_state = provisioning_state


class ProductResult(_serialization.Model):
    """ProductResult.

    :ivar values:
    :vartype values: list[~dpgtestmodelsversiontolerant.models.Product]
    :ivar next_link:
    :vartype next_link: str
    """

    _attribute_map = {
        "values": {"key": "values", "type": "[Product]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, values: Optional[List["_models.Product"]] = None, next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword values:
        :paramtype values: list[~dpgtestmodelsversiontolerant.models.Product]
        :keyword next_link:
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.values = values
        self.next_link = next_link
