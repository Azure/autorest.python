# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azurecore.lro.rpclegacy import LegacyClient
from azurecore.lro.rpclegacy.models import JobResult, JobData

@pytest.fixture
def client():
    with LegacyClient() as client:
        yield client

def test_lro_rpc_legacy_create_job(client):
    result = client.begin_create_job(JobData(comment="async job"), polling_interval=0).result()
    assert result == JobResult({"jobId": "job1", "comment": "async job", "status": "succeeded", "results": ["job1 result"]})
