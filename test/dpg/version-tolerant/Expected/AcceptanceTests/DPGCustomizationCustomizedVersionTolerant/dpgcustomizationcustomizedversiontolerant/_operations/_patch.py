# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typing import Any, Iterable
from azure.core.polling import LROPoller
from ..models import *  # pylint: disable=wildcard-import,unused-wildcard-import
from ._operations import DPGClientOperationsMixin as DPGClientOperationsMixinGenerated


class DPGClientOperationsMixin(DPGClientOperationsMixinGenerated):
    def get_model(self, mode: str, **kwargs: Any) -> Product:
        response = super().get_model(mode, **kwargs)
        return Product(**response)

    def post_model(self, mode: str, input: Product, **kwargs: Any) -> Product:
        response = super().post_model(mode, input, **kwargs)
        return Product(**response)

    def get_pages(self, mode: str, **kwargs: Any) -> Iterable[Product]:
        return super().get_pages(mode, cls=lambda objs: [Product(**x) for x in objs], **kwargs)

    def begin_lro(self, mode: str, **kwargs: Any) -> LROPoller[LROProduct]:
        return super().begin_lro(
            mode,
            cls=lambda pipeline_response, deserialized, headers: LROProduct._from_dict(  # pylint: disable=protected-access
                **deserialized
            ),
            **kwargs
        )


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't otherwise do with the following handwritten customizations framework
    aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__ = [
    "DPGClientOperationsMixin"
]  # only add objects you want to be publicly available to your users at your package level
