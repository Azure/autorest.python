# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# will enable the test after https://github.com/Azure/typespec-azure/issues/2862 fixed
# import pytest
# from _specs_.azure.core.lro.rpc import RpcClient
# from _specs_.azure.core.lro.rpc.models import JobResult, JobData, JobPollResult

# @pytest.fixture
# def client():
#     with RpcClient() as client:
#         yield client

# EXPECTED_RESULT = JobResult({"jobId": "job1", "comment": "async job", "status": "Succeeded", "results": ["job1 result"]})

# def test_lro_rpc_put(client):
#     result = client.begin_create_job(body=JobData({"comment": "async job"}), polling_interval=0).result()
#     assert result == EXPECTED_RESULT

# def test_lro_rpc_get(client):
#     result = client.begin_get_job(job_id="job1", polling_interval=0).result()
#     assert result == EXPECTED_RESULT

# def test_lro_rpc_create_job_final_on_location(client):
#     result = client.begin_create_job_final_on_location(body=JobData({"comment": "async job"}), polling_interval=0).result()
#     assert result == EXPECTED_RESULT

# def test_lro_rpc_get_poll(client):
#     result = client.begin_get_poll(operation_id="operation1", polling_interval=0).result()
#     assert result == JobPollResult({"operationId": "operation1", "status": "Succeeded" })
