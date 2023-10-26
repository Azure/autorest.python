# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.property.valuetypes.aio import ValueTypesClient
from typetest.property.valuetypes import models
from azure.core.exceptions import HttpResponseError

@pytest.fixture
async def client():
    async with ValueTypesClient() as client:
        yield client

@pytest.mark.asyncio
async def test_stream(client):
    # normal response
    response = await client.string.get(stream=True)
    result = b""
    async for item in response:
        result += item
    assert result == b'{"property":"hello"}'

    # raise exception
    try:
        await client.string.put(models.StringProperty(property="wrong"), stream=True)
    except HttpResponseError as err:
        assert err.error is not None
    else:
        raise Exception("HttpResponseError not raised")
