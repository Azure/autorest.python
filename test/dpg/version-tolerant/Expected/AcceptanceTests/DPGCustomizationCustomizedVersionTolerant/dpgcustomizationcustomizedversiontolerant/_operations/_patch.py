# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from typing import Any, overload, Union, TYPE_CHECKING
from azure.core.paging import ItemPaged
from azure.core.polling import LROPoller
from ..models import *  # pylint: disable=wildcard-import,unused-wildcard-import
from ._operations import DPGClientOperationsMixin as DPGClientOperationsMixinGenerated, JSONType

if TYPE_CHECKING:
    from typing import Literal


def mode_checks(*args, **kwargs: Any) -> bool:
    """Return whether model_mode is True"""
    if args:
        return args[0] == "model"
    if "mode" in kwargs:
        return kwargs["mode"] == "model"
    raise ValueError("You need to specify 'mode' equal to 'raw' or 'model'.")


class DPGClientOperationsMixin(DPGClientOperationsMixinGenerated):
    @overload
    def get_model(self, mode: "Literal['raw']", **kwargs: Any) -> JSONType:
        """Pass in mode='raw' to get raw JSON out"""

    @overload
    def get_model(self, mode: "Literal['model']", **kwargs: Any) -> Product:
        """Pass in mode='model' to get a handwritten model out"""

    @overload
    def get_model(self, mode: str, **kwargs: Any):
        """Pass in other modes"""
        raise Exception("No Implementation")

    def get_model(self, *args, **kwargs: Any) -> Union[JSONType, Product]:
        model_mode = mode_checks(*args, **kwargs)
        response = super().get_model(*args, **kwargs)
        if model_mode:
            return Product.deserialize(response)
        return response

    @overload
    def post_model(self, mode: "Literal['raw']", input: JSONType, **kwargs: Any) -> JSONType:
        """Pass in mode='raw' to pass in raw json"""

    @overload
    def post_model(self, mode: "Literal['model']", input: Input, **kwargs: Any) -> Product:
        """Pass in mode='model' to pass in model"""

    @overload
    def post_model(self, mode: str, input: Input, **kwargs: Any):
        """Pass in other modes"""
        raise Exception("No Implementation")

    def post_model(self, *args, **kwargs: Any) -> JSONType:
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            if len(args) > 1:
                args = list(args)  # type: ignore
                args[1] = Input.serialize(args[1])  # type: ignore  # pylint: disable=expression-not-assigned
            else:
                kwargs["input"] == Input.serialize(kwargs["input"])  # pylint: disable=expression-not-assigned
        response = super().post_model(*args, **kwargs)
        if model_mode:
            return Product.deserialize(response)
        return response

    @overload
    def get_pages(self, mode: "Literal['raw']", **kwargs) -> ItemPaged[JSONType]:
        """Pass in mode='raw' to pass for raw json"""

    @overload
    def get_pages(self, mode: "Literal['model']", **kwargs) -> ItemPaged[Product]:
        """Pass in mode='model' to pass for raw json"""

    @overload
    def get_pages(self, mode: str, **kwargs: Any):
        """Pass in other modes"""
        raise Exception("No Implementation")

    def get_pages(self, *args, **kwargs):
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            kwargs["cls"] = lambda objs: [Product.deserialize(x) for x in objs]
        return super().get_pages(*args, **kwargs)

    @overload
    def begin_lro(self, mode: "Literal['raw']", **kwargs) -> LROPoller[JSONType]:
        """Pass in mode='raw' to pass for raw json"""

    @overload
    def begin_lro(self, mode: "Literal['model']", **kwargs) -> LROPoller[LROProduct]:
        """Pass in mode='model' to pass for raw json"""

    @overload
    def begin_lro(self, mode: str, **kwargs: Any):
        """Pass in other modes"""
        raise Exception("No Implementation")

    def begin_lro(self, *args, **kwargs: Any):
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            kwargs["cls"] = lambda pipeline_response, deserialized, headers: LROProduct.deserialize(pipeline_response)
        return super().begin_lro(*args, **kwargs)


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't otherwise do with the following handwritten customizations framework
    aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__ = [
    "DPGClientOperationsMixin"
]  # only add objects you want to be publicly available to your users at your package level
