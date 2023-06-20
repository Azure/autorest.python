# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from skip.special.headers.aio import TraitsClient

@pytest.fixture
async def client():
    async with TraitsClient() as client:
        yield client

@pytest.mark.asyncio
async def test_skip_special_headers(client: TraitsClient):
    with pytest.raises(TypeError):
        await client.smoke_test(
            id=1,
            foo="123",
            if_match='"valid"',
        )
    
    with pytest.raises(TypeError):
        await client.smoke_test(
            id=1,
            foo="123",
            client_request_id="test-id",
        )
