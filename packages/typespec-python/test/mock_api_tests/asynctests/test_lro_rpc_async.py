# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from _specs_.azure.core.lro.rpc.aio import RpcClient
from _specs_.azure.core.lro.rpc.models import JobResult, JobData, JobPollResult

@pytest.fixture
async def client():
    async with RpcClient() as client:
        yield client

EXPECTED_RESULT = JobResult({"jobId": "job1", "comment": "async job", "status": "Succeeded", "results": ["job1 result"]})

@pytest.mark.asyncio
async def test_lro_rpc_put(client):
    result = await (await client.begin_create_job(body=JobData({"comment": "async job"}), polling_interval=0)).result()
    assert result == EXPECTED_RESULT

@pytest.mark.asyncio
async def test_lro_rpc_get(client):
    result = await (await client.begin_get_job(job_id="job1", polling_interval=0)).result()
    assert result == EXPECTED_RESULT

@pytest.mark.asyncio
async def test_lro_rpc_create_job_final_on_location(client):
    result = await (await client.begin_create_job_final_on_location(body=JobData({"comment": "async job"}), polling_interval=0)).result()
    assert result == EXPECTED_RESULT

@pytest.mark.asyncio
async def test_lro_rpc_get_poll(client):
    result = await (await client.begin_get_poll(operation_id="operation1", polling_interval=0)).result()
    assert result == JobPollResult({"operationId": "operation1", "status": "Succeeded" })
