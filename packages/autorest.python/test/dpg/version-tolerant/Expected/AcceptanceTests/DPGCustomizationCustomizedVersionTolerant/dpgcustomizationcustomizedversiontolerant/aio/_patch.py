# pylint: disable=line-too-long,useless-suppression
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import List, Any, Union, cast, IO
from azure.core.async_paging import AsyncItemPaged
from azure.core.polling import AsyncLROPoller
from ..models import *  # pylint: disable=wildcard-import,unused-wildcard-import
from ._operations._operations import JSON
from ._client import DPGClient as DPGClientGenerated


class DPGClient(DPGClientGenerated):
    async def get_model(self, mode: str, **kwargs: Any) -> Product:
        response = await super().get_model(mode, **kwargs)
        return Product(**response)

    async def post_model(self, mode: str, input: Union[IO, Input, JSON], **kwargs: Any) -> Product:
        response = await super().post_model(mode, input, **kwargs)
        return Product(**response)

    def get_pages(self, mode: str, **kwargs: Any) -> AsyncItemPaged[Product]:  # type: ignore
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


__all__: List[str] = ["DPGClient"]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
