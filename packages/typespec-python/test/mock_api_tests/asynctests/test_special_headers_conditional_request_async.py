# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.core import MatchConditions
from specialheaders.conditionalrequest.aio import ConditionalRequestClient

@pytest.fixture
async def client():
    async with ConditionalRequestClient() as client:
        yield client

@pytest.mark.asyncio
async def test_post_if_match(client: ConditionalRequestClient):
    await client.post_if_match(etag="valid", match_condition=MatchConditions.IfNotModified)

@pytest.mark.asyncio
async def test_post_if_none_match(client: ConditionalRequestClient):
    await client.post_if_none_match(etag="invalid", match_condition=MatchConditions.IfModified)
