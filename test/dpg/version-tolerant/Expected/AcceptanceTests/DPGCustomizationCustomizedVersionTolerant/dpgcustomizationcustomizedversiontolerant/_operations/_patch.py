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
from typing import Any, overload, Union, Literal
from azure.core.paging import ItemPaged
from ..models import *
from ._operations import DPGClientOperationsMixin as DPGClientOperationsMixinGenerated, JSONType

def mode_checks(*args, **kwargs: Any) -> bool:
    """Return whether model_mode is True"""
    if args:
        return args[0] == "model"
    if "mode" in kwargs:
        return kwargs["mode"] == "model"
    raise ValueError("You need to specify 'mode' equal to 'raw' or 'model'.")

class DPGClientOperationsMixin(DPGClientOperationsMixinGenerated):

    @overload
    def get_model(self, mode: Literal["raw"], **kwargs: Any) -> JSONType:
        """Pass in mode='raw' to get raw JSON out"""

    @overload
    def get_model(self, mode: Literal["model"], **kwargs: Any) -> Product:
        """Pass in mode='model' to get a handwritten model out"""

    def get_model(self, *args, **kwargs: Any) -> Union[JSONType, Product]:
        model_mode = mode_checks(*args, **kwargs)
        response = super().get_model(*args, **kwargs)
        if model_mode:
            return Product.deserialize(response)
        return response

    @overload
    def post_model(self, mode: Literal["raw"], input: JSONType, **kwargs: Any) -> JSONType:
        """Pass in mode='raw' to pass in raw json"""

    @overload
    def post_model(self, mode: Literal["model"], input: Input, **kwargs: Any) -> Product:
        """Pass in mode='model' to pass in model"""

    def post_model(self, *args, **kwargs: Any) -> JSONType:
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            if len(args) > 1:
                args = list(args)
                args[1] = Input.serialize(args[1])
            else:
                kwargs["input"] == Input.serialize(kwargs["input"])
        response = super().post_model(*args, **kwargs)
        if model_mode:
            return Product.deserialize(response)
        return response

    @overload
    def get_pages(self, mode: Literal["raw"], **kwargs) -> ItemPaged[JSONType]:
        """Pass in mode='raw' to pass for raw json"""

    @overload
    def get_pages(self, mode: Literal["model"], **kwargs) -> ItemPaged[Product]:
        """Pass in mode='model' to pass for raw json"""

    def get_pages(self, *args, **kwargs):
        model_mode = mode_checks(*args, **kwargs)
        if model_mode:
            kwargs['cls'] = lambda objs: [Product.deserialize(x) for x in objs]
        return super().get_pages(*args, **kwargs)

def patch_sdk():
    """Do not remove from this file"""
    pass


__all__ = ["patch_sdk", "DPGClientOperationsMixin"]  # do not remove "patch_sdk" from __all__
