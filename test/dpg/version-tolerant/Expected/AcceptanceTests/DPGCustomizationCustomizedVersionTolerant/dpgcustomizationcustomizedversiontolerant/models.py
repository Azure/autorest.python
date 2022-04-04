# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any


class Input(dict[str, Any]):
    """Input.

    :ivar hello: Required.
    :vartype hello: str
    """

    @property
    def hello(self) -> str:
        return self.__getitem__("hello")

    @hello.setter
    def hello(self, val: str) -> None:
        self.__setitem__("hello", val)

    def __init__(self, *, hello: str, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(hello=hello, **kwargs)


class Product(dict[str, Any]):
    """Product.

    :ivar received: Required. Possible values include: "raw", "model".
    :vartype received: str or ~dpgcustomizationcustomizedversiontolerant.models.ProductReceived
    """

    @property
    def received(self) -> str:
        return self.__getitem__("received")

    @received.setter
    def received(self, val: str) -> None:
        self.__setitem__("received", val)

    def __init__(self, *, received: str, **kwargs):  # pylint: disable=useless-super-delegation
        super().__init__(received=received, **kwargs)


class LROProduct(Product):
    """LROProduct.

    :ivar received: Required. Possible values include: "raw", "model".
    :vartype received: str or ~dpgcustomizationcustomizedversiontolerant.models.ProductReceived
    :ivar provisioning_state: Required.
    :vartype provisioning_state: str
    """

    @property
    def provisioning_state(self) -> str:
        return self.__getitem__("provisioningState")

    @provisioning_state.setter
    def provisioning_state(self, val: str) -> None:
        self.__setitem__("provisioningState", val)

    def __init__(self, *, received: str, provisioning_state: str, **kwargs):
        super().__init__(received=received, provisioningState=provisioning_state, **kwargs)

    @classmethod
    def _from_dict(cls, **kwargs):
        return cls(received=kwargs.pop("received"), provisioning_state=kwargs.pop("provisioningState"), **kwargs)
