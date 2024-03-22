# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azurecore.lro.rpclegacy import LegacyClient, models


@pytest.fixture
def client():
    with LegacyClient() as client:
        yield client


def test_begin_create_job(client: LegacyClient, polling_method):
    result = client.create_resource_poll_via_operation_location.begin_create_job(
        models.JobData(comment="async job"), polling_interval=0, polling=polling_method
    ).result()
    assert result == models.JobResult(
        job_id="job1",
        comment="async job",
        status=models.JobStatus.SUCCEEDED,
        results=["job1 result"],
    )

def test_begin_create_model(client: LegacyClient, polling_method):
    expected = {"modelId": "123", "description": "hello"}
    result = client.create_resource_poll_via_operation_location_and_resource_location.begin_build_model(
        models.DocumentModel(expected), polling_interval=0, polling=polling_method
    ).result()
    assert result == models.DocumentModelDetails(expected)
