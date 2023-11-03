# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.model.nestedproperty.aio import NestedPropertyClient
from typetest.model.nestedproperty.models import Extension


@pytest.fixture
async def client():
    async with NestedPropertyClient() as client:
        yield client

@pytest.fixture
async def expected():
    return Extension({
  "extension": [
    {
      "level": 1,
      "extension": [
        {
          "level": 2
        }
      ]
    },
    {
      "level": 1
    }
  ]
})

@pytest.mark.asyncio
async def test_put(client: NestedPropertyClient, expected: Extension):
    await client.put(expected)


@pytest.mark.asyncio
async def test_get(client: NestedPropertyClient, expected: Extension):
    assert await client.get() == expected

