# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from typing import Any, Union, overload, TYPE_CHECKING
from azure.core.polling import AsyncLROPoller
from azure.core.async_paging import AsyncItemPaged

from ._operations import DPGClientOperationsMixin as DPGClientOperationsMixinGenerated, JSONType
from ...models import *  # pylint: disable=wildcard-import,unused-wildcard-import
from ..._operations._patch import mode_checks

if TYPE_CHECKING:
    from typing import Literal


class DPGClientOperationsMixin(DPGClientOperationsMixinGenerated):
    @overload
    async def get_model(self, mode: "Literal['raw']", **kwargs: Any) -> JSONType:
        """Pass in mode='raw' to get raw JSON out"""

    @overload
    async def get_model(self, mode: "Literal['model']", **kwargs: Any) -> Product:
        """Pass in mode='model' to get a handwritten model out"""
    
    @overload
    def get_model(self, mode: str, **kwargs: Any):
        """Pass in other modes"""
        raise Exception("No Implementation")

    async def get_model(self, *args, **kwargs: Any) -> Union[JSONType, Product]:
        model_mode = mode_checks(*args, **kwargs)
        response = await super().get_model(*args, **kwargs)
        if model_mode:
            return Product.deserialize(response)
        return response

    @overload
    async def post_model(self, mode: "Literal['raw']", input: JSONType, **kwargs: Any) -> JSONType:
        """Pass in mode='raw' to pass in raw json"""

    @overload
    async def post_model(self, mode: "Literal['model']", input: Input, **kwargs: Any) -> Product:
        """Pass in mode='model' to pass in model"""

    @overload
    def post_model(self, mode: str, input: Input, **kwargs: Any):
        """Pass in other modes"""
        raise Exception("No Implementation")

    async def post_model(self, *args, **kwargs: Any) -> JSONType:
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            if len(args) > 1:
                args = list(args)  # type: ignore
                args[1] = Input.serialize(args[1])  # type: ignore  # pylint: disable=expression-not-assigned
            else:
                kwargs["input"] == Input.serialize(kwargs["input"])  # pylint: disable=expression-not-assigned
        response = await super().post_model(*args, **kwargs)
        if model_mode:
            return Product.deserialize(response)
        return response

    @overload
    def get_pages(self, mode: "Literal['raw']", **kwargs) -> AsyncItemPaged[JSONType]:
        """Pass in mode='raw' to pass for raw json"""

    @overload
    def get_pages(self, mode: "Literal['model']", **kwargs) -> AsyncItemPaged[Product]:
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
    async def begin_lro(self, mode: "Literal['raw']", **kwargs) -> AsyncLROPoller[JSONType]:
        """Pass in mode='raw' to pass for raw json"""

    @overload
    async def begin_lro(self, mode: "Literal['model']", **kwargs) -> AsyncLROPoller[LROProduct]:
        """Pass in mode='model' to pass for raw json"""

    @overload
    def begin_lro(self, mode: str, **kwargs: Any):
        """Pass in other modes"""
        raise Exception("No Implementation")

    async def begin_lro(self, *args, **kwargs: Any):
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            kwargs["cls"] = lambda pipeline_response, deserialized, headers: LROProduct.deserialize(pipeline_response)
        return await super().begin_lro(*args, **kwargs)


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't otherwise do with the following handwritten customizations framework
    aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__ = [
    "DPGClientOperationsMixin"
]  # only add objects you want to be publicly available to your users at your package level
