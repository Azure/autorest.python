# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.model.record.aio import RecordTestClient
from typetest.model.record import models

@pytest.fixture
async def client():
    async with RecordTestClient() as client:
        yield client

model_record_unknown = models.ModelRecordUnknown({"prop1": 32, "prop2": True, "prop3": "abc", "name":"ModelRecordUnknown"})

@pytest.mark.asyncio
async def test_post_model_record_unknown(client):
    await client.post_model_record_unknown(model_record_unknown)

@pytest.mark.asyncio
async def test_get_model_record_unknown(client):
    assert await client.get_model_record_unknown() == model_record_unknown
