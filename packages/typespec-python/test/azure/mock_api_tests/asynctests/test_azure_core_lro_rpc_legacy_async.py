# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azurecore.lro.rpclegacy.aio import LegacyClient
from azurecore.lro.rpclegacy import models


@pytest.fixture
async def client():
    async with LegacyClient() as client:
        yield client


# cadl-ranch check api-version in poll request which is not supported by azure-core
@pytest.mark.asyncio
async def test_begin_create_job(client: LegacyClient):
    result = await (
        await client.begin_create_job(
            models.JobData(comment="async job"), polling_interval=0
        )
    ).result()
    assert result == models.JobResult(
        job_id="job1",
        comment="async job",
        status=models.JobStatus.SUCCEEDED,
        results=["job1 result"],
    )
