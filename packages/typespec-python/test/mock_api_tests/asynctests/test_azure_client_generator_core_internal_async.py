# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# import pytest
# from internal import models
# from internal.aio import InternalClient


# @pytest.fixture
# async def client():
#     async with InternalClient() as client:
#         yield client


# @pytest.mark.asyncio
# async def test_get_internal(client: InternalClient):
#     result = await client._get_internal(name="test")
#     assert result.name == "test"


# @pytest.mark.asyncio
# async def test_post_internal(client: InternalClient):
#     result = await client._post_internal(
#         models.ModelOnlyUsedByInternalOperation(id=1, name="test")
#     )
#     assert result.name == "test"
