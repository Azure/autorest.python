# pylint: disable=line-too-long,useless-suppression
# pyright: reportUnnecessaryTypeIgnoreComment=false
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from typing import Any, cast
from azure.core.async_paging import AsyncItemPaged
from azure.core.polling import AsyncLROPoller

from ._operations import _DPGClientOperationsMixin as _DPGClientOperationsMixinGenerated
from ...models import *  # pylint: disable=wildcard-import,unused-wildcard-import


class _DPGClientOperationsMixin(_DPGClientOperationsMixinGenerated):
    async def get_model(self, mode: str, **kwargs: Any) -> Product:
        response = await super().get_model(mode, **kwargs)
        return Product(**response)

    async def post_model(self, mode: str, input: Input, **kwargs: Any) -> Product:  # type: ignore
        response = await super().post_model(mode, input, **kwargs)
        return Product(**response)

    def get_pages(self, mode: str, **kwargs) -> AsyncItemPaged[Product]:  # type: ignore
        pages = super().get_pages(mode, cls=lambda objs: [Product(**x) for x in objs], **kwargs)
        return cast(AsyncItemPaged[Product], pages)

    async def begin_lro(self, mode: str, **kwargs: Any) -> AsyncLROPoller[LROProduct]:  # type: ignore
        poller = await super().begin_lro(
            mode,
            cls=lambda pipeline_response, deserialized, headers: LROProduct._from_dict(  # pylint: disable=protected-access
                **deserialized
            ),
            **kwargs
        )
        return cast(AsyncLROPoller[LROProduct], poller)


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't otherwise do with the following handwritten customizations framework
    aka.ms/azsdk/python/dpcodegen/python/customize
    """


__all__ = [
    "_DPGClientOperationsMixin"
]  # only add objects you want to be publicly available to your users at your package level
