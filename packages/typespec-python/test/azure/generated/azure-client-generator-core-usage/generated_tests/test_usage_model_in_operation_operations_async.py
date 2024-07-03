# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import UsagePreparer
from testpreparer_async import UsageClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestUsageModelInOperationOperationsAsync(UsageClientTestBaseAsync):
    @UsagePreparer()
    @recorded_by_proxy_async
    async def test_input_to_input_output(self, usage_endpoint):
        client = self.create_async_client(endpoint=usage_endpoint)
        response = await client.model_in_operation.input_to_input_output(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy_async
    async def test_output_to_input_output(self, usage_endpoint):
        client = self.create_async_client(endpoint=usage_endpoint)
        response = await client.model_in_operation.output_to_input_output()

        # please add some check logic here by yourself
        # ...

    @UsagePreparer()
    @recorded_by_proxy_async
    async def test_model_in_read_only_property(self, usage_endpoint):
        client = self.create_async_client(endpoint=usage_endpoint)
        response = await client.model_in_operation.model_in_read_only_property(
            body={"result": {"name": "str"}},
        )

        # please add some check logic here by yourself
        # ...
