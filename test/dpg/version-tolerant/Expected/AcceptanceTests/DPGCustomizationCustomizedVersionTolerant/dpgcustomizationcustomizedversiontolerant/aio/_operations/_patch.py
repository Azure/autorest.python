# coding=utf-8
# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from typing import Any, Literal, Union, overload
from azure.core.polling import AsyncLROPoller
from ._operations import DPGClientOperationsMixin as DPGClientOperationsMixinGenerated, JSONType
from ...models import *
from ..._operations._patch import mode_checks
from azure.core.async_paging import AsyncItemPaged


class DPGClientOperationsMixin(DPGClientOperationsMixinGenerated):
    @overload
    async def get_model(self, mode: Literal["raw"], **kwargs: Any) -> JSONType:
        """Pass in mode='raw' to get raw JSON out"""

    @overload
    async def get_model(self, mode: Literal["model"], **kwargs: Any) -> Product:
        """Pass in mode='model' to get a handwritten model out"""

    async def get_model(self, *args, **kwargs: Any) -> Union[JSONType, Product]:
        model_mode = mode_checks(*args, **kwargs)
        response = await super().get_model(*args, **kwargs)
        if model_mode:
            return Product.deserialize(response)
        return response

    @overload
    async def post_model(self, mode: Literal["raw"], input: JSONType, **kwargs: Any) -> JSONType:
        """Pass in mode='raw' to pass in raw json"""

    @overload
    async def post_model(self, mode: Literal["model"], input: Input, **kwargs: Any) -> Product:
        """Pass in mode='model' to pass in model"""

    async def post_model(self, *args, **kwargs: Any) -> JSONType:
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            if len(args) > 1:
                args = list(args)
                args[1] = Input.serialize(args[1])
            else:
                kwargs["input"] == Input.serialize(kwargs["input"])
        response = await super().post_model(*args, **kwargs)
        if model_mode:
            return Product.deserialize(response)
        return response

    @overload
    def get_pages(self, mode: Literal["raw"], **kwargs) -> AsyncItemPaged[JSONType]:
        """Pass in mode='raw' to pass for raw json"""

    @overload
    def get_pages(self, mode: Literal["model"], **kwargs) -> AsyncItemPaged[Product]:
        """Pass in mode='model' to pass for raw json"""

    def get_pages(self, *args, **kwargs):
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            kwargs["cls"] = lambda objs: [Product.deserialize(x) for x in objs]
        return super().get_pages(*args, **kwargs)

    @overload
    async def begin_lro(self, mode: Literal["raw"], **kwargs) -> AsyncLROPoller[JSONType]:
        """Pass in mode='raw' to pass for raw json"""

    @overload
    async def begin_lro(self, mode: Literal["model"], **kwargs) -> AsyncLROPoller[LROProduct]:
        """Pass in mode='model' to pass for raw json"""

    async def begin_lro(self, *args, **kwargs: Any):
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            kwargs["cls"] = lambda pipeline_response, deserialized, headers: LROProduct.deserialize(pipeline_response)
        return await super().begin_lro(*args, **kwargs)


def patch_sdk():
    """Do not remove from this file"""
    pass


__all__ = ["DPGClientOperationsMixin"]  # do not remove "patch_sdk" from __all__
